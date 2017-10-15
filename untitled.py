

import json
from pprint import pprint
import os

filepath = os.getcwd()+'/datasets/'+'RoskildeImage.json'

print(filepath)

filepointer = open(filepath)

data = json.load(filepointer)


for item in data["webDetection"]["webEntities"]:
	print(item["score"],item["description"])


