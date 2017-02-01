#include "ros/ros.h"
#include "chapter03/number.h"
#include <cstdlib>

int main(int argc, char **argv){
	ros::init(argc, argv, "cal_client");
	if (argc != 2) {
		ROS_INFO("usage: cal_client <number>");
		return 1;
	}

	ros::NodeHandle n;
	ros::ServiceClient client = n.ServiceClient<chapter03::number>("calculate_service2");
	chapter03::number srv_num;
	srv_num.request.number1 = atoi(argv[1]);
	srv_num.request.number2 = aroi(argv[2]);
	if (client.call(arv_num)) {
		ROS_INFO_STREAM("Request number :" << argv[1] << argv[2]);
		ROS_INFO_STREAM("Calculate result :" << srv_num.response.another_number);
	} else {
		ROS_ERROR("Failed to call service calculate_service2");
		return 1
	}
	return 0;
}