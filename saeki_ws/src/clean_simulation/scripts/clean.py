#!/usr/bin/python
# -*- coding: utf-8 -*-
# tfをサブスクライブして
# 位置情報から当たり判定を行う
# 判定したオブジェクト名をパブリッシュする

import rospy
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import DeleteModel

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
    def __init__(self, name):
        rospy.loginfo("TurtleBot3 Clean Node Init")
        rospy.init_node('cleaner')
        self.sub = rospy.Subscriber('/gazebo/model_states', ModelStates, self.update_location)
        self.delete_trash = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
        self.target = name
        self.trashs = {}
        self.robots = {}
        self.flag = 'First'
        while self.flag == 'First':
            pass

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
        if self.flag == 'First':
            self.flag = 'Second'

    def collision(self, model):
        # 当たり判定を行う
        result = False
        if (self.robots[self.target].x - model.x) ** 2 + (self.robots[self.target].y - model.y) ** 2 <= 0.1 ** 2:
            result = True
        return result

    def clean(self):
        # 掃除する
        for name, model in self.trashs.items():
            if self.collision(model) == True:
                self.delete_trash(name)
                self.trashs.pop(name)
                rospy.loginfo("%s deleted", name)

    def on(self, arg):
        # 掃除を始める
        pass

    def off(self, arg):
        # 掃除をやめる
        pass


if __name__ == '__main__':
    print('OK')
    # 掃除する機体名を入力
    clean = Clean("turtlebot3_waffle")
    print('Start')
    # ゴミがロボットの周囲(半径10cm)に存在したら消す
    # 10Hz
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        clean.clean()
        rate.sleep()
