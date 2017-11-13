#include "cros.h"

std::string CROS::layer;

void CROS::init(ros::NodeHandle n)
{
  //レイヤ情報の購読登録
  sub = n.subscribe("active_layer", 1000, CROS::layerMessageCallback);
  //初期レイヤの登録
  activate("base");
}

//レイヤメッセージを受け取った際の処理
void CROS::layerMessageCallback(const croscpp::layer_msgType::ConstPtr& msg)
{
	activate(msg->name);
	ROS_INFO_STREAM("layer changed");
}


//アクティベート
void CROS::activate(std::string _layer)
{
    layer = _layer;
}

//ディアクティベート
void CROS::deactivate(std::string _layer)
{
    layer = "base";
}

std::string CROS::now_layer(){
  return layer;
}
