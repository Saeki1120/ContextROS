# How to build / run

## src/simple

```
source ./devel/setup.bash # if you are using bash
catkin_make
roscore # invoke master server
rosrun simple passive.py
rosrun simple active.py
```

## unit test
```
rosrun crospy test1.py
```

## TODO
- add reliable layer change feature (using service call?)
- share current layer state in a same program

