# ContextROS
ContextROSはRobot Operating System(ROS)上でContext-oriented Programingを取り入れたフレームワークである。

# saeki_ws
## clean_simulation
gazeboシミュレータ上でturtlebotを動かしゴミオブジェクトと重なるとゴミオブジェクトを消去する。turtlebotはキーボードで操作する．

### 使い方
1. turtlebot3_gazeboのインストール

```
$ sudo apt-get install ros-kinetic-joy ros-kinetic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-kinetic-rosserial-server ros-kinetic-rosserial-client ros-kinetic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation ros-kinetic-interactive-markers

$ cd ~/catkin_ws/src/
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
$ cd ~/catkin_ws && catkin_make
```

2. 使用モデルの選択

```
# とりあえずwaffleを使用する
$ export TURTLEBOT3_MODEL=waffle
```

3. ワールドの起動  
亀をモチーフにしたワールド上にロボットと非常に小さいゴミオブジェクトがロボットの前方に生成される。

```
roslaunch clean_simulation turtlebot3_world.launch
```

4. 掃除の起動

```
rosrun clean_simulation clean.py
```

5. キー操作の起動

```
rosrun turtlebot3_teleop turtlebot3_teleop_key
```
