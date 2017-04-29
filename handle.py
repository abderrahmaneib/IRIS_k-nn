import csv
import math
import operator
import random
import os

#first handle the data : we load it then we set our traning and test sets
def loadDataset(trainingset=[],testset=[]):
	with open("iris.data.txt",'rb') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
		for i in range (len(dataset)-1):
			for j in range(4):
				dataset[i][j]=float(dataset[i][j])
			if random.random()<0.66:
				trainingset.append(dataset[i])
			else:
				testset.append(dataset[i])


#how we gonna measure the similarity...
def euclidianDistance(elt1,elt2,longueur):
	d=0
	for i in range(len(elt1)-1):
		d+=pow(elt1[i]-elt2[i],2)
	return math.sqrt(d)
#getting the k closest neighbors
def getNeighbors(trainingset,elt,k):
	neighborhood=[]
	for i in range (len(trainingset)):
		distance=euclidianDistance(trainingset[i],elt,4)
		neighborhood.append((trainingset[i],distance))
	neighborhood.sort(key=operator.itemgetter(1))
	neighbors=[]
	for i in range(k):
		neighbors.append(neighborhood[i][0])
	return neighbors
#classifying the sample according the neighbors 
def getResponse(neighbors):
	classVotes={}
	for i in range(len(neighbors)):
		classe=neighbors[i][-1]
		if classe in classVotes:
			classVotes[classe]+=1
		else:
			classVotes[classe]=1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

#get the accuracy
def getAccuracy(testset,predictions):
	vrais=0
	for i in range(len(testset)):
		if testset[i][-1] == predictions[i]:
			vrais+=1
	return (vrais/float(len(testset))*100.0)

def main():
	trainingset=[]
	testset=[]
	k=3
	loadDataset(trainingset,testset)
	print "data loaded \n"
	predictions=[]
	for i in range(len(testset)):
		neighbors=getNeighbors(trainingset,testset[i],k)
		result=getResponse(neighbors)
		predictions.append(result)
	accuracy=getAccuracy(testset,predictions)
	plante=[]
	sl=float(input("enter the sepal length...."))
	plante.append(sl)
	sw=float(input("enter the sepal width..."))
	plante.append(sl)
	pl=float(input("enter the petal length..."))
	plante.append(pl)
	pw=float(input("enter the petal width..."))
	plante.append(pw)

	planteNeighbors=getNeighbors(trainingset,plante,k)
	plantResult=getResponse(planteNeighbors)
	print "your plant is a ",result,"with",accuracy,"of accuracy"


main()























