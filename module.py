import cv2
import mediapipe as freedomtech

drawingModule = freedomtech.solutions.drawing_utils
handsModule = freedomtech.solutions.hands

mod=handsModule.Hands()


h=680
w=840


def findpostion(frame):
    list=[]
    results = mod.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
       for handLandmarks in results.multi_hand_landmarks:
           drawingModule.draw_landmarks(frame, handLandmarks, handsModule.HAND_CONNECTIONS)
           list=[]
           for id, pt in enumerate (handLandmarks.landmark):
                x = int(pt.x * w)
                y = int(pt.y * h)
                list.append([id,x,y])

    return list            





