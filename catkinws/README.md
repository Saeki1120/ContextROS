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
source ./devel/setup.bash # if you are using bash
catkin_make
rosrun crospy crospyserver.py
rosrun crospy test1.py
```

## TODO
- share current layer state in a same program
- automatically unsubscribe services at the end of the node

## DONE
- add reliable layer change feature (using service call?)
