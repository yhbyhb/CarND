#include <functional>
#include <iostream>
#include "cost.h"
#include "cmath"


using namespace std;

float inefficiency_cost(int target_speed, int intended_lane, int final_lane, vector<int> lane_speeds) {
    /*
    Cost becomes higher for trajectories with intended lane and final lane that have traffic slower than target_speed.
    */
    
    //TODO: Replace cost = 0 with an appropriate cost function.
    float cost = 0;

    float delta = (target_speed - lane_speeds[intended_lane])
    			 + (target_speed - lane_speeds[final_lane]);
   	//cost = 1 - exp(-(delta));
    cost = delta / target_speed; //solution

    return cost;
}