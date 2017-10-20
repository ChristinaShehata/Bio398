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
countDict = {}
g = {}

for geneName,orthogroupDict in orthofinderDict.items():
	geneNameList.append(geneName)
	for geneList in orthogroupDict.values():
		for species in speciesList:
			g = {species: geneList.count(species) for species in geneList}	
	newDict[geneName] = g

print(newDict)

#Now, make countDict

#with open(sys.argv[3], "w") as f:
	#json.dump(countDict, f)






