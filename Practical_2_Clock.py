import cv2 as cv
import numpy as np

# computer system
# using numpy to help us to avoid enter row by row
# create 512,512 with zero all the way ==> np.zeors
# (row,column)
canva = np.zeros((512,512,3),np.uint8)

# cv.circle(which canva u want to display on, location, size(radius), colour, the parameter)
# using // to find the quotion
background = cv.circle(canva,(512//2,512//2),250,(255,10,20),-1)
background = cv.circle(canva,(512//2,512//2),240,(180,30,30),-1)
background = cv.circle(canva,(512//2,512//2),230,(180,50,35),-1)
background = cv.circle(canva,(512//2,512//2),220,(180,100,40),-1)
background = cv.circle(canva,(512//2,512//2),210,(180,130,45),-1)

background = cv.circle(canva,(512//2,512//2),90,(180,180,45),-1)
background = cv.circle(canva,(512//2,512//2),60,(150,180,105),-1)

font = cv.FONT_HERSHEY_COMPLEX
# cv.putText(canva u display, name, location, font, size, colour, thickness, how to we rended the text)
cv.putText(canva, "SANS", (512//2-40, 512//2+50), font, 1,(0,0,0), 2, cv.LINE_AA) 

# digit 7
cv.putText(canva, "VII", (512//2-120, 512//2+165), font, 1.5,(0,0,0), 2, cv.LINE_AA) 

# create Hand with a line
# cv.line(which canva/which image, starting point, end point, colour, thickness)
# (512//2, 0) cuz it is reversed

# second
seconds = cv.line(canva, (512//2,512//2), (512//2,50), (40,30,255),3)

# minute
seconds = cv.line(canva, (512//2,512//2), (512//2+165,150), (0,0,0),20)

# hour
seconds = cv.line(canva, (512//2,512//2), (140,190), (0,0,0),20)


cv.imshow("Hello World",canva) # show
cv.waitKey(0)
