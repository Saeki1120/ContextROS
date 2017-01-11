#ifndef _chapter03_layer_H_
#define _chapter03_layer_H_
#include <string>

using namespace std;

long int cal_indoor(long int val1, long int val2);

string connect_indoor(string name1, string name2);

long int cal_outdoor(long int val1, long int val2);

string connect_outdoor(string name1, string name2);

long int cal(long int val1, long int val2, int layer_name);

string connect(string name1, string name2, int layer_name);

#endif
