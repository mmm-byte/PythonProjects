import cv2
import numpy as np
import utlis

curveList = []
avgval = 10

def getLaneCurve(img,display=2):
    imgcopy = img.copy()
    imgResult = img.copy()
    ###STEP 1
    imgThres = utlis.thresholding(img)

    ###STEP 2
    hT,wT,c = img.shape
    points = utlis.valTrackbars()
    imgwarp = utlis.warpImg(imgThres,points,wT,hT)
    imgWarpPoints = utlis.drawPoints(imgcopy, points)

    ###STEP 3
    middlePoint, imgHist = utlis.getHistogram(imgwarp, display=True, minPer=0.5, region=4)
    curveAveragePoint,imgHist = utlis.getHistogram(imgwarp,display=True,minPer=0.5)
    curveRaw = curveAveragePoint - middlePoint

    ###STEP 4
    curveList.append(curveRaw)
    if len(curveList) > avgval:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))

    ### STEP 5 Display
    if display != 0:
        imgInvWarp = utlis.warpImg(imgwarp, points, wT, hT, inv=True)
    imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
    imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
    imgLaneColor = np.zeros_like(img)
    imgLaneColor[:] = 0, 255, 0
    imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
    imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
    midY = 450
    cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
    cv2.line(imgResult, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
    cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
    for x in range(-30, 30):
        w = wT // 20
    cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
    (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
    #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    #cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3);
    if display == 2:
        imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgwarp],
                                             [imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv2.imshow('Resutlt', imgResult)

    ###mormalization
    curve = curve/100
    if curve > 1: curve=1
    if curve < -1:curve=-1
    #print(basePoint-midPoint)

    #cv2.imshow('Thres', imgThres)
    #cv2.imshow('wrap', imgwarp)
    #cv2.imshow('wrap points', imgWarpPoints)
    #cv2.imshow('Histogram',imgHist)
    return curve

if __name__ == '__main__':
    intialTracbarVals = [0,208,0,480]
    utlis.initializeTrackbars(intialTracbarVals)
    cap = cv2.VideoCapture()
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        success, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        ##cv2.imshow('vid',img)
        curve = getLaneCurve(img,display=1)
        print(curve)
        cv2.waitKey(1)
