#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

from geometry_msgs.msg import Twist

from std_srvs.srv import Trigger

#from clean_msgs.srv import Clean

# from auto_drive import AutoDrive
# from drive_msgs.msg import Drive
# ? ROSだとAutoDriveにメッセージを投げるのでは
# クラス間の関係に対応するのがROSだとメッセージになるのでは？
# クラス = ノードをある程度意識していこうかな
# → auto_driveにセンサーが必要なんだよなぁ
# 後で余裕があったら分散的にも書きましょう


class CleanRobo:
    def __init__(self, name=''):
        name = rospy.get_namespace()
        self.name = name
        self.state = 'hoge'

        self.scan_data = [0.0, 0.0, 0.0]
        self.pose = 0.0
        self.prev_pose = 0.0

        # sub(センサー)を登録
        # 複数のロボットのトピック名に関しては後で調べましょう

        # laser subscribe
        self.laser_scan_sub  = rospy.Subscriber("scan", LaserScan, self.laser_scan_msg_callback)

        # odom subscribe
        self.odom_sub = rospy.Subscriber("odom", Odometry, self.odom_msg_callback)

        # バンパー？

        self.drive_manager = AutoDrive(name)
        self.cleaner = Cleaner(name)

        # 常に掃除 on
        self.cleaner.on()

        # self.count = 0
        rospy.loginfo('CleanRobo initialized')

    def control_loop(self):
        # self.count += 1
        if '' == self.state:
            pass
        elif '' == self.state:
            pass
        else:
            self.drive_manager.auto_drive(self.scan_data, self.pose)

    # def talk(self):
    #     pass


    # call back func
    def laser_scan_msg_callback(self, data):
        scan_angle = [0, 30, 330]
        for i, angle in enumerate(scan_angle):
            if math.isinf(data.ranges[angle]):
                self.scan_data[i] = data.range_max
            else:
                self.scan_data[i] = data.ranges[angle]

    def odom_msg_callback(self, data):
        siny = 2.0 * (data.pose.pose.orientation.w * data.pose.pose.orientation.z + data.pose.pose.orientation.x * data.pose.pose.orientation.y)
    	cosy = 1.0 - 2.0 * (data.pose.pose.orientation.y * data.pose.pose.orientation.y + data.pose.pose.orientation.z * data.pose.pose.orientation.z)

        self.pose = math.atan2(siny, cosy)


class AutoDrive:
    def __init__(self, name=''):
        self.state = 'get_direction'
        self.prev_pose = 0.0

        self.escape_range      = math.radians(30.0)
        self.check_forward_dist = 0.7;
        self.check_side_dist    = 0.6;

        # cmd pub
        cmd_vel_topic = name + 'cmd_vel'
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    def auto_drive(self, scan_data, pose):
        if 'get_direction' == self.state:
            # center : 0
            # left : 1
            # right : 2
            if scan_data[0] > self.check_forward_dist:
                if scan_data[1] < self.check_side_dist:
                    self.prev_pose = pose
                    self.state = 'right_turn'
                elif scan_data[2] < self.check_side_dist:
                    self.prev_pose = pose
                    self.state = 'left_turn'
                else:
                    # バリエーション
                    # if (/* condition 早く直進*/) {
                    # # /* code */
                    # } else if (/* condition 遅く直進*/) {
                    # # /* code */
                    # }
                    self.state = 'forward'

            if scan_data[0] < self.check_forward_dist:
                self.prev_pose = pose
                self.state = 'right_turn'
        elif 'forward' == self.state:
            self.update_velocity(0.3, 0.0)
            self.state = 'get_direction'
        elif 'right_turn' == self.state:
            if math.fabs(self.prev_pose - pose) >= self.escape_range:
                self.state = 'get_direction'
            else:
                self.update_velocity(0.0, -1 * 1.5)
        elif 'left_turn' == self.state:
            if math.fabs(self.prev_pose - pose) >= self.escape_range:
                self.state = 'get_direction'
            else:
                self.update_velocity(0.0, 1.5)
        else:
            self.state = 'get_direction'

        return True

    def update_velocity(self, linear, angular):
        cmd_vel = Twist()
        cmd_vel.linear.x  = linear
        cmd_vel.angular.z = angular

        self.cmd_vel_pub.publish(cmd_vel)


class Cleaner:
    def __init__(self, name=''):
        #cmd_vel_topic = name + '/cmd_vel'
        # clean service
        rospy.loginfo('waiting clean service')
        rospy.wait_for_service('switch_cleaner')

        self.switch = rospy.ServiceProxy('switch_cleaner', Trigger)
        rospy.loginfo('Cleaner initialized')

    def on(self):
        # while self.switch().message == 'off':
        #     pass
        res = 'off'
        while res == 'off':
            try:
                res = self.switch().message
            except rospy.ServiceException, e:
                rospy.logerr('Service call failed: %s', e)


    def off(self):
        # while self.switch().message == 'on':
        #     pass
        res = 'on'
        while res == 'on':
            try:
                res = self.switch().message
            except rospy.ServiceException, e:
                rospy.logerr('Service call failed: %s', e)





if __name__ == '__main__':
    rospy.init_node('clean_robo', anonymous=True)
    clean_robo = CleanRobo()

    rate = rospy.Rate(125)
    while not rospy.is_shutdown():
        clean_robo.control_loop()
        rate.sleep()
