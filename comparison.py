#!/usr/bin/env python
#This script runs comparisons for the percent of correct gene calls on VDJ Alignment projects packaged into bioboxes. 
#TBI: reprompt after every insertion
#==============================
#Importing relevant modules
import subprocess
#==============================
#name of original simulated data file
inputData = 'simulatedDataFiles/simu-10-leaves-1-mutate.csv'
#==============================
#Create an empty text file that will store the percent of correct gene calls per project
dataFileName = 'dataFile.txt'
dataFile = open(dataFileName, 'w')
dataFile.close()
#==============================
#Asks user for action to be taken
actions = {'1':'Compare current bioboxes', '2':'Add new biobox', '3':'Run projects with new simulated data file'}
print 'The following dictionary displays actions that can be taken'
print actions
index = raw_input('Enter the number corresponding to the action you want to take: ')
#TBI: reprompt if input not in dictionary
action = actions[index]
print 'You have selected: '+action
#==============================
#TBI:
#if action == 'Compare current bioboxes':
	#if data file is empty, print error message and break
	#else parse data file and print comparison   
#==============================
#Adds a new biobox into dataFile.txt, dataFile.txt is basically a dictionary with keys containing the names of the bioboxes and values containing the path to their output directory (not plot performance data)
#NOTE: to add a new biobox, the directory must be in the same directory as this script
if action == 'Add new biobox':
	#enter name of the biobox, run biobox with current data file, return path to plotting data 
	bioboxname = raw_input('Enter the name of the new biobox: ')
	#TBI: if biobox already in directory print message
	#run comparisonRun.sh (should include python script to generate input yaml file), then take in the path output 	
	comparisonRunPath='./'+bioboxname+'/comparisonRun.sh'
	#print comparisonRunPath
	subprocess.call(comparisonRunPath, shell=True)
#==============================
#TBI:
#elif action == 'Run projects with new simulated data file':
	#select which projects to run with new data file, run those projects 
#==============================
print 'PROCESS COMPLETED'
#==============================
