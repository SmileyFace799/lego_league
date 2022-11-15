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

#crane.run_time(-1000,1000)

#using temporary values
def windmillRun():
    robot.straight(500)
    robot.straight(-230)
    robot.turn(-53) #45
    robot.straight(500)
    robot.turn(95) #90
    robot.straight(400)
    robot.straight(-150)
    robot.straight(400)
    robot.straight(-150)
    robot.straight(400)
    robot.straight(-150)
    robot.turn(-70)
    robot.straight(-600)

def car():
    robot.straight(850)
    crane.run_angle(500, -1800, wait=True)
    crane.run_angle(500, 1800, wait=True)
    robot.straight(-850)

while True:
    pressed = ev3.buttons.pressed()
    if Button.RIGHT in pressed:
        windmillRun()

    elif Button.LEFT in pressed:
        car()
    
    elif Button.UP in pressed:
        crane.run_angle(1000, -5, wait=False)
    
    elif Button.DOWN in pressed:
        crane.run_angle(1000, 5, wait=False)
    