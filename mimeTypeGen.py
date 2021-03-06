#!/bin/env python3
# Changed this to add or remove mime types you want or dont want

import sys

if len(sys.argv) < 2:
	print("Please provide a path to your mime.types file")
	exit(1)

infile = open(sys.argv[1])
fullfile = infile.readlines()
infile.close()

base = """
typedef struct {
char const *const Extension;
char const *const Type;
} mimeType;

const mimeType mTypes[] = {

"""

template = "	{\"{1}\",\"{2}\\r\\n\"},"

print(base)



for line in fullfile:
	if line[0] == '#':
		continue
	line = line.split()

	try:
		while 1:
			line = line.remove('')
	except:
		pass

	if line == [] or line == None:
		continue

	type = line.pop(0)
	temp = template.replace("{2}",type);
	for i in line:
		print(temp.replace("{1}",i))
print("};")
