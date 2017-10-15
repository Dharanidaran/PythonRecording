# 9_filewriter.py

import os
import csv

filepath = os.path.join(os.getcwd(),"datasets","SocialData","roskilde.csv")
outputPath = os.path.join(os.getcwd(),"datasets","SocialData","light.csv")


fileObject = open(filepath,'r')
writeObject = open(outputPath,'w')

csvReader = csv.reader(fileObject,delimiter=";")
csvWriter = csv.writer(writeObject,delimiter="|")


for line in csvReader:
	csvWriter.writerow([line[-4],line[-2],line[-1]])