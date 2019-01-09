#include "cros.h"

std::string CROS::layer;
ros::Subscriber CROS::sub;
ros::Publisher CROS::pub;

void CROS::init(ros::NodeHandle n)
{
  //レイヤ情報の購読登録
  sub = n.subscribe("active_layer", 1000, CROS::layerMessageCallback);
  //レイヤ情報の配布登録
  pub = n.advertise<croscpp::layer_msgType>("active_layer", 1000);
  //初期レイヤの登録
  change_layer("base");
}

//レイヤメッセージを受け取った際の処理
void CROS::layerMessageCallback(const croscpp::layer_msgType::ConstPtr& msg)
{
  change_layer(msg->name);
	ROS_INFO_STREAM("layer changed");
}


//アクティベート
void CROS::activate(std::string _layer)
{
    //localなレイヤを更新
    change_layer(_layer);

    //更新されたレイヤの配布
    croscpp::layer_msgType msg;
    msg.name = _layer;
    pub.publish(msg);
}

//ディアクティベート
void CROS::deactivate(std::string _layer)
{
    //localなレイヤを更新
    change_layer("base");

    //更新されたレイヤの配布
    croscpp::layer_msgType msg;
    msg.name = "base";
    pub.publish(msg);
}

//localなレイヤの更新
void CROS::change_layer(std::string _layer)
{
    layer = _layer;
}

std::string CROS::now_layer(){
  return layer;
}
