# Self Driving Car using Line Detection
## Publication: [Click Here](https://link.springer.com/chapter/10.1007/978-981-19-9285-8_40)
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

## Color Picking for Lane Detection
Using color picking for lane detection involves selecting specific colors that represent lane lines and using those colors to create a mask. This approach is particularly useful for detecting lane lines that are consistently colored, such as white or yellow lines on a road.

In our project, we'll use color picking to create a binary mask that highlights the lane lines based on their color. Here's a detailed explanation and implementation of this technique.

***Steps for Color Picking***
***Color Space Conversion:*** Convert the image from the BGR color space to the HSV color space. The HSV color space is preferred for color picking because it separates the image intensity (brightness) from the color information, making it easier to select specific colors.

***Define Color Range:*** Determine the range of HSV values that correspond to the colors of the lane lines. This range will be used to create a mask that highlights the lane lines.

***Apply Mask:*** Create a binary mask where the pixels within the specified color range are set to white (255) and all other pixels are set to black (0). This mask will isolate the lane lines from the rest of the image.

## Perspective Warping

Perspective warping, also known as perspective transformation, is a technique used in image processing to transform the perspective of an image as if viewed from a different angle. In the context of self-driving cars, perspective warping is crucial for lane detection. It transforms the image from a camera's perspective to a bird's-eye view, making it easier to analyze the road and lane markings.

***Why Perspective Warping is Important***

***Lane Detection:*** A bird's-eye view simplifies the task of detecting lanes by removing the perspective distortion caused by the camera angle.

***Path Planning:*** It helps in better understanding the vehicle's position relative to the lanes, which is essential for path planning and navigation.

***Object Detection:*** Objects on the road, such as obstacles or other vehicles, can be detected and tracked more accurately.

## Motor Control
Motor control in the context of a self-driving car project involves managing the speed and direction of the car's motors based on the detected lane lines and the desired trajectory. This is a crucial component as it translates the lane detection and path planning outputs into actual movement of the vehicle.

***Components of Motor Control***

Hardware Interface: Typically involves a microcontroller or a single-board computer (like a Raspberry Pi) connected to motor drivers and motors.
Motor Drivers: Electronic devices that take low-power control signals and translate them into higher-power signals to drive the motors.
Control Algorithms: Software routines that determine the appropriate motor commands based on sensor inputs and lane detection results.
Basic Concepts
Speed Control: Adjusting the motor speed to control how fast the car moves.
Direction Control: Adjusting the motor direction to control the steering of the car.
PID Control: A control loop mechanism employing proportional, integral, and derivative (PID) control to maintain a desired path.


   For More details about [Image Processing](https://github.com/mmm-byte/PythonProjects/tree/main/Self_Driving_Using_Line_Detection/Installation%20and%20Setup/Image_Processing)
   
   
For More details about [Neural Network](https://github.com/mmm-byte/PythonProjects/blob/main/Self_Driving_Using_Line_Detection/Installation%20and%20Setup/Neural_Network.md)

**Conclusion**
By following the steps above, you will be able to construct a self-driving car using lane detection with a Raspberry Pi. Each module is designed to handle specific tasks, making the system modular and easier to debug. The main script coordinates these modules, ensuring smooth operation. For more details on specific components like image processing and neural networks, refer to the linked documentation.
