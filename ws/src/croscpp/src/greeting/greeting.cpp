#include <ros/ros.h>
#include "layer.h"

int main(int argc, char **argv)
{
	ros::init(argc, argv, "greeting_node");
	ros::NodeHandle n;

	CROS cros;
	cros.init(n);

	cros.activate("Tokyo");

	ros::Rate loop_rate(1);
	while (ros::ok()) {
		//cros.activate("Tokyo");
		greeting(0);
		/*
		loop_rate.sleep();
		cros.activate("London");
		greeting(0);
		*/
		loop_rate.sleep();
		ros::spinOnce();
	}

	return 0;
}
