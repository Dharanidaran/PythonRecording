# fileRead.py

import os


pathToDir = os.getcwd()


# pathToFile = "/Users/dharani/Desktop/PythonRecording"+"/datasets/SocialData/roskilde.csv"


pathToFile = os.path.join(os.getcwd(),"datasets","SocialData","roskilde.csv")

print(pathToFile)