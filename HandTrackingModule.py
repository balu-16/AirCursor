import cv2
import mediapipe as mp
import math
import numpy as np

class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity,
        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.lmList = [] #Initialize lmList here.
        self.results = None #Initialize results here.

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                    self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True):
        self.lmList = [] #Clear lmList at the beginning of the function
        if self.results and self.results.multi_hand_landmarks: # Check if results and multi_hand_landmarks exist
            if handNo < len(self.results.multi_hand_landmarks): #check if the handNo is within the range of detected hands.
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    self.lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                return self.lmList, None #added none to return to match the calling function.
            else:
                return [], None # return empty list and None if handNo is out of range.
        else:
            return [], None #return empty list and None if no hand is detected.

    def fingersUp(self):
        fingers = []
        if len(self.lmList) > 0: #ensure there is a hand detected before trying to get fingers.
            # Thumb
            if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Fingers
            for id in range(1, 5):
                if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # totalFingers = fingers.count(1)

            return fingers
        else:
            return [] #return empty list if no hand is found.

    def findDistance(self, p1, p2, img, draw=True,r=15, t=3):
        if len(self.lmList) > 0 and p1 < len(self.lmList) and p2 < len(self.lmList): #ensure lmList has data and p1 and p2 are valid indexes.
            x1, y1 = self.lmList[p1][1:]
            x2, y2 = self.lmList[p2][1:]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            if draw:
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
                cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
                length = math.hypot(x2 - x1, y2 - y1)

            return length, img, [x1, y1, x2, y2, cx, cy]
        else:
            return 0, img, [] #return default values if lmList is empty or indexes are invalid.