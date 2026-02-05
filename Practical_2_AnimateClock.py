import cv2 as cv
import numpy as np
import math
import time

# Canvas
size = 512
canva = np.zeros((size, size, 3), np.uint8)

def draw_clock():
    # background circles
    cv.circle(canva,(size//2,size//2),250,(255,10,20),-1)
    cv.circle(canva,(size//2,size//2),240,(180,30,30),-1)
    cv.circle(canva,(size//2,size//2),230,(180,50,35),-1)
    cv.circle(canva,(size//2,size//2),220,(180,100,40),-1)
    cv.circle(canva,(size//2,size//2),210,(180,130,45),-1)
    cv.circle(canva,(size//2,size//2),90,(180,180,45),-1)
    cv.circle(canva,(size//2,size//2),60,(150,180,105),-1)

    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(canva, "SANS", (size//2-40, size//2+50), font, 1,(0,0,0), 2, cv.LINE_AA) 
    cv.putText(canva, "VII", (size//2-120, size//2+165), font, 1.5,(10,10,10), 2, cv.LINE_AA) 

while True:
    # reset canvas each frame
    canva = np.zeros((size, size, 3), np.uint8)
    draw_clock()

    # current time
    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour % 12

    # angles (12 o’clock = -90°)
    sec_angle = math.radians(sec * 6 - 90)
    min_angle = math.radians(minute * 6 - 90)
    hour_angle = math.radians(hour * 30 + minute * 0.5 - 90)

    # hand lengths
    sec_len = 200
    min_len = 150
    hour_len = 100

    # calculate end points
    sec_x = int(size//2 + sec_len * math.cos(sec_angle))
    sec_y = int(size//2 + sec_len * math.sin(sec_angle))

    min_x = int(size//2 + min_len * math.cos(min_angle))
    min_y = int(size//2 + min_len * math.sin(min_angle))

    hour_x = int(size//2 + hour_len * math.cos(hour_angle))
    hour_y = int(size//2 + hour_len * math.sin(hour_angle))

    # draw hands
    cv.line(canva, (size//2, size//2), (sec_x, sec_y), (40,30,255), 2)
    cv.line(canva, (size//2, size//2), (min_x, min_y), (0,0,0), 6)
    cv.line(canva, (size//2, size//2), (hour_x, hour_y), (0,0,0), 10)

    cv.imshow("Clock", canva)

    if cv.waitKey(1000) & 0xFF == ord('q'):  # update every second
        break

cv.destroyAllWindows()
