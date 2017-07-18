# **Finding Lane Lines on the Road** 
by Hanbyul Yang, July 18, 2017

## Overview

This is the first project of Self-Driving Car Nanodegree Program of Udacity.

In this project I will detect lane lines in given images and videos.
For the codes, Check `P1.ipynd` file.

## Reflection


### 1. Pipeline and Improving `draw_lines()` function

My pipeline consisted of 6 steps.

1. Grayscale the input image.
<img src="./pipeline/1_gray.jpg" alt="Grayscale" width="50%" height="50%">
2. Blur the image before canny edge detection.
<img src="./pipeline/2_blur.jpg" alt="Blur" width="50%" height="50%">
3. Extract edges from blurred image.
<img src="./pipeline/3_edges.jpg" alt="Canny Edges" width="50%" height="50%">
4. Mask edges with region of interest that has shape of trapezoid.
<img src="./pipeline/4_roi_edges.jpg" alt="Mask" width="50%" height="50%">
5. Get lane lines using Hough transform.
<img src="./pipeline/5_hough.jpg" alt="Hough Lines" width="50%" height="50%">
6. Finally, draw detected lane lines to original image.
<img src="./pipeline/6_weighted.jpg" alt="Draw lines on orginal Image" width="50%" height="50%">

In order to draw a single line on the left and right lanes, I modified the `draw_lines()` function. There are two lane lines to detect. First, I divided to edges from `hough_lines` by their sign of slope. So, if slope is positive, it is line for right lane and negative slope means it is for left lane. There are `y_min` and `y_max` values that are used for masking edges. Using slope and y-intercept that are calculated by `numpy.polyfit()`, two points can be found per line. 

<img src="./pipeline/7_improved.jpg" alt="Imporved draw_lines()" width="50%" height="50%">


### 2. Potential shortcomings with current pipeline

One potential shortcoming would be what would happen when the image has strong shades, Such as trees and central reservations.

<img src="./shortcoming/central_reservation_shadow.jpg" alt="Imporved draw_lines()" width="50%" height="50%">
<img src="./shortcoming/wood_shadow.jpg" alt="Imporved draw_lines()" width="50%" height="50%">

Another potential shortcoming could be lack of robustness on changing color of road.

<img src="./shortcoming/white_road.jpg" alt="Imporved draw_lines()" width="50%" height="50%">


### 3. Possible improvements to pipeline

A possible improvement would be to use some previous detected lane line result.

Another potential improvement could be to ...
