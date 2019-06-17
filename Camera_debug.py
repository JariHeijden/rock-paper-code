#file made by Jari so we will be able to changes values in the arrays and see results for debugging purposes
#needed for example when the lighting will be diffirent or people use a diffirent camera
import cv2											#imports cv2 needed for everything camera
import numpy as np									#imports numpy as np so we can make the arrays needed for color detection

videoCapJhei = cv2.VideoCapture(1)					#so there is a value asigned to the camera. (1) is so it selects an external camera

#these are the arrays used for the color detection they are made with HSV values in mind (Hue, Saturation, Value)
lower_redJhei = np.array([0, 180, 160])
upper_redJhei = np.array([30, 255, 255])

lower_greenJhei = np.array([65, 100, 80])
upper_greenJhei = np.array([95, 255, 255])

lower_blueJhei = np.array([90, 220, 100])
upper_blueJhei = np.array([120, 255, 255])

while(True):
    _, frameJhei = videoCapJhei.read(1)				        #captures the raw footage and makes it workable
    flipImgJhei = cv2.flip(frameJhei,1)				        #Mirrors the captured footage
    
    hsv = cv2.cvtColor(flipImgJhei, cv2.COLOR_BGR2HSV)		#aplies a HSV mask to the footage

    maskRedJhei = cv2.inRange(hsv, lower_redJhei, upper_redJhei)					#takes the captured footage and checks if pixels are in between the 2 selected arrays (Red)
    maskGreenJhei = cv2.inRange(hsv, lower_greenJhei, upper_greenJhei)				#takes the captured footage and checks if pixels are in between the 2 selected arrays (Green)
    maskBlueJhei = cv2.inRange(hsv, lower_blueJhei, upper_blueJhei)					#takes the captured footage and checks if pixels are in between the 2 selected arrays (Blue)

    cv2.imshow('no filter',flipImgJhei) 				                            #displays the unfiltered video feed
    cv2.imshow("hsv", hsv)									                        #displays the footage with a HSV filter
    cv2.imshow("red", maskRedJhei)						                            #displays the red mask footage
    cv2.imshow("blue", maskBlueJhei)					                            #displays the blue mask footage
    cv2.imshow("green", maskGreenJhei)				                                #displays the green mask footage
	
    if cv2.waitKey(24) & 0xFF == ord(' '):			#if spacebar is pressed it will break the while loop
        break

cv2.destroyAllWindows()				    #closes all video windows
videoCapJhei.release()					#stops the camera from capturing footage