#include <ros/ros.h>
#include <std_msgs/String.h>
#include <chapter03/Layer.h>
#include <chapter03/activate.h>

chapter03::Layer l_name;
//ros::Publisher pub;
int service_counter = 0;
void conCallback(const ros::SingleSubscriberPublisher& pub)
{
	ROS_INFO_STREAM("topic has subscribed by node " << pub.getSubscriberName());
}

void disconCallback(const ros::SingleSubscriberPublisher& pub)
{
	ROS_INFO_STREAM("subscriber [" <<  pub.getSubscriberName() << "] disconect");
}

bool change(chapter03::activate::Request &req,
	chapter03::activate::Response &res)
{	
	//トピックの変更
	l_name.layer_name = req.layer_name;
	//サービスの返り値を設定
	res.active_layer_name = req.layer_name;
	//トピック配布 ←しない
	//pub.publish(l_name);
	service_counter++;
	//レイヤの変更を表示
	ROS_INFO_STREAM("request from client: (a layer name) " 
						<< req.layer_name);
	ROS_INFO_STREAM("sending back response: (active layer name) "
						<< res.active_layer_name);
	return true;
}


int main (int argc, char **argv)
{
	ros::init(argc, argv, "layer_controler2");
	ros::NodeHandle n;
	ros::Publisher pub = n.advertise<chapter03::Layer>("active_layer", 1000, conCallback, disconCallback);
	ros::ServiceServer service = n.advertiseService("layer_change", change);
	while(ros::ok()){	
		ros::spinOnce();		//サービスが呼ばれる時にコールバック関数を実行
		if(service_counter == 1){
			pub.publish(l_name);
			service_counter = 0;
		} else {
			service_counter = 0;
		}
	}
	return 0;
}






