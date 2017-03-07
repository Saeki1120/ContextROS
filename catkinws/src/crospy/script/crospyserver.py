#!/usr/bin/env python

import rospy
from crospy import crosyncserver

rospy.init_node('croserver', anonymous=True)
crosyncserver()
