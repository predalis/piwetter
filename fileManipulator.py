#!/usr/bin/env python
# Filename: fileManipulation.py

# returns the content of the file
def getFileContent(filename):
	myFile = open (filename, 'r')
	current = myFile.readlines()
#	print('file content:', current)
	myFile.close()
	return current

#adds at the beginning of a file
def addToFileBeginning(toAdd, filename):
	current = getFileContent(filename)
	current.insert(0, toAdd)
	myFile = open(filename, 'w')
	current = "".join(current) #copy the list content into a string object
	myFile.write(current)
	myFile.close()

def removeLastComma(listOfStrings):
	str = listOfStrings[-1]
	str = str.replace(',', '')
	listOfStrings[-1] = str
	return listOfStrings
	
def addToFileEnd(toAdd, filename):
	current = getFileContent(filename)
	current = removeLastComma(current)
	print (current[-1])
	current.insert(len(current), toAdd)
	myFile = open(filename, 'w')
	current = "".join(current) #copy the list content into a string object
	myFile.write(current)
	myFile.close()

def convertToJsonArray(filename):
	addToFileBeginning('[', filename)
	addToFileEnd(']', filename)	

def copyIntoWebServer(varname, filename, newFilename):
	newVarname = "var "+varname+"= "
	current = getFileContent(filename)
	current.insert(0, newVarname)
	myFile = open('/var/www/files/'+newFilename, 'w')
	current = "".join(current) #copy the list content into a string object
	myFile.write(current)
	myFile.close()
	
def getFileInfos(filename):
	myFile=open(filename, 'r+')
	print ('filename:', myFile.name) 
	print ('this is my Filemode:', myFile.mode)
	print ('current position:', myFile.tell())
	if myFile.tell()>1:
		print('going back to beginning')
		myFile.seek(0,0)
	myFile.write("hello Python")
	print ('first in the file:', myFile.read(1), '\ncurrent position:', myFile.tell(), '\nfileno:', myFile.fileno())

	myFile.close()
	print ('is the file closed?: ',myFile.closed)

