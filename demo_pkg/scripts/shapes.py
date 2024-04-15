#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from math import pi
from std_srvs.srv import Empty 

def move(publisher, distance):
    move_cmd = Twist()
    move_cmd.linear.x = distance
    publisher.publish(move_cmd)
    rospy.sleep(3)

def rotate(publisher, angle):
    rotate_cmd = Twist()
    rotate_cmd.angular.z = angle
    publisher.publish(rotate_cmd)
    rospy.sleep(3)

def draw_rectangle(publisher):
    rospy.loginfo("Robot is moving.......")
    move(publisher, 3.0)
    rotate(publisher, pi / 2)
    move(publisher, 2.0)
    rotate(publisher, pi / 2)
    move(publisher, 3.0)
    rotate(publisher, pi / 2)
    move(publisher, 2.0)
    rospy.sleep(10)
    print("Resetting the robot")    
    call_reset()

def draw_triangle(publisher):
    rospy.loginfo("Robot is moving.......")
    move(publisher, 2.0)
    rotate(publisher, 2 * pi / 3)
    move(publisher, 2.0)
    rotate(publisher, 2 * pi / 3)
    move(publisher, 2.0)
    rotate(publisher, 2 * pi / 3)
    rospy.sleep(10)
    print("Resetting the robot")                                                                    
    call_reset()


def draw_square(publisher):
    rospy.loginfo("Robot is moving.......")
    for _ in range(4):
        move(publisher, 2.0)
        rospy.sleep(2)
        rotate(publisher, pi / 2)
        rospy.sleep(2)
        rospy.sleep(10)
    print("Resetting the robot")
    call_reset()

def draw_star(publisher):
    for _ in range(5):
        move(publisher, 1.0)
        rotate(publisher, 4 * pi / 5)
        move(publisher, 1.0)
        rotate(publisher, -2 * pi / 5)
        rospy.loginfo("Robot is moving.......")
        rospy.sleep(10)
    print("Resetting the robot")
    call_reset()

def call_reset():
    rospy.wait_for_service('/reset')
    try:
        reset = rospy.ServiceProxy('/reset', Empty)
        reset()
        rospy.loginfo("Reset successful.")
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", str(e))

def main():
    rospy.init_node('Shapes')
    rospy.loginfo("Welcome Sir")
    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        print("Shapes that can be navigated")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Star")

        print("Enter the shape:")
        shape = input()

        if shape == "Square":
            draw_square(publisher)
            call_reset()
            rospy.sleep(2)
        elif shape == "Rectangle":
            draw_rectangle(publisher)
            rospy.sleep(3)
        elif shape == "Triangle":
            draw_triangle(publisher)
            rospy.sleep(3)
        elif shape == "Star":
            draw_star(publisher)
            rospy.sleep(3)
        else:
            print("Error !!")
            exit()

if __name__ == '__main__':
    main()
