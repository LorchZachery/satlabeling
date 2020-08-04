import numpy as np
import cv2
from PIL import Image
import sys


drawing = False # true if mouse is pressed
pt1_x , pt1_y = None , None

# mouse callback function
def line_drawing(event,x,y,flags,param):
    global pt1_x,pt1_y,drawing

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        pt1_x,pt1_y=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.line(image,(pt1_x,pt1_y),(x,y),color=(255, 255, 255),thickness=15)
            pt1_x,pt1_y=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        
#img = np.zeros((512,512,3), np.uint8)
image = cv2.imread("image.jpeg")
cv2.namedWindow('img')
cv2.setMouseCallback('img',line_drawing)

def floodfill(x, y):

    #convert image to rbg
    #image = Image.fromarray(img)
    #image = image.convert("RGB")
    #pixdata = image.load()
    
    if pixdata[x,y] == (255, 255, 255): # the base case
        #print ("not white")
        #return

        pixdata[x, y] = (255, 255, 255)
        floodfill(x + 1, y) # right
        floodfill(x - 1, y) # left
        floodfill(x, y + 1) # down
        floodfill(x, y - 1) # up
        
def mask():

    Wmask =(image[:, :, 0:3] == [255, 255, 255]).all(2)
    cv2.imwrite('result.png', (Wmask*255).astype(np.uint8))

    #print(Wmask)
             
while(1):

    #show image on screen as drawing/filling
    cv2.imshow('img',image)
    mask()
    
    #image = cv2.imread("result.png")
    #cv2.imshow('masked image', image)
    
    #floodfill(0, 0)

    if cv2.waitKey(1) & 0xFF == 27:
        break
        

cv2.destroyAllWindows()

#for x in range(0, 512):
    #for y in range(0, 512):
        #cv2.line(img,(x,y+3),(x,y+100),color=(50,255,255),thickness= 1)
        #pixdata[y-1, x] = (20, 255, 255)
