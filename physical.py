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
