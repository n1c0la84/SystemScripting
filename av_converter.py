import os, sys
import subprocess

basepath = sys.argv[1]

for root, dirs, files in os.walk(basepath):
	for file in files:
		if file.endswith(".mkv"):
			file_noext = ''.join(file.split(".")[:-1])
			process = subprocess.Popen("ffmpeg -i \"" + os.path.join(root, file) + "\" -vcodec libx264 -acodec copy -s 1280x720 \"" + os.path.join(root, file_noext) + ".mp4\"")
			process.wait()

for root, dirs, files in os.walk(basepath):
	for file in files:
		if file.endswith(".m4a") or file.endswith(".m4p"):
			file_noext = ''.join(file.split(".")[:-1])
			process = subprocess.Popen("ffmpeg -i \"" + os.path.join(root, file) + "\" -acodec libmp3lame -b:a 192k \"" + os.path.join(root, file_noext) + ".mp3\"")
			process.wait()