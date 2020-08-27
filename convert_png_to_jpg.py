import cv2
from glob import glob

input_dir = 'square_6'
output_dir = 'jpg'

img_paths = glob('%s/*.png'% input_dir) 
# + glob('%s/*.jpg'% input_dir)
for img_path in img_paths:
	#print(img_path)
	img = cv2.imread(img_path)
	base = img_path[:-4]
	print(base)
	cv2.imwrite('jpg/'+base+'.jpg', img)

