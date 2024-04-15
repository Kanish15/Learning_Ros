#!/usr/bin/env python3

import rospy
from std_msgs.msg  import String

def node1():
    rospy.init_node('Node_1')

    rospy.loginfo("NODE INTIALIZING.... ")

    node = rospy.Publisher('Topic_1', String, queue_size = 10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
       
     msg = "NODE 1 IS SENDING THE DATA ON TOPIC 1!!!!"
     
     node.publish(msg)

     rospy.loginfo(msg)

     rate.sleep()

if __name__== '__main__':
 node1()
