import os
from glob import glob
import random
import cv2

# Cách1
def add_boder(image_path, output_path, low, high):
    """
    low: kích thước biên thấp nhất (pixel)
    hight: kích thước biên lớn nhất (pixel)
    """
    # random các kích thước biên trong khoảng (low, high)
    top = random.randint(low, high)
    bottom = random.randint(low, high)
    left = random.randint(low, high)
    right = random.randint(low, high)
    
    image = cv2.imread(image_path)
    original_width, original_height = image.shape[1], image.shape[0]
    
    #sử dụng hàm của opencv để thêm biên
    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_REPLICATE)
    
    #sau đó resize ảnh bằng kích thước ban đầu của ảnh
    image = cv2.resize(image, (original_width, original_height))
    cv2.imwrite(output_path, image)

def change_brightness(image_path, output_path, value):
    """
    value: độ sáng thay đổi
    """
    img=cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v[v > 255] = 255
    v[v < 0] = 0
    
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    
    cv2.imwrite(output_path, img)



input_dir = 'bien_so_car_long_test'
imgs_paths = glob('%s/*.jpg' % input_dir)

print('start')
for img_path in imgs_paths:
	base = img_path.split('.')[0]
	out = base + '_margin.jpg'
	add_boder(img_path, out, 50, 175)
	print(out)
	
