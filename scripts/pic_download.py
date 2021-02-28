from imutils import paths
import requests
import cv2
import os
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("--name", required=True)
# args = vars(ap.parse_args())

# grab the list of URLs from the input file, initialize the
# total number of images downloaded
rows = open('./urls1.txt').read().strip().split("\n")
total = 0
p = ''

for url in rows:

	try:
		r = requests.get(url, timeout=60)
		p = "{}.jpg".format(str(total).zfill(8))
		f = open("./output/buddha/{}".format(p), "wb")
		f.write(r.content)
		f.close()
		print("[INFO] downloaded: {}".format(p))
		total += 1
	except Exception as ex:
		print(ex)

for imagePath in paths.list_images('./output'):
	delete = False
	try:
		image = cv2.imread(imagePath)
		if image is None:
			delete = True

	# if OpenCV cannot load the image then the image is likely
	# corrupt so we should delete it
	except:
		print("Exception coming from invalid picture")
		delete = True

	# check to see if the image should be deleted
	if delete:
		print("[INFO] deleting {}".format(imagePath))
		os.remove(imagePath)