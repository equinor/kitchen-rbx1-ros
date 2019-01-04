#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray
from rbx1_slush.srv import *

def get_robot_status():
    rospy.wait_for_service('get_status')
    try:
        get_status = rospy.ServiceProxy('get_status', RobotStatus)
        resp1 = get_status()
        return resp1.status
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def joint_state_publisher():
    rospy.init_node('joint_state_publisher')
    pub=rospy.Publisher('joint_states', JointState, queue_size=10)
    rate= rospy.Rate(20)

    while not rospy.is_shutdown():
        msg=JointState()
        msg.header.stamp = rospy.Time.now()
        msg.name = ['gripper_idol_gear_joint', 'gripper_servo_gear_joint',
         'joint_1_base_shoulder', 'joint_2_shoulder_arm', 'joint_3_arm_upper_forearm', 
         'joint_4_upper_forearm_forearm', 'joint_5_forearm_wrist', 'joint_6_wrist_hand']
        msg.position = get_robot_status()
        msg.effort = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        msg.velocity = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__=='__main__':
    try:
        joint_state_publisher()
    except rospy.ROSInterruptException:
        pass