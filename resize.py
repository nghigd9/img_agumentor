import os
from glob import glob
import cv2

input_dir = './bus/'
imgs_paths = glob('%s/*.jpg' % input_dir) + glob('%s/*.png' % input_dir)
output_dir = './bus/'

print('start')

i = 0
for img_path in imgs_paths:
    print(img_path)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    file_name = img_path.split('/')[-1]
    print(file_name)
    cv2.imwrite(output_dir + file_name, img)
