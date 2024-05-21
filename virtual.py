ip_address = 'localhost' # Enter your IP Address here
project_identifier = 'P3B' # Enter the project identifier i.e. P3A or P3B
hardware = False # True when working with hardware. False when working in the simulation

# SERVO TABLE CONFIGURATION
short_tower_angle = 270 # enter the value in degrees for the identification tower 
tall_tower_angle = 0 # enter the value in degrees for the classification tower
drop_tube_angle = 180 # enter the value in degrees for the drop tube. clockwise rotation from zero degrees

# 3. Qbot Configuration
bot_camera_angle = -21.5 # angle in degrees between -21.5 and 0

# BIN CONFIGURATION
# Configuration for the colors for the bins and the lines leading to those bins.
# Note: The line leading up to the bin will be the same color as the bin 

bin1_offset = 0.15 # offset in meters
bin1_color = [1,0,0] # e.g. [1,0,0] for red
bin1_metallic = False

bin2_offset = 0.15
bin2_color = [0,1,0]
bin2_metallic = False

bin3_offset = 0.15
bin3_color = [0,0,1]
bin3_metallic = False

bin4_offset = 0.15
bin4_color = [0,1,1]
bin4_metallic = False
#--------------------------------------------------------------------------------
import sys
sys.path.append('../')
from Common.simulation_project_library import *

hardware = False
if project_identifier == 'P3A':
    table_configuration = [short_tower_angle,tall_tower_angle,drop_tube_angle]
    configuration_information = [table_configuration, None] # Configuring just the table
    QLabs = configure_environment(project_identifier, ip_address, hardware,configuration_information).QLabs
    table = servo_table(ip_address,QLabs,table_configuration,hardware)
    arm = qarm(project_identifier,ip_address,QLabs,hardware)
else:
    table_configuration = [short_tower_angle,tall_tower_angle,drop_tube_angle]
    bin_configuration = [[bin1_offset,bin2_offset,bin3_offset,bin4_offset],[bin1_color,bin2_color,bin3_color,bin4_color],[bin1_metallic,bin2_metallic, bin3_metallic,bin4_metallic]]
    configuration_information = [table_configuration, bin_configuration]
    QLabs = configure_environment(project_identifier, ip_address, hardware,configuration_information).QLabs
    table = servo_table(ip_address,QLabs,table_configuration,hardware)
    arm = qarm(project_identifier,ip_address,QLabs,hardware)
    bot = qbot(0.1,ip_address,QLabs,project_identifier,hardware)
#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------


home_qarm = [0.406, 0.0, 0.483] # Home location of Q-arm
home_qbot = [1.4660494327545166, 0.04666011780500412, 0.000756654713768512]


mass = 0
total_mass = 0
bin_location = None
no_container = True
bin_destination = None

# Pickup actions of q-arm with containers
def pick_up():
    arm.rotate_elbow(-30)
    time.sleep(1)
    arm.rotate_shoulder(45)
    time.sleep(1)
    arm.control_gripper(45)
    time.sleep(1)

# Moves the qarm home
def move_home():
    arm.move_arm(0.406, 0.0, 0.483)
    time.sleep(1)

# Drops the first container in correct position on hopper, first position
def drop_off1():
    move_home()
    arm.rotate_elbow(-10)
    time.sleep(1)
    arm.rotate_base(-88)
    time.sleep(1)
    arm.rotate_shoulder(5)
    time.sleep(1)
    arm.rotate_elbow(-70)
    time.sleep(1)
    arm.rotate_shoulder(20)
    time.sleep(1)
    arm.rotate_elbow(20)
    time.sleep(1)
    arm.rotate_shoulder(10)
    time.sleep(1)
    arm.control_gripper(-45)
    time.sleep(1)
    arm.home()
    time.sleep(1)

# Drops the second container in correct position on hopper, second position
def drop_off2():
    move_home()
    arm.rotate_elbow(-15)
    time.sleep(1)
    arm.rotate_base(-88)
    time.sleep(1)
    arm.rotate_shoulder(5)
    time.sleep(1)
    arm.rotate_elbow(-5)
    time.sleep(1)
    arm.rotate_shoulder(5)
    time.sleep(1)                      
    arm.rotate_elbow(-5)
    time.sleep(1)
    arm.rotate_shoulder(10)
    time.sleep(1)
    arm.control_gripper(-45)
    time.sleep(1)
    arm.home()
    time.sleep(1)

# Drops the third container in correct position on hopper, third position
def drop_off3():
    move_home()
    arm.rotate_elbow(-10)
    time.sleep(1)
    arm.rotate_base(-88)
    time.sleep(1)
    arm.rotate_shoulder(10)
    time.sleep(1)
    arm.control_gripper(-45)
    time.sleep(1)
    arm.rotate_shoulder(-15)
    time.sleep(1)
    arm.home()
    time.sleep(1)

# Function that allows the q-bot to move amongst the yellow path
def line_following(): 
    #Read left_IR and right_IR sensors
    ir_reading = bot.line_following_sensors()
    left_ir = ir_reading[0]
    right_ir = ir_reading[1]

    # if straight movement, move straight
    if left_ir == 1 and right_ir == 1:
        bot.set_wheel_speed([0.05, 0.05])
    # if left turn approaching, turn left
    elif left_ir == 1 and right_ir == 0:
        bot.set_wheel_speed([0.05, 0.1])
    # if right turn approaching, turn right
    elif left_ir == 0 and right_ir == 1:
        bot.set_wheel_speed([0.1, 0.05])
    # if q-bot falls off track, move slightly back on track
    else:
        bot.set_wheel_speed([0.01, 0])
            

# Function that dispenses a container onto the servo table and returns the attributes of the container
def dispense_container():
    
    # Randomly spawns contaminated or non contaminated container out of 6 possibilities
    spawned_container = table.dispense_container(random.randint(1, 6), True)
    print(spawned_container)

    # return container attributes [material, mass, bin destination]
    return spawned_container
    

# Function that loads containers onto Q-bot with the use of the Q_arm
def load_container():
    global total_mass, mass, bin_location, no_container, bin_destination

    # loops over a max of three dispensed containers
    for i in range(3):
        # if first cinbtainer in cycle
        if i == 0:
            # if no container is already on servo table
            if no_container == True:
                container = dispense_container()
                pick_up()
                drop_off1()
                mass = container[1] # mass of current container
                total_mass = mass # total mass on hopper
                bin_location = container[2] # holds the bin destination of current cycle
                no_container = False # update this variable to indicate that next time there will be a container on table
            # if there is already a container on servo table
            else:
                pick_up()
                drop_off1()

        # if not the frst container dispensed in cycle
        else:
            next_container = dispense_container()
            mass = next_container[1]
            next_bin_location = next_container[2] # holds the bin destination of next container 
            total_mass += mass

            # If next container satisfies conditions
            if (total_mass < 90 and next_bin_location == bin_location):
                pick_up()
                if i == 1: # If second bottle in cycle
                    drop_off2()
                else: # If third bottle in cycle
                    drop_off3()
                    no_container = True
                    bin_destination = bin_location # after last conatiner has been placed, set the next cycles bin destination to currently dispensed container bin destination
            else:
                bin_destination = bin_location
                bin_location = next_bin_location
                total_mass = mass
                break


        
# Function that transfers the container to the correct bin via the q-bot
def transfer_container():

    global bin1_color, bin2_color, bin3_color, bin4_color, bin_destination
    bin_reached = False
    counter = 0
    
    
    # Identify target bin's color
    if bin_destination == 'Bin01':
        color = bin1_color
    elif bin_destination == 'Bin02':
        color = bin2_color
    elif bin_destination == 'Bin03':
        color = bin3_color
    elif bin_destination == 'Bin04':
        color = bin4_color

    print(bin_destination)

    # Activate bot sensors for detecting the target bin
    bot.activate_color_sensor()
    bot.activate_line_following_sensor()
    
    # while the target bin hasn't been reached 
    while (bin_reached != True):
        line_following() # keep moving q-bot along path
        sensor_reading = bot.read_color_sensor() # reads the sensor info of color sensor
        
        # if colour of bin is detected, keep moving in order to align correctly
        if sensor_reading[0] == color:
            if color == bin1_color and counter < 10:
                line_following()
                counter+=1
            elif color == bin2_color and counter < 7:
                line_following()
                counter+=1
            elif color == bin3_color and counter < 14:
                line_following()
                counter+=1
            elif color == bin4_color and counter < 7:
                line_following()
                counter+=1
            else: # after q-bot is aligned with bin
                bot.stop() # stopp q-bot and rotate the bin to further align better with bin
                if color == bin1_color:
                    bot.rotate(-5) 
                elif color == bin2_color:
                    bot.rotate(-7)
                elif color == bin3_color:
                    bot.rotate(-4)
                else:
                    bot.rotate(20) 
                bin_reached = True
    
    # Deactivate the color sensor when done identifying the bin
    bot.deactivate_color_sensor()     

# Function that activates the hopper on q-bot and deposits the containers in the target bin
def deposit_container():
    bot.activate_stepper_motor() # activate rotary actuator
    time.sleep(2)
    bot.rotate_hopper(45) # tilt hopper down
    time.sleep(2)
    bot.rotate_hopper(-45) # tilt hopper up
    time.sleep(2)
    bot.deactivate_stepper_motor()  # deactivate rotary actuator when done

# Function that returns the q-bot home
def return_home():
    global home_qbot # holds the main home position of q-bot
    reached_home = False # Tracks whether the q-bot has reached home or not
    position_qbot = bot.position() # Holds the current position of q-bot
    
    # While the q-bot hasn't reached home
    while reached_home == False:
        line_following() # Keep moving bot
        # Add an offset to the q-bots home position to ensure that the q-bot actually stops due to nonrepeatable movement each cycle
        if (position_qbot[0] < (home_qbot[0] + 0.0055) and position_qbot[1] < (home_qbot[1] + 0.0055)) and (position_qbot[0] > (home_qbot[0] - 0.0055) and position_qbot[1] < (home_qbot[1] - 0.0055)):
            bot.stop()
            reached_home = True
        position_qbot = bot.position()
        
    # Align the bot correctly
    bot.rotate(-15)
    
        
    
    
# Function that combines the program together
def main():
    end_cycles = input("Are you done? ")

    # Repeat program until the user says otherwise
    while (end_cycles == "No"):
        load_container()
        transfer_container()
        deposit_container()
        return_home()
        end_cycles = input("Are you done? ")
