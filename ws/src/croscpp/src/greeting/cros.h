#ifndef __CROS_H
#define __CROS_H

#include <ros/ros.h>
#include <croscpp/layer_msgType.h>

class CROS
{
private:
  ros::Subscriber sub;
  static std::string layer;

public:
  void init(ros::NodeHandle n);
  static void layerMessageCallback(const croscpp::layer_msgType::ConstPtr& msg);
  static void activate(std::string _layer);
  static void deactivate(std::string _layer);
  std::string now_layer();
};



#endif /* __CROS_H */
