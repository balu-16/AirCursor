import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

wCam, hCam = 640, 480
frameR = 100
smoothening = 7

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

dragging = False  # Flag to track dragging state

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open camera. Trying camera index 0.")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open any camera. Exiting.")
        exit()
    else:
        print("Camera index 0 opened successfully.")
else:
    print("Camera index 1 opened successfully.")

cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame. Exiting.")
        break

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        fingers = detector.fingersUp()

        # Stop dragging if all fingers are closed
        if fingers == [0, 0, 0, 0, 0]:
            dragging = False
            autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)  # Ensure dragging is stopped

        else:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

            # Move the mouse when thumb, index, and middle fingers are open
            if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                autopy.mouse.move(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

            # Left Click when thumb and index touch (Dragging Mode)
            length_thumb_index, img, _ = detector.findDistance(4, 8, img)
            if length_thumb_index < 40:
                if not dragging:
                    autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)  # Click and hold
                    dragging = True
                cv2.circle(img, (lmList[8][1], lmList[8][2]), 15, (0, 255, 0), cv2.FILLED)
            else:
                if dragging:
                    autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)  # Release drag
                    dragging = False

            # Right Click when thumb and middle touch
            length_thumb_middle, img, _ = detector.findDistance(4, 12, img)
            if length_thumb_middle < 40:
                cv2.circle(img, (lmList[12][1], lmList[12][2]), 15, (0, 0, 255), cv2.FILLED)
                autopy.mouse.click(autopy.mouse.Button.RIGHT)

    # Show FPS and display the image to prevent freezing
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow('Image', img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
