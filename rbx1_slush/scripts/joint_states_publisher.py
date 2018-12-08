#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray

from rbx1 import RobotSingleton

def joint_state_publisher():
    rospy.init_node('joint_state_publisher')
    pub=rospy.Publisher('joint_states', JointState, queue_size=10)
    rate= rospy.Rate(30)
    robot = RobotSingleton.getInstance()

    while not rospy.is_shutdown():
        msg=JointState()
        msg.header.stamp = rospy.Time.now()
        status = robot.getStatus()
        msg.position = status['currentPos']
        msg.effort = [0, 0, 0, 0, 0, 0]
        msg.velocity = [0, 0, 0, 0, 0, 0]
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__=='__main__':
    try:
        joint_state_publisher()
        joint_command_subscriber()
    except rospy.ROSInterruptException:
        pass