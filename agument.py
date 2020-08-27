import os
from glob import glob
import random
import cv2
import imutils

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



def rotate_image(image_path, range_angle, output_path):
    """
    range_angle: Khoảng góc quay
    """
    image = cv2.imread(image_path)
    #lựa chọn ngẫu nhiên góc quay 
    angle = random.randint(-10, 5)
    
    img_rot = imutils.rotate(image, angle)
    cv2.imwrite(output_path, img_rot)


input_dir = 'square_1'
imgs_paths = glob('%s/*.jpg' % input_dir)

print('start')
for img_path in imgs_paths:
    base = img_path[:-4]
    print(base)
    out = base + '_dec20.jpg'
    #rotate_image(img_path, 0, out)
    # change_brightness(img_path, out, 25)
    # add_boder(img_path, out, 350, 500)
    print(out)
	
