#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
crane = Motor(Port.C)

# Write your program here.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=140)
robot.settings(1000, 500, 150, 150)

#crane.run_time(-1000,1000)

#using temporary values
def windmillRun():
    robot.straight(280)
    robot.straight(-200)
    robot.turn(-31) #45
    robot.straight(480)
    robot.turn(62) #90
    robot.straight(400)
    robot.straight(-150)
    robot.straight(400)
    robot.straight(-150)
    robot.straight(400)
    robot.straight(-150)
    robot.turn(-53)
    robot.straight(-600)

def batteryRun():
    crane.run_angle(500, -360, wait=False)
    robot.straight(480)
    crane.run_angle(500, 540, wait=True)
    robot.straight(-480)
    crane.run_angle(1000, -1440, wait=True)

def driveAcross():
    robot.straight(800)
    robot.turn(-15)
    robot.straight(800)

def boxRun():
    robot.straight(390)
    robot.turn(-21)
    robot.straight(250) # Reaches box
    crane.run_angle(500, 900, wait=True) # Empties basket
    robot.straight(-240)
    crane.run_angle(500, 360, wait=False) # Resets arm
    robot.turn(16) # Aims for power farm
    robot.straight(400) # Removes first 2 power units
    robot.turn(45) # Aims for unit 3
    robot.straight(300) # Removes 3rd unit
    robot.straight(-275)
    robot.turn(-43)
    robot.straight(-900) # Arrives back

def waterRun():
    robot.straight(360)
    crane.run_angle(1000, -1080, wait=True)
    crane.run_angle(1000, 1080, wait=True)
    robot.straight(-360)

def handRun():
    crane.run_angle(500, -360, wait=False)
    robot.straight(725)
    robot.turn(-48)
    robot.straight(450) # reached the hand
    crane.run_angle(500,560, wait=True) # crane goes down
    robot.straight(-50) # pulled lever back
    robot.straight(-50) # ...slowly
    crane.run_angle(500,-200, wait=True)
    robot.straight(-420)
    robot.turn(-83)
    robot.straight(820)


    '''
    robot.straight(-200)
    robot.turn(-150) #180 turn between hand and machine
    robot.straight(310)#reached machine
    crane.run_angle(500,540, wait=True)
    crane.run_angle(500,-1080, wait=True)
    crane.run_angle(500,540, wait=True) #machine task finished
    robot.straight(-30)
    robot.turn(-74)
    crane.run_angle(500, 810, wait=False)
    robot.straight(810)
    '''

while True:
    pressed = ev3.buttons.pressed()
    
    if Button.CENTER in pressed and Button.UP in pressed:
        crane.run_angle(1000, -5, wait=False)
    
    elif Button.CENTER in pressed and Button.DOWN in pressed:
        crane.run_angle(1000, 5, wait=False)
    
    elif Button.CENTER in pressed and Button.LEFT in pressed:
        driveAcross()
    
    elif Button.CENTER in pressed and Button.RIGHT in pressed:
        waterRun()
    
    elif Button.RIGHT in pressed:
        windmillRun()

    elif Button.LEFT in pressed:
        boxRun()
    
    elif Button.UP in pressed:
        handRun()
    
    elif Button.DOWN in pressed:
        batteryRun()

    
    
    