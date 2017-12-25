//=================================================================================
// Name        : help_functions.h
// Version     : 2.0.0
// Copyright   : Udacity
//=================================================================================

#include <iostream>
#include "help_functions.h"

//TODO: assign a value, the difference in distances between x_t and x_{t-1}
//that maximizes the returned probability of norm_pdf

float value = 2;//YOUR VALUE HERE


float parameter = 1.0; //set as control parameter or observation measurement
float stdev = 1.0; //position or observation standard deviation

int main() {

    float prob = Helpers::normpdf(value, parameter, stdev);

    std::cout << prob << endl;

    return 0;
}