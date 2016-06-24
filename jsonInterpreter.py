 #!/usr/bin/python

import json
import numpy as np
import datetime
import pandas as panda
import matplotlib.pyplot as plt
import fileManipulator

print('starting the analysis. please stand by.')

def prepareJsonArray(filename):
	myContent = fileManipulator.getFileContent(filename)
	if myContent[-1].find(',')!= -1:
		fileManipulator.convertToJsonArray(filename)


def loadJsonArray(filename):
	with open(filename, encoding='utf-8') as dataFile:
		data = json.loads(dataFile.read())
		return data
arrayNames = ['lightData', 'Temp1Data', 'barometerData', 'rainData', 'timeData', 'dateData', 'Temp2Data', 'altitudeData', 'windData', 'humidityData']

lightData = []
Temp1Data = []
barometerData = []
rainData =[]
timeData = []
dateData = []
Temp2Data = []
altitudeData = []
windData = []
humidityData = []
fails = []



def fillWithZeros(indexz):
    print (indexz, len(rainData), len(lightData))
    if (len(lightData)>indexz):
        lightData[indexz]= 0
    else:
        lightData.append(0)
    if (len(Temp1Data)>indexz):
        Temp1Data[indexz]= 0
    else:
        Temp1Data.append(0)

    if (len(barometerData)>indexz):
        barometerData[indexz]= 0
    else:
        barometerData.append(0)

    if (len(rainData)>indexz):
        rainData[indexz]= 0
    else:
        rainData.append(0)

    if (len(timeData)>indexz):
        timeData[indexz]= 0
    else:
        timeData.append(0)

    if (len(dateData)>indexz):
        dateData[indexz]= 0
    else:
        dateData.append(0)

    if (len(Temp2Data)>indexz):
        Temp2Data[indexz]= 0
    else:
        Temp2Data.append(0)

    if (len(altitudeData)>indexz):
        altitudeData[indexz]= 0
    else:
        altitudeData.append(0)

    if (len(windData)>indexz):
        windData[indexz]= 0
    else:
        windData.append(0)

    if (len(humidityData)>indexz):
        humidityData[indexz]= 0
    else:
        humidityData.append(0)

def insertData(data):
	for element in data:
		try:
			lightData.append(int(float(element['LightIntensity'])))
			Temp1Data.append(float(element['Temperature1']))
			barometerData.append(float(element['Barometer']))
			rainData.append(float(element['RainIntensity']))
			dateData.append(element['Date'])
			timeData.append(element['Time'])
			supi = dateData[data.index(element)]+' '+timeData[data.index(element)]
			myDay = datetime.datetime.strptime(supi, '%Y:%m:%d %H:%M:%S')
			timeData[data.index(element)]=myDay
			Temp2Data.append(float(element['Temperature2']))
			altitudeData.append(float(element['Altitude']))
			windData.append(element['WindDirection'])
			humidityData.append(float(element['Humidity']))
		except ValueError:
			print ('there was an error!', data.index(element), element, 'ignoring the element' )
			fillWithZeros(data.index(element))
			fails.append(data.index(element))
#del data[data.index(element)]

def correctTemp1Fails(myArray):
	for element in myArray:
		if element>50:
			print("correcting temp1:",element)
			myArray[myArray.index(element)]=myArray[myArray.index(element)-1]

def correctHumidityDataFails(myArray):
	for element in myArray:
		if element>103:
			print("correcting humidity: ",element)
			myArray[myArray.index(element)]=myArray[myArray.index(element)-1]

def removeFails(myArray):
	print ('fails:',fails)
	for value in fails:
		myArray[int(value)]= myArray[int(value)-1]
		
def printEverything():
    print (len(data),
           len(lightData),
           len(Temp1Data),
           len(barometerData),
           len(rainData),
           len(timeData),
           len(dateData),
           len(Temp2Data),
           len(altitudeData),
           len(windData),
           len(humidityData),
           lightData,
           Temp1Data,
           barometerData,
           rainData,
           timeData,
           dateData,
           Temp2Data,
           altitudeData,
           windData,
           humidityData,
           '\n')

def showMeAPlot(ArrayToShow, filename, range):
		print('generating', filename, 'plot')
		tp = None
		tp = panda.Series(ArrayToShow, index=timeData)
		tp.plot()
	#	plt.ylabel(filename)
	#	plt.xlabel('date')
	#	plt.axis([0,len(ArrayToShow), range[0], range[1]])
	#	plt.savefig(filename+'.png')
		plt.savefig('/var/www/files/'+filename+'.png')
		plt.clf()
		#plt.plot(x,y)



#printEverything()

prepareJsonArray('test.json')
fileManipulator.copyIntoWebServer('myWeData', 'test.json', 'wetterdaten.json')
dataToAnalyze = loadJsonArray('test.json')
insertData(dataToAnalyze)

print ('so many measure data:',len(lightData))

print('removing the fails')
print (fails)

arrayNames = ['lightData', 'Temp1Data', 'barometerData', 'rainData', 'timeData', 'dateData', 'Temp2Data', 'altitudeData', 'windData', 'humidityData']

removeFails(lightData)
removeFails(Temp1Data)
removeFails(barometerData)
removeFails(rainData)
removeFails(timeData)
removeFails(dateData)
removeFails(Temp2Data)
removeFails(altitudeData)
removeFails(windData)
removeFails(humidityData)

correctTemp1Fails(Temp1Data)
correctHumidityDataFails(humidityData)

showMeAPlot(lightData, 'lightPlot',[0,1024])
showMeAPlot(barometerData, 'barometerPlot',[800,1200])
showMeAPlot(Temp1Data, 'temp1Plot', [-50,50])
showMeAPlot(rainData, 'rainPlot', [0, 1500])
showMeAPlot(Temp2Data, 'temp2Plot', [-50,50])
showMeAPlot(altitudeData, 'altiPlot', [200,400])
#showMeAPlot(windData, 'windPlot', [-10,50])
showMeAPlot(humidityData, 'humidityPlot', [0,120])