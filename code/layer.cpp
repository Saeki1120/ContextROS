 #include "layer.h"
 long int cal_indoor(long int val1 , long int val2){
 long int val;
                val = val1 + val2;
                return val;
        }
string connect_indoor(string name1 , string name2){
 string name;
                name = name1 + name2;
                return name;
        }
int hoge_indoor(int name1 , int name2){
 int name;
                name = name1 + name2;
                return name;
        }
long int cal_outdoor(long int val1 , long int val2){
 long int val;
                val = val1 - val2;
                return val;
        }
string connect_outdoor(string name1 , string name2){
 string name;
                name = name2 + name1;
                return name;
        }
int hoge_outdoor(int name1 , int name2){
 int name;
                name = name1 + name2;
                return name;
        }
long int cal(long int val1 , long int val2,int layer_name){
if (layer_name == 0) {return cal_indoor(val1,val2);}
else if (layer_name == 1){return cal_outdoor(val1,val2);}
}
string connect(string name1 , string name2,int layer_name){
if (layer_name == 0) {return connect_indoor(name1,name2);}
else if (layer_name == 1){return connect_outdoor(name1,name2);}
}
int hoge(int name1 , int name2,int layer_name){
if (layer_name == 0) {return hoge_indoor(name1,name2);}
else if (layer_name == 1){return hoge_outdoor(name1,name2);}
}
