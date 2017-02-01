#include <ros/ros.h>
#include <std_msgs/String.h>
#include <chapter03/activate.h>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "sample_client");
	ros::NodeHandle n;
	ros::ServiceClient client = n.serviceClient<chapter03::activate>("layer_change");
	chapter03::activate act;	

	int i = 0;	

	ros::Rate loop_rate(0.05);
	while(ros::ok()) {
		if (i % 2 == 0) {
			act.request.layer_name = 0;
		} else {
			act.request.layer_name = 1;
		}
		
		if (client.call(act)) {
			ROS_INFO_STREAM("A requested layer " << act.request.layer_name
				<< "was activated completely");
			ROS_INFO_STREAM("Now activated layer is " <<  act.response.active_layer_name);
		} else {
			ROS_ERROR("Failed to call service layer_cahnge");
		}

		if (i >= 9){
			i = 0;
		} else {
			i++;
		}		
		loop_rate.sleep();
	}

	return 0;
}
