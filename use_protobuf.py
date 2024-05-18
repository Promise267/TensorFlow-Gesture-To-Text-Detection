import os
import sys
args = sys.argv
direcotry = args[1]
protoc_path = args[2]
for file in os.listdir(direcotry):
	if file.endswith(".protoc"):
		os.system(protoc_path+" "+directory+"/"+file+" --python+out=.")