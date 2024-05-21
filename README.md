# Role

---

Within my **computing sub-team**, ***I*** took the role of the manager, which consists of the following main responsibilities:

- Facilitate discourse among team members and with 1P13 instructional team
- Promote an equitable work environment
- Assume a leadership role in identifying and managing team conflict
- Assume the role of Design Studio Chair during scheduled weekly meetings
- Complete and submit Preliminary Gantt Chart

# Time-chart

---

Our project was split amongst various parts which we call **“milestones”**. As the manager, ***I*** came up with a Gantt chart that helped us organize our time and complete the project by the given deadline.

<img width="1385" alt="1" src="https://github.com/AHMEDELZARIA/Recover-JPEG/assets/93144563/96dc737d-2a46-472c-91a2-eca834169152">
Gantt chart of project 3, outlining the start and end of given tasks, “milestones”, and design project report

# Design Process

---

Before we dive into the design process, it is important to provide some context. **Recycling plants need an automated system to sort and properly place recyclable containers to isolate the garbage mixed in to optimize the recycling process.** In a controlled virtual and physical environment, we can create our own recycling station with sorting capabilities. In this project, our team was provided with lots of possible sensors, allowing us to determine what container we are working with and whether that container can be recycled. By the end **we** would have effectively sorted containers into their correct bin locations.

## 1. Defining Functions, Objectives, and Constraints

As per every project we do. **We** first **must aim to understand the overall problem** that we are dealing with. A great way to develop a problem statement is to first and foremost, understand the **function(s), objectives, and constraints** your system possesses. As a team, we came up with the following table that effectively highlights these aspects:
| Objectives | Constraints | Function(s) |
| --- | --- | --- |
| Computing solution should avoid obstacles | Cannot use external robotics or manufactured parts | Sort and recycle containers into correct corresponding bin |
| Computing solution should be very accurate in determining if container is recyclable or not | Q-bot must travel along yellow path |  |
| Should be able to identify the presence of a container | Q-arm should only pick up and load containers if there are fewer than 3 containers already on the Q-bot, new container in sorting station is to be transferred to the same bin as existing containers on Q-bot, and the total mass of all containers on Q-bot is less than 90 grams |  |
| Should be able to verify that bottles are clean or contaminated | Cannot use expensive sourced materials |  |
| Should be able to classify the material of the container | Cannot use tools and equipment not available in Design Studio |  |
| Should be able to transfer container to correct bin | Cannot use anything deemed to be unsafe by a TA, faculty mentor or staff member |  |
| Should be able to deposit containers into correct bin |  |  |

After classifying our objectives, constraints, and functions. **We** were now ready to start writing some pseudocode to better understand the algorithm and flow of our solution. 

## 2. Pseudocode, Algorithm Development, and Program Flow

The following is the initial flow of the computer program:
```
Start program 

  

Dispense container function 

    Randomly dispense a container onto the turn table 

    Determine the material, mass, and bin using sensors 

    Return this information for future use 

  

Load container function 

    Check to see if the q-bot has less than 3 bottles 

    Check to see if the mass is less than 90 grams 

    Ensure that the new container goes to the same bin as a 

    container on the q-bot 

  

    If all conditions satisfied, move q-arm to pick up position 

    Pick up container with q-arm and transfer container to 

    hopper 

    Move q-arm back to home position 

 

    If q-bot has 3 bottles, stop container selection 

    If the mass is equal or will be greater than 90, stop 

    container selection 

    If new container does not have same bin location, leave it 

    on the turn table 

  

Q-bot moving function 

    Follow yellow path to correct bin where containers will be 

    disposed using sensors 

    Identify the correct bin using sensor 

    Follow the bin path to move beside the bin 

    Rotate for the hopper to be adjacent to the bin 

    Activate mechanism to lift hopper and drop containers into 

    Bin 

    Follow yellow path back to home position to collect new 

    containers 

  

Once containers are disposed of correctly, terminate program
```

I developed a storyboard to better understand the steps of the program and to visualize what the solution should look like:

<img width="505" alt="2" src="https://github.com/AHMEDELZARIA/Recover-JPEG/assets/93144563/9a3509b7-fae3-4af5-a290-462c5bb47988">

We then combined our program flow and storyboard to develop pseudocode:
```
function dispense container:
    dispense container 
    calculate inductive average
    calculate container mass
    calculate photoelectric average

    If inductive reading indicates metal:
        set material attribute to paper
        set bin attribute to bin01
    Else:
        If photoelectric average indicates paper:
            set material attribute to paper
            If container mass indicates clean:
                set bin attribute to bin02
            Else:
                set bin attribute to bin04
        Else:
            set material attribute to bin04
            If container mass indicates clean:
                set bin attribute to bin03
            Else:
                set bin attribute to bin04
    return list of bin attribute, container mass

function load container:
    get list of container attributes
    set pickup coordinates in variable
    initialize bottle counter variable
    initialize total mass variable

    while number of containers on q-bot is less than 3 and new container to be placed container to be placed is same destination and total mass is less than 90 grams:
        q-arm travels to container
        q-arm picks up container
        q-arm transfers and drops container on q-bot hopper
        increment number of containers
        increment total mass

function transfer container:
    activate q-bot movement sensor to move q-bot along yellowline
    activate colour sensor
    activate ultrasonic sensor

        If desired bin colour is detected:
            stop q-bot
            calculate distance from bin
            move q-bot to desired distance

function deposit container:
    activate hopper
    dispense containers in bin
    return hopper back to original state

function return home:
    activate q-bot movement sensor
    move q-bot along yellow line forward
    travel until home coordinates are reached
    stop q-bot
```
## 3. Virtual Environment Code Development

Now that we had a good idea of how the program should run, I was ready to take it onto the Q-Labs virtual environment to start writing out the code. Below are a few images to help visualize the virtual environment we were working with.

<img width="358" alt="3" src="https://github.com/AHMEDELZARIA/Recover-JPEG/assets/93144563/63332b26-07b8-411d-a52b-0caf06abfadf">

Sorting Station where containers are dispensed from the tube [1]

![Q-arm, which will pick up containers from sorting station and transfer them to q-bot hopper. Q-bot, which will take containers and drop them off at their correct bin. This is also the home location of the q-bot. [1]](https://github.com/AHMEDELZARIA/Recover-JPEG/assets/93144563/8997636a-f354-4f37-ac8f-bc98dba9b822)

Q-arm, which will pick up containers from sorting station and transfer them to q-bot hopper. Q-bot, which will take containers and drop them off at their correct bin. This is also the home location of the q-bot. [1]

![4 possible bins for drop-off. Q-bot travels along yellow line in one direction only. [1]](https://github.com/AHMEDELZARIA/Recover-JPEG/assets/93144563/7d530879-38e7-49ea-b4a5-49cb1ccd9ea6)

4 possible bins for drop-off. Q-bot travels along yellow line in one direction only. [1]

![Drop-off process. With the help of a linear actuator, the hopper is activated and tilted to dump containers in bin. [1]](https://github.com/AHMEDELZARIA/Recover-JPEG/assets/93144563/2ca6cb73-9098-4608-880a-d9c519fae83a)

Drop-off process. With the help of a linear actuator, the hopper is activated and tilted to dump containers in bin. [1]

### Table 1 List of Container Attributes [1]
| ID | Q-Lab Render | Material  | Mass(g) | Contamination | Target Bin |
| --- | --- | --- | --- | --- | --- |
| 01 | White bottle | Plastic  | approx. 9.25 | Clean | Bin03 |
| 02 | Red can  | Metal | approx. 15.0 | Clean | Bin01 |
| 03 | Blue bottle | Paper | approx. 10.0 | Clean | Bin02 |
| 04 | White bottle | Plastic | > 9.25 | Dirty | Bin04 |
| 05 | Red can | Metal | > 15.0 | Dirty | Bin01 |
| 06 | Blue bottle | Paper | > 10.0 | Dirty | Bin04 |

Table 2 List of Sensors Available to Virtually Mount to the Q-bot [1]
| Ultrasonic Sensor | LDR (Light Dependent Resistor) |
| --- | --- |
| Active Infrared (IR) Sensor | Color Sensor |
| Hall Effect Sensor |  |

**We** decided to use the colour sensor which returns RGB values. We would look for the RGB values in order to know when to stop when Q-bot has reached the bin. 

After a lot of tweaking, testing, and debugging. ***I*** was able to develop the following code which effectively classifies the dispensed container(s) attributes, determines bin destination, commands q-arm to pick up and transfer containers to q-bot hopper, command the q-bot to drop-off containers and travel home, and then repeat until told else wise.

```python
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
```
[Check out this YouTube video for a demonstration of the dispense, pickup, transfer, and travel process.](https://www.youtube.com/watch?v=G3dEqA3ELUk)

## 4. Physical Environment Code Development

After successfully developing virtual environment code, **we** took it to the physical environment, which is less complicated, to develop the code in real life. We utilized the ultrasonic sensor to sense when the Q-bot had reached the bin. The physical environment consists of a Q-bot, which is loaded with containers prior, which would then travel along the yellow path until it reaches the bin and drops-off the containers.

![Physical Environment. Containers are loaded onto Q-bot hopper prior to running of program. Yellow path indicates path of travel of Q-bot. White bin is the recycling bin in this environment. [1]](https://github.com/AHMEDELZARIA/Recover-JPEG/assets/93144563/7c1e1bb9-8fb5-48fe-a145-4a2eb33963ab)

Physical Environment. Containers are loaded onto Q-bot hopper prior to running of program. Yellow path indicates path of travel of Q-bot. White bin is the recycling bin in this environment. [1]

With this given environment, I developed the following code:

```python
ip_address = '172.17.42.73' # Enter your IP Address here
project_identifier = 'P3B' # Enter the project identifier i.e. P3A or P3B
#--------------------------------------------------------------------------------
import sys
sys.path.append('../')
from Common.hardware_project_library import *

hardware = True
QLabs = configure_environment(project_identifier, ip_address, hardware).QLabs
if project_identifier == 'P3A':
    arm = qarm(project_identifier,ip_address,QLabs,hardware)
    table = servo_table(ip_address,QLabs,None,hardware)
else:
    speed = 0.1 # in m/s
    bot = qbot(speed,ip_address,QLabs,project_identifier,hardware)
#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------
def main():
    bot.activate_line_following_sensor() # Activate line sensor
    bot.activate_ultrasonic_sensor() # Activate the ultrasonic sensor

    bin_reached = False # Tracks if the q-bot has reached the bin
    
    # While the q-bot hasn't reached the bin yet
    while bin_reached == False:
        ultrasonic_reading = bot.read_ultrasonic_sensor()
        print(ultrasonic_reading)

        # If bin distance is reached 
        if ultrasonic_reading >= 0.01 and ultrasonic_reading <= 0.05:
            bot.stop() # Stop the q-bot
            # Deactivate the sensors
            bot.deactivate_line_following_sensor()         
            bot.deactivate_ultrasonic_sensor()
            # Update loop control variable and break just in case
            bin_reached == True
            break
        else:
            # Read left and right ir sensor reading
            ir_reading = bot.line_following_sensors()
            left_ir = ir_reading[0]
            right_ir = ir_reading[1]
                
            # if sraight movement, move straight
            if left_ir == 1 and right_ir == 1:
                bot.set_wheel_speed([0.025, 0.025])
            # else if left turn approaching, turn left
            elif left_ir == 1 and right_ir == 0:
                bot.set_wheel_speed([0.01, 0.05])
            # else if right turn approaching, turn right
            elif left_ir == 0 and right_ir == 1:
                bot.set_wheel_speed([0.05, 0.01])
            # if q-bot falls off track, move slightly until line is detected
            else:
                bot.set_wheel_speed([0.00, 0.01])

    
    # Move the bot slightly up to align with bin           
    time.sleep(2)
    bot.forward_time(1)

    # Dump the containers in the bin 
    bot.activate_linear_actuator()
    bot.linear_actuator_out(5)
    time.sleep(2)
    bot.linear_actuator_in(5)
    time.sleep(2)
    bot.deactivate_linear_actuator()
```
The following is a [video](https://www.youtube.com/watch?v=mpEF0jYhEnE) demonstrating the result of the following code above

# Project Reflection

---

Throughout this project, ***I*** came to to finally **understand the importance of software testing**. Software testing is crucial for identifying and preventing inefficiencies and bugs in your software. Test your code under multiple different test cases allows one to ensure that the software performs as intended, even in extreme cases. 

Although I am satisfied with the final result of the software, there is always room for improvement that we must consider. Factors such as:

- **How can we ensure the Q-bot returns to the exact home position each iteration? Sometimes it isn’t aligned correctly and the next iteration fails as the Q-arm misses the Q-bot hopper.**
- **Rather than hardcoding the Q-arms travel and drop-off of containers, is there a way for the Q-arm to sense the location of the Q-bot hopper and use this information for more accurate transfer of containers? This would potentially fix the complaint above.**
- **How can we scale up the design? Currently the process is very slow and in a real life setting, we would need more robots and quicker travel time.**
    
    ## Learning Experience
    
    This project helped me greatly in **3 departments, software testing, debugging, and algorithm design** . Prior to this project, I had not tested a program more than I did in this project. Each component of the program required a ton of testing **to ensure all cases are met**. This taught me the importance of testing as there are so many cases to consider and the more you test, the more reliable the software is. In terms of **debugging**, there were multiple times throughout this project where my code was not working. For example, the Q-bot was falling off track, containers wouldn’t fall into their respective containers, Q-bot struggles to return home, etc. All these situations where opportunities for me to look through code and identify where the bugs occurred. The interface ***I*** was using also did not provide much detail as to where the errors occur as modern day IDE’s do, so this forced me to break down code line by line to understand where logical and syntactical errors would occur. Finally, this system was broken down into multiple functions that work together to create a successful recycling system. **Each function needed its own algorithm** which **we** broke down and implemented. This process helped me immensely in terms of **problem solving** as we were able to take a big problem and break it into small simple commands for the computer. 
    
    In terms of soft skills, this project helped me in terms of being a **project manager**. I was always on top of tasks and ensuring each one of my group members was on track. This project taught me l**eadership within a professional setting, communication, time management, and organization.** 
    

# Sources

---

[1] McMaster University Engineering 1P13 Staff, “1 – P3 Project Module”, *Avenue to learn*, 2023. [Online]. Available: https://avenue.cllmcmaster.ca/d2l/le/content/486894/viewContent/4019352/View. [Accessed Jan. 13, 2022]
