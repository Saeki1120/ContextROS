#include "ros/ros.h"
#include "chapter03/number.h"
#include <cstdlib>
#include <iostream>

int main(int argc, char **argv){
	ros::init(argc, argv, "cal_client");
	//if (argc != 3) {
	//	ROS_INFO("usage: cal_client <number>");
	//	return 1;
	//}
	
	ros::NodeHandle n;
	ros::ServiceClient client = n.serviceClient<chapter03::number>("calculate_service2");
	chapter03::number srv_num;
	int num1;
	int num2;
	while (ros::ok()) {
		std::cout << "整数を２つ入力してください\n";	
		std::cin >> num1;		
		std::cin >> num2;
		//srv_num.request.number1 = atoi(argv[1]);
		//srv_num.request.number2 = atoi(argv[2]);
		srv_num.request.number1 = num1;
		srv_num.request.number2 = num2;
		if (client.call(srv_num)) {
			ROS_INFO_STREAM("Request number :" << argv[1] << ", "<< argv[2]);
			ROS_INFO_STREAM("Calculate result :" << srv_num.response.another_number);
		} else {
			ROS_ERROR("Failed to call service calculate_service2");
			return 1;
		}
	}
	
	return 0;
}
