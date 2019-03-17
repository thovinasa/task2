import cv2
import numpy as np
def afftrans(in_img):
	img=cv2.imread(in_img)
	rows,cols,ch = img.shape
	pts1=np.float32([[50,50],[200,50],[50,200]])
	pts2=np.float32([[10,100],[200,50],[100,250]])
	M = cv2.getAffineTransform(pts1,pts2)
	dst = cv2.warpAffine(img,M,(cols,rows))
		
	cv2.imwrite(in_img,dst)
