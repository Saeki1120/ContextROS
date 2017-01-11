#include <ros/ros.h>
#include <std_msgs/String.h>
#include <chapter03/Layer.h>
#include <chapter03/name.h>
#include <string>
#include "layer.h"

chapter03::Layer l_name;

using namespace std;

bool connect(chapter03::name::Request &req,
				chapter03::name::Response &res)
{
	res.another_name = connect(req.name1, req.name2, l_name.layer_name);
	ROS_INFO_STREAM("request from client: (name1, name2) " 
						<< req.name1 << ", " << req.name2);
	ROS_INFO_STREAM("sending back response: (connect1) "
						<< res.another_name);
	return true;
}

void messageCallback(const chapter03::Layer::ConstPtr& msg)
{
	l_name.layer_name = msg->layer_name;
	ROS_INFO_STREAM("I activate [" <<  msg->layer_name << "] layer");
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "write_server2");
	ros::NodeHandle n;
	l_name.layer_name = 0;
	ros::Subscriber sub = n.subscribe("active_layer", 1000, messageCallback);
	ros::ServiceServer service = n.advertiseService("write_service2", connect);
	ros::spin();
	return 0;
}
