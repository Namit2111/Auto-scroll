import cv2
import numpy as np
import pyautogui
  
blue_lower=np.array([100,150,0],np.uint8)   #range of the color you want to be detected
blue_upper=np.array([140,255,255],np.uint8)

cap = cv2.VideoCapture(0)               # to capture video footage

prev_y = 0

while True:     
	ret, frame = cap.read()  
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, blue_lower, blue_upper)                 #Hide background
	contours, hierarchy = cv2.findContours(
		mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for i in contours:
		area = cv2.contourArea(i)
		if area > 1000:
			x, y, w, h = cv2.boundingRect(i)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			if y < prev_y:
				pyautogui.press('down')
			prev_y = y
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) == ord('q'):                          #to get out of loop
		break

cap.release()
cap.closeAllWindow()
cv2.destroyWindow()
