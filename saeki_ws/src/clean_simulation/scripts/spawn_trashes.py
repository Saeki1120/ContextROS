#!/usr/bin/python
# -*- coding: utf-8 -*-

# ある範囲にランダムに複数のゴミを生成する
# spawnサービスを複数回実行するスクリプトを作る
# これ一つで全ての部屋のオブジェクトを生成する
# → このスクリプトを複数実行すると同名オブジェクトを生成し問題になる
import random
import rospy, tf
from gazebo_msgs.srv import DeleteModel, SpawnModel
from geometry_msgs.msg import *

from clean_simulation.srv import SpawnTrash
from clean_simulation.srv import SpawnTrashResponse

class TrashSpawner:
    """ゴミ生成器"""
    # 正直これもサーバーにして常に生成できるようにしたい
    def __init__(self):
        print("Waiting for gazebo services...")
        #rospy.init_node('trash_spaener')
        rospy.wait_for_service('gazebo/delete_model')
        rospy.wait_for_service('gazebo/spawn_urdf_model')
        print("Got it.")

        self.spawn_trash = rospy.ServiceProxy('gazebo/spawn_urdf_model', SpawnModel)
        self.delete_trash = rospy.ServiceProxy("gazebo/delete_model", DeleteModel)
        self.spawn_srv = rospy.Service('spawn_trash', SpawnTrash, self.switch)


        # パスを考えないとなぁ
        with open("/media/sf_VirtualUbuntu1604/catkin_ws/src/clean_simulation/urdf/trash_object.urdf.xacro", "r") as f:
            self.product_xml = f.read()

        q = tf.transformations.quaternion_from_euler(0,0,0)
        self.orient = Quaternion(q[0], q[1], q[2], q[3])

        # 部屋の大きさ
        # self.romm_size = {0:[(7, -1), (5, -5)], 1: [(7, 5), (2.5, 0)], 2:[(2, 5), (0.1, 1.1)], 3:[(-0.2, 5), (-5, 0)], 4:[(-5.2, 5), (-7.3, 1)], 5:[(-5.2, 0), (-7.3, -3.7)]}
        # self.trash_num = 0

        self.spawn_trashes(0,0)

    # def spawn_trashe(self, arg):
    #     pass

    def spawn_trashes(self, x, y):
        # 同名のオブジェクトが生成されるとしんどいなぁ
        # とりあえず生成予定の名前のオブジェクトを削除する
        for num in xrange(0,10):
            trash_name = "trash_{0}_0".format(num)
            print("Deleting model:%s", trash_name)
            self.delete_trash(trash_name)

        for num in xrange(0,10):
            trash_y   = x + random.uniform(-0.5, 0.5)
            trash_x   = y + random.uniform(-0.5, 0.5)
            trash_name   =   "trash_{0}_0".format(num)
            print("Spawning model:%s", trash_name)
            trash_pose   =   Pose(Point(x=trash_x, y=trash_y, z=0),   self.orient)
            self.spawn_trash(trash_name, self.product_xml, "", trash_pose, "world")

    def switch(self, request):
        # ゴミを生成する
        # 中心位置が欲しい
        self.spawn_trashes(request.x, request.y)
        rospy.loginfo('Trash was spawned')

        return TriggerResponse(success=True, message='Trash was spawned')

if __name__ == '__main__':
    rospy.init_node('spawner', anonymous=True)
    rospy.loginfo("spawner start")
    spawner = TrashSpawner()
    rate = rospy.Rate(125)
    while not rospy.is_shutdown():
        rate.sleep()
