
# Delete all files in directory (sys.argv[2]) containing:
# sys.argv[1] substring

import os, re, sys, glob

string = sys.argv[1]
target_dir = sys.argv[2]
elements = os.listdir(target_dir)

whole_paths = [None] * len(elements)
for i in range(0,len(elements)):
	whole_paths[i] = os.path.join(target_dir,elements[i])
	
for i in range(0,len(whole_paths)):
	if string in elements[i]:
		os.remove(whole_paths[i])
	
print '\nAll files, containing substring "' + string + '"\nwere deleted in the following directory: \n' + target_dir
