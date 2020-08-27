from glob import glob

input_dir = 'square_1'

txt_paths = glob('%s/*.txt' % input_dir)

img_paths = glob('%s/*.jpg' % input_dir)

print('number of txts:', len(txt_paths))
print('num imgs:', len(img_paths))

