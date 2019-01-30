#!/usr/bin/python
# -*- coding: utf-8 -*-
# tfをサブスクライブして
# 位置情報から当たり判定を行う
# 判定したオブジェクト名をパブリッシュする
import sys
import rospy
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import DeleteModel
from std_srvs.srv import Trigger
from std_srvs.srv import TriggerResponse

class Model:
    """名前と位置をもつ"""
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z


# 後でクラスを使う時に使う予定
class Clean:
    """対象モデルの範囲内にあるオブジェクトを消去する"""
    def __init__(self, target=''):
        #rospy.loginfo("TurtleBot3 Clean Node Init")
        name = rospy.get_namespace()
        self.sub = rospy.Subscriber('/gazebo/model_states', ModelStates, self.update_location)


        self.target = target
        self.state = 'off'
        self.trashs = {}
        self.robots = {}
        self.flag = True

        self.switch_cleaner = rospy.Service('switch_cleaner', Trigger, self.switch)

        rospy.loginfo("Waiting for gazebo services...")
        #rospy.wait_for_service('gazebo/delete_model')
        #rospy.loginfo("Got it.")
        # self.sub = rospy.Subscriber('/gazebo/model_states', ModelStates, self.update_location)
        self.delete_trash = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)


        # 掃除したゴミの数をpubするといいかも？

        while self.flag:
            pass

        rospy.loginfo('Clean initialized')

    def update_location(self, model_states):
        # ロボットとゴミの位置を更新
        for i, name in enumerate(model_states.name):
            if 'trash' in name:
                x = model_states.pose[i].position.x
                y = model_states.pose[i].position.y
                z = model_states.pose[i].position.z
                self.trashs[name] = Model(name, x, y, z)
            if 'turtlebot3' in name:
                x = model_states.pose[i].position.x
                y = model_states.pose[i].position.y
                z = model_states.pose[i].position.z
                self.robots[name] = Model(name, x, y, z)
            else:
                pass

        # 最初の受信を判定
        if self.flag:
            self.flag = False

    def collision(self, model):
        # 当たり判定を行う
        result = False
        if (self.robots[self.target].x - model.x) ** 2 + (self.robots[self.target].y - model.y) ** 2 <= 0.1 ** 2:
            result = True
        return result

    def clean(self):
        # 掃除する
        if 'on' == self.state:
            for name, model in self.trashs.items():
                if self.collision(model):
                    rospy.loginfo("Detect")
                    self.delete_trash(name)
                    self.trashs.pop(name)
                    rospy.loginfo("%s deleted", name)
        elif 'off' == self.state:
            pass
        else:
            pass


    def switch(self, request):
        # 掃除状態を変更する
        if 'on' == self.state:
            self.state = 'off'
        elif 'off' == self.state:
            self.state = 'on'

        msg = "Now state " + self.state
        rospy.loginfo(msg)

        return TriggerResponse(success=True, message=self.state)


if __name__ == '__main__':
    # rospy.loginfo('OK')
    # 掃除する機体名を入力
    name = sys.argv[1]
    rospy.init_node('cleaner', anonymous=True)
    clean = Clean(name)
    #rospy.loginfo('Start')
    # ゴミがロボットの周囲(半径10cm)に存在したら消す
    # 10Hz
    rate = rospy.Rate(125)
    while not rospy.is_shutdown():
        clean.clean()
        rate.sleep()
