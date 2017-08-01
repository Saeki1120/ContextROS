#include <iostream>
#include "ccpp.h"
#include "ccpp1.h"

// in source code we want to describe as follows:
//
// @Layer(base) {
//     int CCpp1::calc (int a, int b)
//     {
//         return a + b;
//     }
// }

// @Layer(l1) {
//     int CCpp1::calc (int a, int b)
//     {
//         return a * b;
//     }
// }

// and cocdes should be generated as follows:

int CCpp1::calc_base (int a, int b)
{
    return a + b;
}

int CCpp1::calc_l1 (int a, int b)
{
    return a * b;
}

int main ()
{
    CCpp_init ();

    CCpp1 o;
    std::cout << o.calc (10, 20) << std::endl;

    CCpp_activate("l1");
    std::cout << o.calc (10, 20) << std::endl;

    return 0;    
}