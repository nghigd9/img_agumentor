from glob import glob
import os
import shutil

input_dir = 'square_1'

txt_paths = glob('%s/*.txt' % input_dir)
for txt_path in txt_paths:
    # print(txt_path)
    base=txt_path[:-4]
    print(base)

    # brightness label
    new_path = base + '_dec20.txt'
    print(new_path)
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        with open(new_path, 'w+', encoding='utf-8') as out:
            out.writelines(lines)

    #blur1.0 label
    # with open(txt_path, 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     with open(base+'__blur1.0.txt', 'w+', encoding='utf-8') as out:
    #         out.writelines(lines)
    #     with open(base+'__noise0.01.txt', 'w+', encoding='utf-8') as out:
    #         out.writelines(lines)

    #noise0.003
    # new_path = base + '__noise0.003.txt'
    # print(new_path)
    # with open(txt_path, 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     with open(new_path, 'w+', encoding='utf-8') as out:
    #         out.writelines(lines)
print('!!! DONE')