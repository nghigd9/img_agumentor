import os
from glob import glob

input_dir = 'long_10'
imgs_paths = glob('%s/*.jpg' % input_dir)

print('start')

i = 0
for img_path in imgs_paths:
	print(img_path)
	os.rename(img_path, input_dir + '/l_bx_bca' + str(i) + '.jpg')
	i +=1
