#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from math import pi
from turtlesim.srv import Spawn
from std_srvs.srv import Empty 

def move(publisher, distance):
    move_cmd = Twist()
    move_cmd.linear.x = distance
    publisher_2.publish(move_cmd)
    publisher.publish(move_cmd)
    rospy.sleep(3)

def rotate(publisher, angle):
    rotate_cmd = Twist()
    rotate_cmd.angular.z = angle
    publisher.publish(rotate_cmd)
    publisher.publish(rotate_cmd)
    rospy.sleep(3)

def k(publisher_2):
    rospy.loginfo("Starting the robot")
    rospy.sleep(1)
    rotate(publisher_2, pi / 2)
    move(publisher_2, 2)
    rotate(publisher_2, pi / 3)

def call_reset():
    rospy.wait_for_service('/reset')
    try:
        reset = rospy.ServiceProxy('/reset', Empty)
        reset()
        rospy.loginfo("Reset successful.")
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", str(e))

if __name__ == '__main__':
    rospy.init_node('Shapes')
    rospy.wait_for_service('/spawn')
    try:
        new = rospy.ServiceProxy('/spawn', Spawn)
        new(1.0, 1.0, 0.0, 'turtle2')
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", str(e))
    
    rospy.loginfo("Welcome Sir")
    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    publisher_2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    k( publisher_2)  
