from glob import glob
import  os

input_dir = 'square_6'

img_paths = glob('%s/*.jpg' % input_dir )

i = 0
for img_path in img_paths:
    # print(img_path)
    base = img_path[:-4]
    # print(base)
    txt_path = base + '.txt'
    print(txt_path)
    new_img_path = input_dir + '/' + 'top_down_square' + str(i) + '.jpg'
    #new_txt_path = input_dir + '/' + 'top_down' + str(i) + '.txt'
    i += 1
    os.rename(img_path, new_img_path)
   # os.rename(txt_path, new_txt_path)
print('done.')
