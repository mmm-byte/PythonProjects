# Self Driving Car using Line Detection
We're going to use a Raspberry Pi to construct a self-driving vehicle in this project that can recognise lanes. We will first quickly review the hardware aspect before writing the code in depth and writing it step by step. Instead of using a raspberry pi, we will develop the code on a desktop computer, then add it to the pi. This means that even if the Car isn't ready, you may still follow along to learn lane detection.

## Initial Setup
We're going to set up your Raspberry Pi quickly for the first time so you can start working on a straightforward project. We'll find out how to use Windows or Mac to remotely control a Raspberry Pi. To comprehend input and output devices, we will use an LED light and a push button.


## OpenCV Installation on RaspberryPi
Raspberry Pi Opencv installation. The python package manager pip can typically be used for this, although opencv on the Raspberry Pi frequently has installation issues with pip. As a result, we must install from the source. We will walk through each step needed to install opencv from source in this video.
For More Details check [Installation](https://github.com/mmm-byte/PythonProjects/blob/main/Self_Driving_Using_Line_Detection/Installation%20and%20Setup/Installation.md) and [Configuration](https://github.com/mmm-byte/PythonProjects/blob/main/Self_Driving_Using_Line_Detection/Installation%20and%20Setup/Installation.md)

## The concept and Setup
In this series we will learn how to create a Self-Driving Car using Raspberry Pi that can follow a path using simple lane detection. We will first detect our path and then find the curve present in our road. Then we will send commands to our motors based on this curve.

We will be using the Ultimate Raspberry Pi Robot that we have built in the previous tutorials. We also managed to write a motor module that intake values of speed and turn ranging from -1 to 1 and handles the code for the H-bridge.

I added a 7 inch Touch Screen at the back since it becomes easier to debug and tune. The ease of use is mostly taken as guaranteed when working with raspberry pi and this is the leading cause of people drooping projects half way or not starting at all.

## The Concept of Lane Detection
The idea is to find the path using color detection or edge detector and then getting the curve using summation of pixels in the y direction i.e a histogram. We can split the task into 5 different steps. This includes Thresholding, Warping , Histogram, Averaging, and Displaying. Since we have been creating modules so far, we are going to create a module for lane detection as well. This way we don’t need to put all the code in one script instead we can have separate python files that each perform their separate tasks. So for this project we will have a Main Script that will be connected to our Motor Module and the Lane Detection Module. Since the Lane Detection code will take up some space we will separate all the functions into a Utilities file keeping the main Module neat and clean.

## Importing Libraries
Even though we will run the code on Raspberry pi, we are going to write the code on a PC in Pycharm. This way the coding process is much easier. All we need is a video or image to find the results and later we can simply tune the code once we run it on raspberry pi.

We will import the opencv library along with numpy. If you are not sure how to install this in raspberry pi you can follow this tutorial. Utlis is the file that we will create as a container for all our functions so that we can keep the main code tidy.

```
import cv2
import numpy as np
import utlis
```

Since we are creating a module and we want to run it as a standalone script as well we will add the if statement to check the file name. If this is the main module that was run then we will grab frame from our video and call the main function. In this case we will call the main function ‘getLaneCurve’ since that is what we are interested in.

```
if __name__ == '__main__':
    cap = cv2.VideoCapture('vid.mp4')
    while True:
        _, img = cap.read() # GET THE IMAGE      
        img = cv2.resize(img,(640,480)) # RESIZE
        getLaneCurve(img)
        cv2.waitKey(1)
   ```
   For More [Image Processing](https://github.com/mmm-byte/PythonProjects/tree/main/Self_Driving_Using_Line_Detection/Installation%20and%20Setup/Image_Processing)
