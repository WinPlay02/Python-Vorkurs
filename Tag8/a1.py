import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

teilnehmeranzahl = [('2020-10-12', 210), ('2020-10-13', 180),
					('2020-10-14', 180), ('2020-10-15', 165),
					('2020-10-16', 160), ('2020-10-19', 165),
					('2020-10-20', 155), ('2020-10-21', None),
					('2020-10-22', None), ('2020-10-23', None)]
colors = ["blue" if x[1] != None else "red" for x in teilnehmeranzahl]

#a)
def daily_lost(teilnehmeranzahl):
	verlust = []
	for i in range(1, len(teilnehmeranzahl)):
		if(teilnehmeranzahl[i][1] == None):
			continue
		verlust.append(1 - teilnehmeranzahl[i][1] / teilnehmeranzahl[i-1][1])
		print(f"Lost: {(1 - teilnehmeranzahl[i][1] / teilnehmeranzahl[i-1][1])*100}%")
	return verlust

#b)
def list_to_numb_array(verlust):
	return np.array(verlust, dtype = 'float32')


#c)
def info(nparray):
	print(f"Min: {np.amin(nparray)}")
	print(f"Max: {np.amax(nparray)}")
	print(f"Std: {np.std(nparray)}")
	print(f"Avg: {np.average(nparray)}")

#d)
def to_pd_DataFrame(teilnehmeranzahl): 
	f = pd.Series(dict(teilnehmeranzahl))
	df = pd.DataFrame({'teilnehmer': f})
	print(df)
	return df

#e)
def barchart(dataframe):
	plt.style.use('seaborn-whitegrid')
	# dataframe.T.plot(kind='bar', colors=colors)
	plt.bar(dict(teilnehmeranzahl).keys(), dataframe["teilnehmer"], color=colors, label='index') # 
	plt.xticks(rotation='vertical')

	plt.ylabel('Teilnehmeranzahl')
	plt.title('Python Vorkurs')
	plt.show()

#f)
def extrapolate(nparray):
	for i in range(1, len(teilnehmeranzahl)):
		if(teilnehmeranzahl[i][1] == None):
			teilnehmeranzahl[i] = (teilnehmeranzahl[i][0], teilnehmeranzahl[i-1][1] * (1.0-np.average(nparray)))
			continue
	return to_pd_DataFrame(teilnehmeranzahl)
