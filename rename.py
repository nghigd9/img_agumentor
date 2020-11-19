import os
from glob import glob

input_dir = 'square_11'
imgs_paths = glob('%s/*.jpg' % input_dir) + glob('%s/*.png' % input_dir)

print('start')

i = 0
for img_path in imgs_paths:
	print(img_path)
	os.rename(img_path, input_dir + '/sq_11_' + str(i) + '.jpg')
	i +=1
