#!/usr/bin/env python
#8-20-15
#This script runs comparisons for the percent of correct gene calls on VDJ Alignment projects packaged into bioboxes. 
#TBI: reprompt after every insertion
#==============================
#Importing relevant modules
import subprocess
import os
import csv
import sys
import operator
#==============================
#This function parses the data file and stores the information collected into a dictionary
def parseFile(dataFile, dataDict):
	#if data file is not empty parse it 
	if os.stat(dataFileName).st_size != 0:
		with open(dataFileName) as file:
			for line in file:
				line = line.rstrip()
				temp=line.split(':')
				dataDict[temp[0]] = temp[1]
#==============================
#returns percentages and error from csv files in dictionary format
def getCSV(paths):
	#dictionary containing the percentage value and margin of error per biobox
	percentages = {}
	for biobox in paths:
		csvfile=paths[biobox]
		#parse csv file		
		with open(csvfile) as file:
			reader = csv.DictReader(file, delimiter=',')	
			for row in reader:
				if row['bin_low_edge']=='-0.5':
		        		percentages[biobox]=row['contents']+','+row['binerror']	
	#the values are in the string format 'contents,binerror' (i.e. 1.0,0.005450822838987679)
	return percentages
#==============================
#output to a file the rank, name of biobox and percentage of bin error for each biobox in the input dictionary
def compare(csvDict):
	sortedList=sorted(csvDict.items(), key=operator.itemgetter(1)) 		
	file = open('results.txt', 'w')
	for i in sortedList:
		print>>file, i
	file.close()					
#==============================
#name of original simulated data file
inputData = 'simulatedDataFiles/simu-10-leaves-1-mutate.csv'
#dictionary to hold info from dataFile
dataDict = {}			 
#Create an empty text file that will store the paths to the output plot directory
dataFileName = 'dataFile.txt'
dataFile = open(dataFileName, 'w')
dataFile.close()
parseFile(dataFile, dataDict)
#==============================
#Asks user for action to be taken
actions = {'1':'Compare current bioboxes', '2':'Add new biobox', '3':'Run projects with new simulated data file'}
print 'The following dictionary displays actions that can be taken: '
print actions
index = raw_input('Enter the number corresponding to the action you want to take: ')
#TBI: reprompt if input not in dictionary
action = actions[index]
print 'You have selected: '+action
#==============================
#Looks at the plot performance of each biobox (percent v, d, and j correct)
if action == 'Compare current bioboxes':
	#if data file is empty, print error message and break
	if os.stat(dataFileName).st_size == 0:
		sys.exit('There are no bioboxes currently listed in '+dataFileName)
	#else compare percentages located in dataDict dictionary
	else:
		#dictionary containing names of bioboxes and paths to csv files
		paths = {}
		#add names of bioboxes to dictionary
		for biobox in dataDict:
			paths[dataDict[biobox]] = ''	
		#add name of csv file of gene to compare to end of path to plot direcotry
		percentagesToCompare = {1:'v_gene', 2:'d_gene', 3:'j_gene'}
		print 'The following dictionary displays the types of comparisons possible'
		print percentagesToCompare
		percentToCompare = percentagesToCompare[raw_input('Pick the number corresponding to a percentage to compare')]+'.csv'			
		for biobox in paths:
			paths[biobox]+=percentageToCompare
		#compare the csv files	
		percentages=getCSV(paths)
		#output results in sorted order to file
		compare(percentages)
#==============================
#Adds a new biobox into dataFile.txt, dataFile.txt is basically a dictionary with keys containing the names of the
#bioboxes and values containing the path to their output directory (plot performance data)
#NOTE: to add a new biobox, the directory must be in the same directory as this script
elif action == 'Add new biobox':
	#enter name of the biobox, run biobox with current data file, return path to plotting data 
	bioboxname = raw_input('Enter the name of the new biobox: ')
	#TBI: if biobox already in directory print message
	comparisonRunPath='./'+bioboxname+'/comparisonRun.sh'
	#TBI: pass in dataFileName as parameter
	#calls the shellscript that will ask for parameters to generate an input yaml file, run the docker image, and run plot performance
	subprocess.call(comparisonRunPath, shell=True)
#==============================
#TBI: run projects with new simulated file
#elif action == 'Run projects with new simulated data file':
	#select which projects to run with new data file, run those projects 
#==============================
print 'PROCESS COMPLETED'
#==============================

