from glob import glob

input_dir = 'long_1'

txt_paths = glob('%s/*.txt' % input_dir)

for txt_path in txt_paths:
	print(txt_path)
	newLines = []
	with open(txt_path, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			new = '1 ' + line[2:]
			newLines.append(new)
	with open('txt/'+txt_path, 'w+', encoding='utf-8') as out:
		out.writelines(newLines)
print('done')
