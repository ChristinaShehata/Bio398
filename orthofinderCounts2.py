import json
#get counts of genes for each species in each orthogroup
#dictionary with keys of gene names and values are dictionaries with keys of orthogroup IDs and values of gene names

with open("/Users/ChristinaShehata/Desktop/species_list.txt", "r") as f:
	speciesList = [line.split("\t")[0] for line in f.readlines()]
	#print(speciesList)

with open("/Users/ChristinaShehata/Desktop/GOIorthofinderGroups.json", "r") as f:
	for line in f:
		orthofinderDict=json.loads(line)
		#print(orthofinderDict)

sepList = []
name_listDict = {}
geneNameList = []
species_lengthDict = {}
lenList = []
countDict = {}
newList = []
counts_for_all = []
indList = []
newDict = {}
NewgeneList = []
countList = []
g = {}
countDict0 = {}
counts = {}


for geneName,orthogroupDict in orthofinderDict.items():
	geneNameList.append(geneName)
	for geneList in orthogroupDict.values():
		#counts[species] = 0
		for species in speciesList:
			g = {species: geneList.count(species) for species in geneList}	
	newDict[geneName] = g

#print(counts)
print(newDict)

for value in newDict.values():
	for speciesNum,count in newDict.items():
		for species in speciesList:
			if species in speciesNum: ##then add the values together of those keys
				countDict0=0
				#counts = filter
			#countDict0 = {species:  for species in speciesNum}

#print(counts)
#print(countDict0)
	#for i,gene in enumerate(geneList):
			

#for species in speciesList:

			#sepList.append(list(filter(lambda x: species in x,geneList)))
	#name_listDict[geneName] = sepList
	
#print(List1) #This is a list the complete gene lists



	#for item in sepList:
			#if item[0] in geneList:
				#newList.append(item)
	#
	#break

#print(name_listDict)
	
#for key, value in name_listDict.items():
	#for lst in value:
		#if lst in name_listDict[key]:
			#newList.append(lst)



#print(counts_for_all)
#print(sepList)

#print(newList)

#for orthogroupDict in orthofinderDict.values():
#	for geneList in orthogroupDict.values():
#		for toop in newList:
#			toop1 = toop[1]
#			if toop1[0] in geneList:
#				List1.append(toop)

#print(List1)
#print(newDict)
#print(name_listDict)

#for value in name_listDict.values():
	#for lst in value:
		#lenList.append(len(lst))

#species_lengthDict = dict(zip(speciesList,lenList))

#print(species_lengthDict)

#for name in geneNameList:	
	#countDict[name] = species_lengthDict

#print(countDict)

with open("/Users/ChristinaShehata/Desktop/orthofinderCounts.json", "w") as f:
	json.dump(countDict, f)









#countDict = {len(item):item for item in sepList}	

			#for item in sepList:
			#	countDict[species] = len(item)

#print(countDict)

	
		
#countDict = {len(item):item for item in sepList}


		
		
		
		#for i in item:
			#if species in i:
			#	countDict[species] = len(item)
			#	print(countDict)
			
				#if any(species in gene for gene in geneList):
					#print(geneList.count(species))
	
	
	
	
	
	#TheList = [s for s in geneList if any(species in s for species in speciesList)]
	
	
	
	
	
	#	listOfLists.append(geneList)

#for list in listOfLists:
	#for gene in list:
	#	if "amaranth" in gene:
	#		amaranthList.append(gene)
			
#print(amaranthList)
	
		
		

#def speciesCount(geneList):
	#for gene in geneList:
		#if "amaranth" in gene:
			#countList.append(gene)
			#return countList
		#for gene in geneList:
			
			#if gene.startswith("apple"):
				#print(gene)
				#speciesDict["apple"] = geneList.count(gene)
				
#[ unicode(x.strip()) if x is not None else '' for x in row ]
				
#print(speciesDict)
	#countDict[geneName] = 
	
	#	for gene in geneList:
	#		if gene.startswith("apple"):
	#			print(gene)
		
		#for i in v:
		#	if i.startswith("apple"):
			#	print(key + " is the gene name. " + i + " is an apple gene in the same orthogroup.")
			#	print(k + " is the orthogroup" + "\n")






