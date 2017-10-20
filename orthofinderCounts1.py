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
sepList = []
name_listDict = {}
species_lengthDict = {}
lenList = []
countDict = {}

for geneName,orthogroupDict in orthofinderDict.items():
	geneNameList.append(geneName)
	for geneList in orthogroupDict.values():
		for species in speciesList:
			sepList.append(list(filter(lambda x: species in x,geneList)))
	`name_listDict[geneName] = sepList
		#break

print(name_listDict)

for value in name_listDict.values():
	for lst in value:
		lenList.append(len(lst))

species_lengthDict = dict(zip(speciesList,lenList))

for name in geneNameList:	
	countDict[name] = species_lengthDict

#print(countDict)

with open(sys.argv[3], "w") as f:
	json.dump(countDict, f)






