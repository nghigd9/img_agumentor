from glob import glob
from shutil import copyfile


input_dir = 'long_3'

img_paths = glob('%s/*.jpg' % input_dir)

for img_path in img_paths:
	base = img_path[:-4]
	print(base)
	# print(img_path)
	new_img_path = 'output/' + img_path
	copyfile(img_path, new_img_path)

	txt_path = base+'.txt'
	new_txt_path = 'output/' + txt_path
	copyfile(txt_path, new_txt_path)

print('!!!!done.')