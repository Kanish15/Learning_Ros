#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def pub():
    rospy.init_node('pub')

    pub_details = rospy.Publisher('helloTopic', String, queue_size=10)

    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():

        msg = "Hey from the PUBLISHER!!"

        pub_details.publish(msg)

        rospy.loginfo(msg)

        rate.sleep()

if __name__=='__main__':
    pub()