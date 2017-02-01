#include <ros/ros.h>
#include <std_msgs/String.h>
#include <chapter03/Layer.h>
#include <chapter03/number.h>
#include "layer.h"

//現在のレイヤを保持
chapter03::Layer l_name;

//calculateサービスが呼ばれた時に呼び出される関数
bool calculate(chapter03::number::Request &req,
				chapter03::number::Response &res)
{
	//#################################################
	res.another_number = cal((long int)req.number1, (long int)req.number2, (int)l_name.layer_name);
	//#################################################

	ROS_INFO_STREAM("request from client: (number1, number2) " 
		<< (long int)req.number1 << ", " <<(long int)req.number2);
	ROS_INFO_STREAM("sending back response: (sum) "
		<< res.another_number);
	return true;
}

//レイヤが変更された時に呼ばれる関数
void messageCallback(const chapter03::Layer::ConstPtr& msg)
{
	l_name.layer_name = msg->layer_name;
	ROS_INFO_STREAM("I activate [" <<  msg->layer_name << "] layer");
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "calculate_server2");
	ros::NodeHandle n;
	//rosに購読者として登録
	ros::Subscriber sub = n.subscribe("active_layer", 1000, messageCallback);
	//rosにサービスを登録
	ros::ServiceServer service = n.advertiseService("calculate_service2", calculate);
	//コールバック関数を呼び出す無限ループ
	ros::spin();
	return 0;
}
