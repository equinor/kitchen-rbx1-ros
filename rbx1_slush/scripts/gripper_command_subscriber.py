#!/usr/bin/env python

import rospy

from std_msgs.msg import Float64MultiArray
from rbx1 import RobotSingleton

def callback(data):
    robot = RobotSingleton.getInstance()
    robot.runGripper(data.data)
    rospy.loginfo("I receive %s", data.data)

def gripper_command_subscriber():
    rospy.init_node('gripper_command_subscriber')
    rospy.Subscriber('/rbx1_gripper_controller/command', Float64MultiArray, callback)
    rospy.spin()

if __name__=='__main__':
    gripper_command_subscriber()