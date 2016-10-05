
# Check if files in directory (sys.argv[2]) containing:
# sys.argv[1] substring

import os, re, sys, glob

target_dir = sys.argv[2]
elements = os.listdir(target_dir)
string = sys.argv[1]
found = 0

whole_paths = [None] * len(elements)
for i in range(0,len(elements)):
	whole_paths[i] = os.path.join(target_dir,elements[i])
	
for i in range(0,len(whole_paths)):
	if string in elements[i]:
		found = found + 1
	
if (found > 0):
	print '\n' + str(found) + ' file(s) containing substring "' + string + '"\nwere found in the following directory: \n' + target_dir + '\n'
	sys.exit(0)
else:
	sys.exit(-1)
