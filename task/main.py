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
robot.settings(1000, 500, 150, 1000)

#crane.run_time(-1000,1000)

#using temporary values
def windmillRun():
    robot.straight(280)
    robot.straight(-200)
    robot.turn(-36) #45
    robot.straight(480)
    robot.turn(65) #90
    robot.straight(400)
    robot.straight(-150)
    robot.straight(400)
    robot.straight(-150)
    robot.straight(400)
    robot.straight(-150)
    robot.turn(-65)
    robot.straight(-600)

def batteryRun():
    robot.straight(380)
    robot.turn(-47)
    robot.straight(160)
    crane.run_angle(500, 720, wait=True)

def driveStraight():
    robot.straight(2000)

def handRun():
    crane.run_angle(500, -810, wait=False)
    robot.straight(800)
    robot.turn(-75)
    robot.straight(540) #reached the hand
    crane.run_angle(500,990, wait=True) #crane goes down
    robot.straight(-100) #pulled lever back
    crane.run_angle(500,-990, wait=True)
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



while True:
    pressed = ev3.buttons.pressed()
    
    if Button.CENTER in pressed and Button.UP in pressed:
        crane.run_angle(1000, -5, wait=False)
    
    elif Button.CENTER in pressed and Button.DOWN in pressed:
        crane.run_angle(1000, 5, wait=False)
    
    elif Button.CENTER in pressed and Button.LEFT in pressed:
        driveStraight()
    
    elif Button.RIGHT in pressed:
        windmillRun()

    elif Button.LEFT in pressed:
        batteryRun()
    
    elif Button.UP in pressed:
        handRun()

    
    
    