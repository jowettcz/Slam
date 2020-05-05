import cv2

video_cap = cv2.VideoCapture('/Users/zhangzhaowei/Desktop/Drone/unvehicle/DJI_0004.MP4')

count = 0
while True:
	count += 1
	success, image = video_cap.read()
	print(success)
	image.copyto(im)
	im = cv2.resize(im, (0,0), 0.5, 0.5)
	cv2.imshow("video",im)
	while(cv2.waitKey(300) == 's'): # wait
		image_name = ''+count+'.jpg';
		cv2.imwrite(image_name, image)

video_cap.release() 
cv2.destroyAllWindows() 

