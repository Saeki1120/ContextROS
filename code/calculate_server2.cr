#include <ros/ros.h>
#include <std_msgs/String.h>
#include <chapter03/Layer.h>
#include <chapter03/number.h>


Layer indoor {
	long int cal(long int val1, long int val2)
	{
		long int val;
		val = val1 + val2;
		return val;
	}
}

Layer outdoor {
	long int cal(long int val1, long int val2)
	{
		long int val;
		val = val1 - val2;
		return val;
	}
}

bool calculate(chapter03::number::Request &req,
				chapter03::number::Response &res)
{
	//*******************
	res.another_number = cal((long int)req.number1, (long int)req.number2);			//行いたい振る舞い
	//*******************
	ROS_INFO_STREAM("request from client: (number1, number2) " 
						<< (long int)req.number1 << ", " <<(long int)req.number2);
	ROS_INFO_STREAM("sending back response: (sum) "
						<< res.another_number);
	return true;
}


void messageCallback(const chapter03::Layer::ConstPtr& msg)
{
	//*******************
	set_layer(msg->layer_name);
	//*******************
	ROS_INFO_STREAM("I activate [" <<  msg->layer_name << "] layer");
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "calculate_server2");
	ros::NodeHandle n;
	//*******************
	set_layer("indoor");
	//*******************
	ros::Subscriber sub = n.subscribe("active_layer", 1000, messageCallback);
	ros::ServiceServer service = n.advertiseService("calculate_service2", calculate);
	ros::spin();
	return 0;
}