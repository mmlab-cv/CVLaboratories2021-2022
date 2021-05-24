import cv2
import numpy as np 

face_cascade_front_path = '/home/mmlab/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml'
face_cascade_profile_path = '/home/mmlab/opencv/data/haarcascades/haarcascade_profileface.xml'

grrr_image = cv2.imread('/home/mmlab/workspace/CVLaboratories/Test/grr.jpg')

cap = cv2.VideoCapture(0)

casc_front = cv2.CascadeClassifier()
casc_front.load(face_cascade_front_path)

casc_profile = cv2.CascadeClassifier()
casc_profile.load(face_cascade_profile_path)

while cap.isOpened():
    ret, frame = cap.read()
    #frame = resize(frame, 0.4)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    detected = casc_front.detectMultiScale(frame_gray, 1.1, 2, 0 | cv2.CASCADE_SCALE_IMAGE, (30, 30))
    detected_profile = casc_profile.detectMultiScale(frame_gray, 1.1, 2, 0 | cv2.CASCADE_SCALE_IMAGE, (30, 30))

    for (x,y,w,h) in detected:
        cv2.rectangle(frame, (x, y),(x + w, y + h), (255,0,255), 3)

        # 1] BLUR
        #frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (40, 40))
        # 2] SHUFFLING PIXELS
        # np.random.shuffle(frame[y:y+h, x:x+w].flat)
        # 3] NEGATIVE
        # frame[y:y+h, x:x+w] = cv2.bitwise_not(frame[y:y+h, x:x+w])
        # 4] EMOJI
        #grrr_resize = cv2.resize(grrr_image, (w, h)) 
        #frame[y:y+h, x:x+w] = grrr_resize

    for (x,y,w,h) in detected_profile:
        cv2.rectangle(frame, (x, y),(x + w, y + h), (255,0,0), 3)


    cv2.imshow("video", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
