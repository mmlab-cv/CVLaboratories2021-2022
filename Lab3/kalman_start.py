import cv2
import numpy as np
import matplotlib.pyplot as plt

frame = np.zeros((800,800,3),np.uint8)
last_mes = current_mes = np.array((2,1),np.float32)
last_pre = current_pre = np.array((2,1),np.float32)

def mousemove(event, x,y,s,p):
    global frame, current_mes, mes, last_mes, current_pre, last_pre
    #last_pre = current_pre
    last_mes = current_mes
    current_mes = np.array([[np.float32(x)],[np.float32(y)]])

    #kalman.correct(current_mes)
    #current_pre = kalman.predict()

    lmx, lmy = last_mes[0].astype(int),last_mes[1].astype(int)
    #lpx, lpy = last_pre[0].astype(int),last_pre[1].astype(int)
    
    cmx, cmy = current_mes[0].astype(int),current_mes[1].astype(int)    
    #cpx, cpy = current_pre[0].astype(int),current_pre[1].astype(int)   
    
    cv2.line(frame, (lmx[0],lmy[0]),(cmx[0],cmy[0]),(0,200,0))
    #cv2.line(frame, (lpx[0],lpy[0]),(cpx[0],cpy[0]),(0,0,200))


cv2.namedWindow("Kalman")
cv2.setMouseCallback("Kalman", mousemove)

while(True):
    cv2.imshow('Kalman',frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
