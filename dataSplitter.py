import tkinter as tk
from tkinter import filedialog
import os

filename = filedialog.askopenfilename()
#print(type(filename))
#lastSlash = findall(r'/', filename)[-1]
lastSlash = filename.rfind(r'/')
#print(lastSlash)

secondiDaDividere = 600
seconds = secondiDaDividere * 2

with open(filename, "r", encoding="utf-8") as dati:
	data = dati.readlines()


#Dobbiamo scartare l'ultimo file se ha meno di seconds righe, senno sfaserebbe le misurazioni degli altri
noOfFiles = len(data)//seconds
for ll in range(0, noOfFiles):
	curfile = "partition_" + str(ll+1) + "_" + str(filename[lastSlash+1:])
	print(curfile)
	if not os.path.exists(curfile):
		partition = open(curfile, 'x')
	else:
		partition = open(curfile, 'w')		

	for i in data[ll*seconds: (ll+1)*seconds]:
		partition.write(i)
	
