import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
import re

def myticks(x, pos):
	if x % 50 == 0:
		return ""
	else:
		return int(x)

def avg(ints = []):
	tot=0
	for i in ints:
		tot+=i
	return tot/len(ints)

def approx(num):
	if num % 10 >= 5:
		return int(((num // 10) + 1) * 10)
	else:
		return int((num // 10) * 10)

fig, ax = plt.subplots()

def plotInitializer(ax):

	ax.set_ylabel("Incidenza")
	ax.set_xlabel("Particelle / 10 minuti")
	ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(50))
	ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(10))
	ax.xaxis.set_minor_formatter(matplotlib.ticker.FuncFormatter(myticks))
	ax.tick_params(axis='x', which='major', labelrotation=45)
	ax.tick_params(axis='x', which='minor', labelrotation=45, labelsize=8, labelcolor='grey')
	ax.set_xlim(minVisible + phase, maxVisible + phase)
	ax.set_title("Effetto EST-OVEST")



root = tk.Tk()
root.withdraw()


minVisible = 240
maxVisible = 520
phase = 0

plotInitializer(ax)

# Per far funzionare questa cosa, i file devono essere di esattamente 1200 righe, ovvero 600 secondi*2 -> 10 minuti
for direzione in range(3):
	if direzione == 0:
		filename = filedialog.askopenfilenames(
			defaultextension='.txt',
			title="Seleziona EST"
		) # Fai in modo di poter scegliere il file col coso di windows
	elif direzione == 1:
		filename = filedialog.askopenfilenames(
			defaultextension='.txt',
			title="Seleziona OVEST"
		)
	elif direzione == 2:
		filename = filedialog.askopenfilenames(
			defaultextension='.txt',
			title="Seleziona VERTICALE"
		)
	paths = list(filename)

	data = []
	numberOfParticles = 0
	particles10min = []
	particlesIndexer = {}

	for tot in paths:
		numberOfParticles = 0
		with open(tot, "r", encoding="utf-8") as dataFile:
			data = dataFile.readlines()
		for i in range(0, len(data), 2):
			numberOfParticles += int(data[i][-2])
		particles10min.append(approx(numberOfParticles))

	for j in particles10min:
		if j in particlesIndexer:
			particlesIndexer[j] += 1
		else:
			particlesIndexer[j] = 1


	for i in particlesIndexer:
		if direzione == 0:
			ax.bar(i, particlesIndexer[i], width=8, color=(.1,.1,1,.5))
		elif direzione == 1:
			ax.bar(i, particlesIndexer[i], width=8, color=(1,.05,.05,.5))
		elif direzione == 2:
			ax.bar(i, particlesIndexer[i], width=8, color=(.1,.9,.1,.5))
	else:
		if direzione == 0:
			valoreMedio = avg(particles10min)
			print("Il valore medio EST è ", valoreMedio, "\n")
			ax.text(0.50, 0.9, r'$\bar x$ OVEST = ' + str(valoreMedio)[:8], color=(.1,.1,1,1), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
		elif direzione == 1:
			valoreMedio = avg(particles10min)
			print("Il valore medio OVEST è ", valoreMedio, "\n")
			ax.text(0.50, 0.86, r'$\bar x$ EST = ' + str(valoreMedio)[:8], color=(1,.1,.1,1), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
		elif direzione == 2:
			valoreMedio = avg(particles10min)
			print("Il valore medio VERTICALE è ", valoreMedio, "\n")
			ax.text(0.50, 0.82, r'$\bar x$ VERTICALE = ' + str(valoreMedio)[:8], color=(.1,.9,.1,1), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

# Saremo in 5 a portare questo segreto nella tomba EST <-> OVEST

plt.show()