from glob import glob
import os
import shutil

input_dir = 'long_0'

txt_paths = glob('%s/*.txt' % input_dir)
for txt_path in txt_paths:
    # print(txt_path)
    base=txt_path[:-4]
    print(base)
    new_path = base + '_brightness.txt'
    print(new_path)
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        with open(new_path, 'w+', encoding='utf-8') as out:
            out.writelines(lines)


    # with open(txt_path, 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     with open(base+'__blur1.0.txt', 'w+', encoding='utf-8') as out:
    #         out.writelines(lines)
    #     with open(base+'__noise0.01.txt', 'w+', encoding='utf-8') as out:
    #         out.writelines(lines)
print('!!! DONE')