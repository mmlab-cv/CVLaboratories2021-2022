import cv2
import numpy as np
import matplotlib.pyplot as plt

frame = np.zeros((800,800,3),np.uint8)
last_mes = current_mes = np.array((2,1),np.float32)
last_pre = current_pre = np.array((2,1),np.float32)

def mousemove(event, x, y, s, p):
    global frame, current_mes, last_mes, current_pre, last_pre
    #last_pre = current_pre
    last_mes = current_mes
    current_mes = np.array([[np.float32(x)],[np.float32(y)]])

    #kalman.correct(current_mes)
    #current_pre = kalman.predict()

    lmx, lmy = [l.astype(int) for l in last_mes[:2]]
    # lpx, lpy = [l.astype(int) for l in last_pre[:2]]
    
    cmx, cmy = [l.astype(int) for l in current_mes[:2]]   
    # cpx, cpy = [l.astype(int) for l in current_pre[:2]]    
    
    cv2.line(frame, (lmx[0],lmy[0]),(cmx[0],cmy[0]),(0,200,0))
    #cv2.line(frame, (lpx[0],lpy[0]),(cpx[0],cpy[0]),(0,0,200))


cv2.namedWindow("Kalman")
cv2.setMouseCallback("Kalman", mousemove)

while(True):
    cv2.imshow('Kalman',frame)
    if cv2.waitKey(30) == ord('q'):
        break

cv2.destroyAllWindows()
