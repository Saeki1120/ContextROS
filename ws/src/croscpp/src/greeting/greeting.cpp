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
		cros.activate("Tokyo");
		ros::spinOnce();
		loop_rate.sleep();
		greeting(0);
		cros.activate("London");
		ros::spinOnce();
		loop_rate.sleep();
	}

	return 0;
}
