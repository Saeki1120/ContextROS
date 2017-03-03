 #include "layer.h"
 long int cal_sum(long int val1 , long int val2){
 long int val;
                val = val1 + val2;
                return val;
        }
long int cal_diff(long int val1 , long int val2){
 long int val;
                val = val1 - val2;
                return val;
        }
long int cal_prod(long int val1 , long int val2){
 long int val;
                val = val1 * val2;
                return val;
        }
long int cal(long int val1 , long int val2,int layer_name){
if (layer_name == 0) {return cal_sum(val1,val2);}
else if (layer_name == 1){return cal_diff(val1,val2);}
else if (layer_name == 2){return cal_prod(val1,val2);}
}
