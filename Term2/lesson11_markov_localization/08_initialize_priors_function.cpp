#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

//initialize priors assumimg vehicle at landmark +/- 1.0 meters position stdev
std::vector<float> initialize_priors(int map_size, std::vector<float> landmark_positions,
                                     float control_stdev);

int main() {

    //set standard deviation of position:
    float control_stdev = 1.0f;


    //set map horizon distance in meters 
    int map_size = 25;

    //initialize landmarks
    std::vector<float> landmark_positions {5, 10, 20};

    // initialize priors
    std::vector<float> priors = initialize_priors(map_size, landmark_positions,
                                                  control_stdev);
    
    //print values to stdout 
    for (unsigned int p = 0; p < priors.size(); p++) {
        std::cout << priors[p] << endl;
    }
        
    return 0;

};

//TODO: Complete the initialize_priors function
std::vector<float> initialize_priors(int map_size, std::vector<float> landmark_positions,
                                     float control_stdev) {

//initialize priors assumimg vehicle at landmark +/- 1.0 meters position stdev

    //YOUR CODE HERE
    std::map<int, float> probs;
    for (const auto& pos : landmark_positions)
    {
        for (int i = -control_stdev; i <= control_stdev; ++i)
        {
           probs.insert(std::pair<int, float>(pos - i, 1));
        }
    }

    int length = probs.size();

    std::vector<float> priors;
    for (int i = 0; i < map_size; ++i)
    {
        priors.push_back((float)0);
    }

    for( const auto& loc_prob : probs )
    {
        priors[loc_prob.first] = loc_prob.second / length;
    }
    return priors;
}
