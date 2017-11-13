# ContextROS C++
c++でContextROSを使用する方法

## レイヤ記述例．

レイヤ名で管理

```
#include <Library_name>
Layer Layer_name [
  //function  
  void greeting(int hour){
    std::cout << "おはよう" << std::endl;
  }
]
```

## アプリケーション 例

```
#include <ros/ros.h>
#include "layer.h"

int main(int argc, char **argv)
{
	ros::init(argc, argv, "greeting_node");
	ros::NodeHandle n;

	CROS cros;
	cros.init(n);

	ros::Rate loop_rate(1);
	while (ros::ok()) {
		/* code */
		greeting(0);
		ros::spinOnce();
		loop_rate.sleep();
	}

	return 0;
}

```

## 使い方
1. レイヤ記述(layer.cr)を用意する．
2. 以下のコマンドを実行し，layer.cppとlayer.hを生成する．

  ```
  pytohn parser.py layer.cr
  ```

3. アプリケーションと組み合わせて実行する.

ROSマスターの起動

'''
$ roscore
'''

greetingアプリケーションの実行

'''
$ rosrun croscpp greeting_node
'''

交互にレイヤを切り替えながら挨拶を表示する

## パッケージ構成
- ws
  - build
  - devel
  - src
    - croscpp
      - CMakeList.txt
      - package.xml
      - src
        - greeting
      - msg

## Issue
1. レイヤ記述にif, while文が記述できない
2. ノード内でのアクティベーションしか行えず, レイヤをpubしない
3. 単一のレイヤしか保持できない
