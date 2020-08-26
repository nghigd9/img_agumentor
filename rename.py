import os
from glob import glob

input_dir = 'sp_bottom_left'
imgs_paths = glob('%s/*.jpg' % input_dir)

print('start')

i = 0
for img_path in imgs_paths:
	print(img_path)
	os.rename(img_path, 'sp_bottom_left/sp_bottom_left' + str(i) + '.jpg')
	i +=1
