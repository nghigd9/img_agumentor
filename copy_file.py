from glob import glob
import shutil

input_dir = 'data'

files = glob('%s/*.jpg' % input_dir)

i = 1
for file in files:
	filename = file.split('/')[-1]
	print(filename)
	if i % 1 == 0:
		shutil.move(file, "data/"+filename)
	if i % 4 == 1:
    		shutil.move(file, "plate_2/"+filename)
	if i % 4 == 2:
    		shutil.move(file, "plate_3/"+filename)
	if i % 4 == 3:
    		shutil.move(file, "plate_4/"+filename)
	i += 1
print('done')
