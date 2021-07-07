import sys
sys.path.append("c:/users/nachi/appdata/local/programs/python/python39/lib/site-packages")
from PIL import Image , ImageColor
import numpy as np
image = Image.open(r"D:\c programs\pic5.png")
img2arr = np.array(image)
weight = list()

for i in range(0, image.height-1, 12) :
	for j in range(0, image.width-1, 8) :
		a = img2arr[i][j][0] + img2arr[i][j+1][0] + img2arr[i+1][j][0] + img2arr[i+1][j+1][0]
		b = img2arr[i][j][1] + img2arr[i][j+1][1] + img2arr[i+1][j][1] + img2arr[i+1][j+1][1]
		c = img2arr[i][j][2] + img2arr[i][j+1][2] + img2arr[i+1][j][2] + img2arr[i+1][j+1][2]
		#d = img2arr[i][j][0] + img2arr[i][j+1][0] + img2arr[i+1][j][0] + img2arr[i+1][j+1][0]
		#NewValue = (( (int(a)+int(b)+int(c)) * int(d)) / 195075)
		NewValue = float((int(a)+int(b)+int(c))) / 765
		if (NewValue > 0.5):
			print("#", sep="", end="")
		else :
			print(" ", sep="", end="")
	#weight.append(NewValue)
	print("")
