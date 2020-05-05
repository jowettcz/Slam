import cv2
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser() 
	parser.add_argument("-i", "--file", help="input file", dest="input_file", required=True) 
#	parser.add_argument("-o", "--output",help="output file location",dest="output_location",required=True)  

	video_cap = cv2.VideoCapture(parser.input_file)

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

