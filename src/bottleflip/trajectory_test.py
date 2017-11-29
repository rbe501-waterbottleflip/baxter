#!/usr/bin/python2

import rospy
import baxter_interface

from baxter_interface import CHECK_VERSION
from baxter_interface import Gripper

global right_gripper

if __name__ == '__main__':
	rospy.init_node('griptest')
	
	global right_gripper

	rospy.sleep(rospy.Duration(5,0))

	rs = baxter_interface.RobotEnable(CHECK_VERSION)
	rs.enable()

	right_gripper = Gripper('right');

	right_gripper.calibrate()
	
	print "closing gripper"
	right_gripper.close()

	rospy.sleep(rospy.Duration(5,0))
	print "opening gripper"
	right_gripper.open()

	
