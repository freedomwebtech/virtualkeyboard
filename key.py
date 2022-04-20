import cv2
from pynput.keyboard import Controller
from module import findpostion
import math
from time import sleep
cap = cv2.VideoCapture(0)
keyboard=Controller()
keys=[["Q","W","E","R","T","Y","U","I","O","P"],
      ["A","S","D","F","G","H","J","K","L",";"],
      ["Z","X","C","V","B","N","M",",",".","/"]]
finalText=""
def draw(img,buttonlist):
    for button in buttonlist:
        x,y=button.pos
        w,h=button.size
        cv2.rectangle(img,(button.pos),(x+w,y+h),(0,0,255),-1)
        cv2.putText(img,button.text,(x+10,y+40),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
    return img
class button():
    def __init__(self,pos,text,size=[60,60]):
        self.pos=pos
        self.text=text
        self.size=size
    
    
buttonlist=[]
for i in range(3):
    for j,key in enumerate(keys[i]):
        buttonlist.append(button([70*j+20,70*i+40],key))   

while True:

     ret, frame = cap.read()
     flipped = cv2.flip(frame, flipCode = 1)
     frame = cv2.resize(flipped, (840, 680))
    

     
     a=findpostion(frame)
     frame = draw(frame,buttonlist)
     if len(a)!=0:
        for button in buttonlist:
            x,y=button.pos
            w,h=button.size
            x1,y1=a[8][1],a[8][2]
            x2,y2=a[12][1],a[12][2]
            length = math.hypot(x2-x1,y2-y1)
            if x<x1<x+w and y<y1<y+h:
               cv2.rectangle(frame,(button.pos),(x+w,y+h),(122,0,122),-1)
               cv2.putText(frame,button.text,(x+10,y+40),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
               print(length)
               if length < 30:
               
                  cv2.rectangle(frame,(button.pos),(x+w,y+h),(0,255,0),-1)
                  cv2.putText(frame,button.text,(x+10,y+40),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
                  finalText +=button.text
                  keyboard.press(button.text)
                  keyboard.release(button.text)
                  
                  
     
         
     cv2.rectangle(frame,(50,350),(700,450),(122,0,122),-1)
     cv2.putText(frame,finalText,(60,425),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
     sleep(0.15)
     

        
       
     cv2.imshow("Frame", frame);
     if cv2.waitKey(1) & 0xFF==27:
         break
cap.release()
cv2.destroyAllWindows()
    