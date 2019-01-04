#!/usr/bin/env python

import rospy

from std_msgs.msg import Float64MultiArray
from rbx1_slush.srv import *

def move_gripper(pos):
    rospy.wait_for_service('move_gripper')
    try:
        move_gripper = rospy.ServiceProxy('move_gripper', RobotGripper)
        move_gripper(pos)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def callback(data):
    move_gripper(data.data[0])
    rospy.loginfo("I receive %s", data.data)

def gripper_command_subscriber():
    rospy.init_node('gripper_command_subscriber')
    rospy.Subscriber('/rbx1_gripper_controller/command', Float64MultiArray, callback)
    rospy.spin()

if __name__=='__main__':
    gripper_command_subscriber()