from random import random
import cv2
import mediapipe as mp
import math
import time
import numpy as np
# import tensorflow as tf

# # Eğer tensorflow gpu da çalışıyorsa onu engelleyip cpu ya almak için
# tf.config.set_visible_devices([], 'GPU')


class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5, trackCon=0.5):
        # tf.config.set_visible_devices([], 'GPU')
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, 
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon, 
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
        return lmlist

class SnakeGame():
    def __init__(self) -> None:
        self.points = [] # list of points
        self.lengths=[]# list of lengths
        self.currentLength = 0 # total length of snake
        self.allowedLength = 150 # total allowed length 
        self.previousHead = (0,0) # previous head position
        # self.pathFood="/media/serkancam/yedek/Calismalar/python/okulCalismalar/oyg_calisma/opencv/images/elma.jpg"
        # self.imgFood=cv2.imread(self.pathFood,cv2.IMREAD_UNCHANGED)
        # self.hFood,self.wFood,self.cFood=self.imgFood.shape
        # self.foodPoint=(0,0)
        # self.randomFoodLocation()
    
    def randomFoodLocation(self):
        self.foodPoint=random.randint(100,1000),random.randint(100,600)
    
    def update(self,imgMain, currentHead):
        
        px,py = self.previousHead
        cx,cy=currentHead        
        self.points.append((cx,cy))
        distance = math.hypot(cx-px,cy-py)#((cx-px)**2 + (cy-py)**2)**0.5
        self.lengths.append(distance)
        self.currentLength += distance
        self.previousHead=currentHead#cx,cy
        #length reducion    
        if self.currentLength>self.allowedLength:
            for i,length in enumerate(self.lengths):
                self.currentLength -= length
                self.points.pop(i)# del self.points[i]
                self.lengths.pop(i)# del self.lengths[i]
                if self.currentLength<self.allowedLength:
                    break 
               
        #draw snake
        if self.points:
            for i,point in enumerate(self.points):
                if i!=0:
                    cv2.line(imgMain,self.points[i-1],self.points[i],(0,0,255),20)
            cv2.circle(imgMain,self.points[-1],20,(200,0,200),cv2.FILLED)
        #draw food
        
        return imgMain

def overlayPNG(self,imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape
    *_, mask = cv2.split(imgFront)
    maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)
    imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)

    imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    maskBGRInv = cv2.bitwise_not(maskBGR)
    imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv

    imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)
    imgBack = cv2.bitwise_or(imgBack, imgMaskFull)

    return imgBack

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
detector = handDetector()

game=SnakeGame()


while True:
    success, img = cap.read()
    img=cv2.flip(img,1)
    img = detector.findHands(img,draw=False)
    lmlist = detector.findPosition(img=img,draw=False)
    if len(lmlist) != 0:  
       pointIndex=tuple(lmlist[8][1:])
       img=game.update(imgMain=img,currentHead=pointIndex)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()