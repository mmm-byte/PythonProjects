# Histogram
Now comes the most important part, finding the curve in our path . To do this we will use the summation of pixels. But what is that? Given that our Warped image is now binary i.e it has either black or white pixels, we can sum the pixel values in the y direction. Lets look at this in more detail.

![image](https://user-images.githubusercontent.com/73929680/233860258-e592c3af-9e41-49a2-9e3f-b740a98792ec.png)

The picture above shows all the white pixels with 255 value and all the black with 0. Now if we sum the pixels in first column it yeilds 255+255+255+255+255 = 1275. We apply this method to each of the columns. In our original Image we have 480 pixels in the width. Therefore we will have 480 values. After summation we can look at how many values are above a certain threshold hold lets say 1000 on each side of the center red line. In the above example we have 8 columns on the left and 3 columns on the right. This tells us that the curve is towards left. This is the basic concept, though we will add a few more things to improve this and get consistent results. But if we look deeper into this we will face a problem. Lets have a look.

![image](https://user-images.githubusercontent.com/73929680/233860283-49e61645-5983-4292-8ffe-d88582000210.png)

The above images shows the 3 cases where this methods would work. We can clearly see that when the curve is right the number of pixels on the right hand side are more than the left and vise versa. And when its straight the number of pixels are approximately same on both sides.

This is all good but there are cases when this method would fail . An example is shown below.

![image](https://user-images.githubusercontent.com/73929680/233860364-946f3a5a-6369-4edc-acf7-dd9f2c6ec2fe.png)

Here even though there is no curve since more pixels are present on one side the algorithm will output either left or right curve. So how can we fix this problem. The answer is simple we adjust the center line.

![image](https://user-images.githubusercontent.com/73929680/233860384-10d49ab0-c6e7-4fd8-892a-1f5794b2522a.png)

So now we have to find the center of the base which will give us the center line and then compare the pixels on both side.

Lucky for us both processes can be computed with the same function. By sumation of these pixels we are basically finding the histogram. Therefore we will call this function ‘getHistogram’. Lets assume we are doing the second step where we have to sum all the pixels and later we will come back to step one to find the center of the base.

First we will declare our function that will take image as an input argument. The we will simply sum all the pixels in the y direction . Achieving this is easier than it sounds as it requires just one line of code.

```
def getHistogram(img,display=False,minVal = 0.1,region= 4):
 
    histValues = np.sum(img, axis=0)
  ```

Here histValues are the 480 values that contain the sum of each column.

Now some of the pixels in our image might just be noise. So we don’t want to use them in our calculation . Therefore we will set a threshold value which will be the minimum value required for any column to qualify as part of the path and not noise. We can set a hard-coded value but it is better to get it based on the live data. So we will find the maximum sum value and multiply our user defined percentage to it to create our threshold value.

```
maxValue = np.max(histValues)  # FIND THE MAX VALUE
minValue = minPer*maxValue
```

Now we can simply add all the number of pixels on each side and find left right or straight direction. But this is not what we want, if the curve is right we want to know how much right. To get the value of the curvature we will find the indices of all the columns that have value more than our threshold and then we will average our indices. This means that if our pixels indices started from 30 and ended at 300, our average would be (300-30)/2 +30 = 165.
```
indexArray =np.where(histValues >= minValue) # ALL INDICES WITH MIN VALUE OR ABOVE
basePoint =  int(np.average(indexArray)) # AVERAGE ALL MAX INDICES VALUES
```

The base value is now the average base point of our image. We can draw this base point to visualize better.

```
if display:
    imgHist = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for x,intensity in enumerate(histValues):
       # print(intensity)
        if intensity > minValue:color=(255,0,255)
        else: color=(0,0,255)
        cv2.line(imgHist,(x,img.shape[0]),(x,img.shape[0]-(intensity//255//region)),color,1)
    cv2.circle(imgHist,(basePoint,img.shape[0]),20,(0,255,255),cv2.FILLED)
```

