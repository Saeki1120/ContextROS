 #include "layer.h"
 void greeting_Tokyo(int time){
 std::cout << "おはよう" << std::endl;
        }
void greeting_London(int time){
 std::cout << "Good morning" << std::endl;
        }
void greeting(int time){
CROS cros;
if (cros.now_layer() == "Tokyo") {return greeting_Tokyo(time);}
else if (cros.now_layer() == "London"){return greeting_London(time);}
}
