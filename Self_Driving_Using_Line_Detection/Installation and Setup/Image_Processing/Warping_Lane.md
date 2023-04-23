# Warping
We don’t want to process the whole image because we just want to know the curve on the path right now and not a few seconds ahead. So we can simply crop our image, but this is not enough since we want to look at the road as if we were watching from the top . This is known as a bird eye view and it is important because it will allow us to easily find the curve. To warp the image we need to define the initial points. These points we can determine manually. So to make this process easier we could use track bars to experiment with different values. The idea is to get a rectangle shape when the road is straight.

We can create two functions for the trackbars. One that initializes the trackbars and the second that get the current value from them.

```
def nothing(a):
    pass
def initializeTrackbars(intialTracbarVals,wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)
def valTrackbars(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points
 ```   
 
Now we can call the initialize function at the start of the code and the valTrackbar in the while loop just before warping the image. Since both functions are written in the utlis file we will write ‘utlis.’ before calling them.
```
intialTracbarVals = [110,208,0,480]
utlis.initializeTrackbars(intialTracbarVals)
```
```
points = utlis.valTrackbars()
```

Now we will write our warping function that will allow us to get the bird eyes view using the four points that we just tuned.

```
def warpImg (img,points,w,h,inv=False):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2,pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp
   ```
   
Here we are getting the transformation matrix based on the input points and then warping the image using the ‘warpPrespective’ function. Since we will also need to apply inverse Warping later on, we will add this functionality to our function. To inverse we just need the inverse matrix which we can find by switching the pts1 and pts2.

Now we call call our function to get the warp perspective.
```
imgWarp = utlis.warpImg(imgThres, points, wT, hT)
```

Its a good idea to visualize our points to make the tuning process easier. So to display our points we can create a new function that loops through the points and draws them using the ‘circle’ function.
```
def drawPoints(img,points):
    for x in range( 0,4):
        cv2.circle(img,(int(points[x][0]),int(points[x][1])),15,(0,0,255),cv2.FILLED)
    return img
```

Now we can call this function to draw the points.
```
imgWarpPoints = utlis.drawPoints(imgWarpPoints, points)
```
