import json
import sys

#######################################################################################
##This script identifies the number of genes from each species in each orthogroup
###
##sys.argv[1] is species list
##sys.argv[2] is the JSON dictionary of the OrthoFinder Results
##sys.argv[3] is the JSON dictionary with the number of species in each orthogroup
#######################################################################################

with open(sys.argv[1], "r") as f:
	speciesList = [line.split("\t")[0] for line in f.readlines()]
	#print(speciesList)

with open(sys.argv[2], "r") as f:
	for line in f:
		orthofinderDict=json.loads(line)
		#print(orthofinderDict)

geneNameList = []
stringList = []
name_stringDict = {}
species_countDict={}
countDict = {}

for geneName,orthogroupDict in orthofinderDict.items():
	geneNameList.append(geneName)
	for geneList in orthogroupDict.values():
		stringList.append("".join(geneList))

name_stringDict = dict(zip(geneNameList,stringList))

#print(name_stringDict)

for name,string in name_stringDict.items():
	for species in speciesList:
		#x = string.partition(species)
		#print(x)
		if species != "apple":
			species_countDict[species] = string.count(species)
		else:
			species_countDict["apple"] = string.count("apple") - string.count("pineapple")
	#print(name)								#printing them separately works
	#print(species_countDict)
	countDict[name] = dict(species_countDict)	#does this work?
	
print(countDict)

with open(sys.argv[3], "w") as f:
	f.write(json.dumps(countDict))






