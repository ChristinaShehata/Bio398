import sys
import json
import re
import csv

#######################################################################################
## This script identifies the number of genes from each species in each orthogroup
##
## sys.argv[1] is species list
## sys.argv[2] is the JSON dictionary of the OrthoFinder Results
## sys.argv[3] is the csv file with the number of species in each orthogroup
#######################################################################################

def make_species_list():
	with open(sys.argv[1], "r") as f:
		speciesList = [line.split("\t")[0] for line in f.readlines()]
	return speciesList

def make_count_dict(speciesList):
	with open(sys.argv[2], "r") as f:
		for line in f:
			orthofinderDict = json.loads(line)

	name_speciesDict = {}
	species_countDict = {}
	countDict = {}

	for geneName, orthogroupDict in orthofinderDict.items():
		for geneList in orthogroupDict.values():
			species_list = [re.sub("\d", "", i) for i in geneList]
			name_speciesDict[geneName] = species_list

	for key, lst in name_speciesDict.items():
		for species in speciesList:
			species_countDict[species] = lst.count(species)
			species_countDict["total"] = len(lst)
			countDict[key] = dict(species_countDict)
	return countDict

def main():
	speciesLst = make_species_list()
	countDict = make_count_dict(speciesLst)
	with open(sys.argv[3], "w") as f:
		gene = countDict.keys()
		for dict in countDict.values():
			writer = csv.DictWriter(f, fieldnames=dict.keys())	
		writer.writeheader()
		for dict in countDict.values():
			writer.writerow(dict) ##Now just add column of gene Names 
	
main()






