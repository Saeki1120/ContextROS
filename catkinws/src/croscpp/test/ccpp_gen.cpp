// should be generated from src
#include "ccpp1.h"

#include <map>
#include <string>

static std::string ccpp_layer;

// should be generated from decls of base methods
static std::map <std::string, int (CCpp1::*)(int, int)> calc_methods;

// should be generated from decls of base methods
int CCpp1::calc (int a, int b)
{
    return (this->*(calc_methods[ccpp_layer]))(a, b);
}

void CCpp_init ()
{
    ccpp_layer = "base";

    // should be generated from decls of base methods
    calc_methods["base"] = &CCpp1::calc_base;
    calc_methods["l1"] = &CCpp1::calc_l1;
}

void CCpp_activate(std::string _layer)
{
    ccpp_layer = _layer;
}

void CCpp_deactivate(std::string _layer)
{
    ccpp_layer = "base";
}

