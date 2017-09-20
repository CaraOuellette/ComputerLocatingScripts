#!/usr/bin/env python
"""
SCRIPT FOR ASSOCIATING DOMAINS/NAMES/IPS WITH A LOCATION
LOCATION FIELS ARE GENERATED EACH TIME, LOOK INTO SERIALIZATION
SWITCH STATEMENT FOR DOMAIN COMPARISON IS CLUNKY, LOOK INTO CONFIG FILE

so it works from the command line...who knows here
TODO: figure out how to export the script...
"""
import os
import configparser
import csv
from LocationAssociation import *


# reading from config.ini
path = 'LocationAssociation\\'
config = configparser.ConfigParser()
config.read('data\\config.ini')
readpath = config['READING']['Path']
writefileL = config['WRITING']['LocatedExtension']
writepathL = config['WRITING']['Located']
writefileU = config['WRITING']['UnlocatedExtension']
writepathU = config['WRITING']['Unlocated']
locationfile = config['READING']['Locationfile']
loglocation = config['WRITING']['Logs']

if __name__ == '__main__':
    # building folders - this could be done with a method
    # should also get this folder creation to be logged
    folders = os.listdir()
    if readpath in folders:
        print("The readpath is in folders: " + str(readpath in folders))
        print("See?")
        print(folders)
        reportfiles = os.listdir(readpath)
    else:
        os.mkdir(readpath)
        print('A folder for unprocessed reports was created.')
        reportfiles = []
    if not writepathL in folders:
        os.mkdir(writepathL)
        print('A folder for located computers was created.')
    if not writepathU in folders:
        os.mkdir(writepathU)
        print('A folder for unlocated computers was created.')
    if not loglocation in folders:
        os.mkdir(loglocation)
        print('A folder for log files was created.')

    # opening already read reports
    processedreportfile = open('data\\' + config['DEFAULT']['Processed'],'r+')
    processedreports = processedreportfile.read().split('\n')
    locations = ImportTools.ImportTools.read_Locations('data\\' + locationfile)
    for file in reportfiles:
        if ".csv" in file and not file in processedreports:
            # reading the report file
            computers = ImportTools.ImportTools.read_Computers('Unsorted\\' + file)
            # initializing variables
            located = []
            IPlocated = []
            mysteries = []
            supermysteries = []
            charDict = {}
            sum1 = 0
            # locating by domain / name
            for comp in computers:
                if AssociationTool.AssociationTool.compareByDomain(comp, locations):
                    located.append(comp)
                else:
                    mysteries.append(comp)
            print("A total of " +
                  str(len(located) + len(mysteries)) + " computers were processed.")
            print(str(len(located)) +
                  " were located successfully by domain and naming convention.")
            print("The remaining computers will now be sorted by IP.")
            # locating by ip
            for comp in mysteries:
                if not comp.IP == [0, 0, 0, 0]:
                    for loc in locations:
                        AssociationTool.AssociationTool.compareByIP(comp, loc)
                    if comp.location == "" or comp.location == "Unknown":
                        supermysteries.append(comp)
                    else:
                        IPlocated.append(comp)
                else:
                    supermysteries.append(comp)
            print("Out of the remaining " + str(len(mysteries)) + " computers, " +
                  str(len(IPlocated)) + " more were located via IP.")
            print('Writing located computers to file ' + writepathL +
                  "\\"+ writefileL + file)
            # writing files - located computers
            ImportTools.ImportTools.write_Computers(located + IPlocated, writepathL +
                                                    "\\" + writefileL + file)
            print('Writing still unlocated computers to file ' + writepathU +
                          "\\"+ writefileU + file)            
            # writing files - unlocated computers
            ImportTools.ImportTools.write_Computers(supermysteries, writepathU +
                                                    "\\" + writefileU + file)
            # adding processed report to list
            processedreportfile.write(file+"\n")
            print("The names among unlocated computers" +
                  " will be computed, by 5 character string.")
            #documenting weird names. this could be written somewhere too.
            for comp in supermysteries:
                if comp.name[0:5] in charDict.keys():
                    val = charDict[comp.name[0:5]]
                    charDict[comp.name[0:5]] = val + 1
                else:
                    charDict[comp.name[0:5]] = 1
            for key in sorted(charDict.keys()):
                print(str(key.encode('ascii', 'ignore'))[2:-1] + ": " + str(charDict[key]) + "\n")
                sum1 += charDict[key]
            print("These names represent " + str(sum1) + " names out of " +
                  str(len(supermysteries)) + ".")
            ImportTools.ImportTools.writeLog(file,
                                            writefileL + file,
                                            writepathL, writefileU + file,
                                            writepathU, loglocation)
    processedreportfile.close()
    print("This concludes the script. Press any key to exit.")
    input()
