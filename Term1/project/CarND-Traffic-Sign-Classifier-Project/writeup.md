# **Traffic Sign Recognition** 
by Hanbyul Yang, Aug 9, 2017

## Overview

This is a project of Self-Driving Car Nanodegree Program of Udacity.

In this project I will classify traffic signs in given images.
For the codes, Check [`Traffic_Sign_Classifier.ipynb`](./Traffic_Sign_Classifier.ipynb).

[//]: # (Image References)

[summary_image]: ./writeup_images/summary_data.png "Summary data"
[histo_train]: ./writeup_images/histo_train.png "Histogram of training set"
[histo_valid]: ./writeup_images/histo_valid.png "Histogram of validation set"
[histo_test]: ./writeup_images/histo_test.png "Histogram of test set"
[data_aug_org]: ./writeup_images/data_aug_org.png "Sample image"
[data_augs]: ./writeup_images/data_augs.png "Data augmentation samples"
[test_images]: ./writeup_images/test_images.png "Test images from web"
[test_softmax]: ./writeup_images/test_softmax_result.png "Softmax prediction result"

## Data Set Summary & Exploration

### Basic summary of the data set

* The size of training set is `34799`.
* The size of the validation set is `4410`.
* The size of test set is `12630`
* The shape of a traffic sign image is `(32, 32, 3)`.
* The number of unique classes/labels in the data set is `43`.

### An exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. 
Below image shows each image per class and each title shows its count.
![alt text][summary_image]

There are three histograms showing how the data distributed. Data imbalance is easily noticeable. In case of training data, the largest number of class is 2100 and the smallest one is 180. Validation and test set also have data imbalance but it is similar with training set case.   

![alt text][histo_train]
![alt text][histo_valid]
![alt text][histo_test]

Here are all class names and image counts.

| ClassId |                                           SignName | Count |
|--------:|:---------------------------------------------------|------:| 
|       0 |                               Speed limit (20km/h)   | 180 |
|       1 |                               Speed limit (30km/h)  | 1980 |
|       2 |                               Speed limit (50km/h)  | 2010 |
|       3 |                               Speed limit (60km/h)  | 1260 |
|       4 |                               Speed limit (70km/h)  | 1770 |
|       5 |                               Speed limit (80km/h)  | 1650 |
|       6 |                        End of speed limit (80km/h)   | 360 |
|       7 |                              Speed limit (100km/h)  | 1290 |
|       8 |                              Speed limit (120km/h)  | 1260 |
|       9 |                                         No passing  | 1320 |
|      10 |       No passing for vehicles over 3.5 metric tons  | 1800 |
|      11 |              Right-of-way at the next intersection  | 1170 |
|      12 |                                      Priority road  | 1890 |
|      13 |                                              Yield  | 1920 |
|      14 |                                               Stop   | 690 |
|      15 |                                        No vehicles   | 540 |
|      16 |           Vehicles over 3.5 metric tons prohibited   | 360 |
|      17 |                                           No entry   | 990 |
|      18 |                                    General caution  | 1080 |
|      19 |                        Dangerous curve to the left   | 180 |
|      20 |                       Dangerous curve to the right   | 300 |
|      21 |                                       Double curve   | 270 |
|      22 |                                         Bumpy road   | 330 |
|      23 |                                      Slippery road   | 450 |
|      24 |                          Road narrows on the right   | 240 |
|      25 |                                          Road work  | 1350 |
|      26 |                                    Traffic signals   | 540 |
|      27 |                                        Pedestrians   | 210 |
|      28 |                                  Children crossing   | 480 |
|      29 |                                  Bicycles crossing   | 240 |
|      30 |                                 Beware of ice/snow   | 390 |
|      31 |                              Wild animals crossing   | 690 |
|      32 |                End of all speed and passing limits   | 210 |
|      33 |                                   Turn right ahead   | 599 |
|      34 |                                    Turn left ahead   | 360 |
|      35 |                                         Ahead only  | 1080 |
|      36 |                               Go straight or right   | 330 |
|      37 |                                Go straight or left   | 180 |
|      38 |                                         Keep right  | 1860 |
|      39 |                                          Keep left   | 270 |
|      40 |                               Roundabout mandatory   | 300 |
|      41 |                                  End of no passing   | 210 |
|      42 |  End of no passing by vehicles over 3.5 metric ...   | 210 |


## Design and Test a Model Architecture

### Preprocessing the image data.

At the first time, I didn't preprocess and just trained images and than normalized image data. The normalized training set has much faster training speed than non-normalize one. I tried grayscaling but It didn't have better validation accuracy. I think color of traffic sign is also important so I decided not to apply grayscaling.

With just normalization is not enough to get higher validation accuracy. Random rotation, translation, shear and brightness augmentation are applied to image data. 
Here are original images and 9 randomly augmented images.

![alt text][data_aug_org]
![alt text][data_augs]

I made 9 augmented images for each image. so total training images are 10 times of original training images. (So, total training set is `347990`.)

After augmenting images, normalization is applied to data.

### Final model architecture and training

Following table describes my final model.

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x3 RGB image   							| 
| Convolution 5x5     	| 1x1 stride, valid padding, outputs 28x28x50	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x50					|
| Convolution 5x5	    | 1x1 stride, valid padding, outputs 10x10x100	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x100					|
| Fully connected		| inputs 2500, outputs 100						|
| dropout				| keep probability 0.5							|
| Fully connected		| inputs 100, outputs 100						|
| dropout				| keep probability 0.5							|
| Fully connected		| inputs 100, outputs 43						|
| Softmax				| prediction  									|
 
At first, I started with LeNet-5 that is included class materials and after I also tried [published baseline model on this problem](http://yann.lecun.com/exdb/publis/pdf/sermanet-ijcnn-11.pdf). But their validation accuracies couldn't exceed 0.89. 

I added dropout layer after two fully connected layers like AlexNet. Its validation accuracy can easily exceed 0.93. After adjusting hyper-parameters such as epoch, learning rate and batch size, It performed about 0.96 ~ 0.97. 
After data augmentation, the validation performance is in range of 0.97 ~ 0.98.

I used ADAM optimizer just like one in the class material. 128 batch size and 0.001 learning rate are the optimal. 

LeNet was developed for gray-scaled image and number of class is relatively small. Also, It is developed when computing power is not enough. So, LeNet is not the best model for traffic sign classifier and Our problem needs more recent technology. AlexNet proved for 1000 classes image classifier and relatively simple comparing recent models such as Inception or ResNet. So I take some inspirations from AlexNet for my final model architecture. The results was good enough.

### Final model result

My final model results were:
* training set accuracy : `0.977`
* validation set accuracy : `0.984`
* test set accuracy : `0.960`

After 5 epochs, training set accuracy is in range of `0.96` and `1.0`.
In case of validation set accuracy, It is around in `0.97` ~ `0.98` after about 10 epochs. I tried smaller learning rate and larger epochs, decided with 0.001 learning rate and 20 epochs.
Both training set and validation set accuracy is high so it is neither overfitting nor underfitting.

## Test a Model on New Images

### German traffic signs on web
I randomly choose six images from official web site of [German Traffic Sign Recognition Benchmark](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news).
Especially, from test set. `http://benchmark.ini.rub.de/Dataset/GTSRB_Final_Test_Images.zip`

Since they are the test set, they are not labeled. So I labeled manually.
Here are six German traffic signs that I randomly selected:

![alt text][test_images]

The third image `07851.ppm` might be difficult to classify. It is confusing even my classification, but it is not `Speed limit (20km/h)`, `Speed limit (30km/h)`, or `Speed limit (50km/h)`, I decided it to `Speed limit (80km/h)`.

### Model's predictions

Here are the results of the prediction:

| Image                                         |     Prediction	        					| Result |
|:----------------------------------------------|:----------------------------------------------|:----:|
| No passing for vehicles over 3.5 metric tons  | No passing for vehicles over 3.5 metric tons  |  O  |
| Road narrows on the Right-of-way	     		| Road narrows on the Right-of-way              |  O  |
| Speed limit (80km/h) | Speed limit (50km/h) |  X  |
| Vehicles over 3.5 metric tons prohibited | Vehicles over 3.5 metric tons prohibited |  O  |
| Traffic signals | Traffic signals |  O  |
| Speed limit (60km/h) | Speed limit (60km/h) |  O  |

The model was able to correctly guess 5 of the 6 traffic signs, which gives an accuracy of 83.33%. This result is lower than the accuracy on the test set of 0.96, but the result is from only 6 images so I think it is reasonable.

### Softmax probabilities for each prediction

The code for making predictions on my final model is located in the 24th cell of the Ipython notebook.

Following is bar charts of softmax probabilities for each prediction.

![alt text][test_softmax]

Although the third image which has wrong prediction, but model predicted as second highest probability. So, my final model has 100% accuracy in top-5 manner.

## Reflections

Due to the data imbalance, the model may predict worse on smaller number classes. 
Adding dropout layers after fully connected layers gave huge performance improvement. Data augmentation also helped on model performance. 
For further improvement, I think that it needs more complicated layer and higher resolution images. AlexNet that I referred to is quite good model, but as I mentioned above, More advanced and recent architectures will be helpful. 32 x 32 is hard to classify even with bare eyes on some difficult cases.
