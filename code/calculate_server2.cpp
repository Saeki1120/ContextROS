#include <ros/ros.h>
#include <std_msgs/String.h>
#include <chapter03/Layer.h>
#include <chapter03/number.h>

//現在のレイヤを保持
chapter03::Layer l_name;

//#################################################
//レイヤindoorでの振る舞い
long int sum(long int val1, long int val2)
{
	long int val;
	val = val1 + val2;
	return val;
}

//レイヤoutdoorでの振る舞い
long int diff(long int val1, long int val2)
{
	long int val;
	val = val1 - val2;
	return val;
}
//#################################################

//calculateサービスが呼ばれた時に呼び出される関数
bool calculate(chapter03::number::Request &req,
				chapter03::number::Response &res)
{
	//#################################################
	if (l_name.layer_name == "indoor") {
		res.another_number = sum((long int)req.number1, (long int)req.number2);			//indoor振る舞い
	} else if (l_name.layer_name == "outdoor") {
		res.another_number = diff((long int)req.number1, (long int)req.number2);		//outdoor振る舞い
	}
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

	//レイヤコントロール部に問い合わせるほうがいいのかな？？
	l_name.layer_name = "indoor";		//set_layer()
	
	//rosに購読者として登録
	ros::Subscriber sub = n.subscribe("active_layer", 1000, messageCallback);

	//rosにサービスを登録
	ros::ServiceServer service = n.advertiseService("calculate_service2", calculate);

	//コールバック関数を呼び出す無限ループ
	ros::spin();
	return 0;
}
