# Author: Christine Vu
# File:   Clustering.py
# Usage: 'python Clustering.py <numberofClusters> <textFile.txt>''
# Date:   May 9th, 2016
# 
#
# Description:
#     Sorts points into clusters.
#     Outputs graph of points; clusters
#     are visually separable by colors!
#****************************************************************   





#computes euclidean distance between two...
#...coodinate points
def euclideanDistance(point, centroid):
	import math 

	xDiffSq = point[0] - centroid[0]
	xDiffSq = xDiffSq**2
	yDiffSq = point[1] - centroid[1]
	yDiffSq = yDiffSq**2

	SUM = xDiffSq + yDiffSq
	distance = math.sqrt(SUM)
	return distance




#computes which centroid is closest to a point
def closestPoint(point, centroids):
	distances = []
	for i in centroids:
		dist = euclideanDistance(point, i)
		distances.append(dist)

	#print ("Distances: ", distances)
	shortest = min(distances)
	#print ("Shortest: ", shortest)
	closest = centroids[distances.index(shortest)]
#	print ("Closest: ", closest)

	return closest



def newCentroids(clusters, centroids):
	for i in clusters:
	#	print ("CLUSTER: ", i)
		sumX = 0
		sumY = 0
		for j in clusters[i]:
		#	print(j)
			sumX += j[0]
			sumY += j[1]

		averageX = sumX
		averageY = sumY
		if (len(clusters[i]) != 0):
			averageX = sumX/len(clusters[i])
			averageY = sumY/len(clusters[i])
		#	print ("averageX: ", averageX)
		#	print ("averageY: ", averageY)
			centroids[i][0] = averageX
			centroids[i][1] = averageY

	return centroids



def clearClusters(clusters):
	for i in clusters:
		clusters[i] = []
	return clusters



def printClusters(clusters, centroids):
	import numpy as np
	import matplotlib.pyplot as plt
	import matplotlib.cm as cm
	import itertools

	plotClustersX = []	
	plotClustersY = []	

	for i in clusters:
		plotClustersX.append([])
		plotClustersY.append([])

		for j in clusters[i]:
			plotClustersX[i].append(j[0])
			plotClustersY[i].append(j[1])

	print (plotClustersX)		
	print (plotClustersY)	


	colors = itertools.cycle(["r", "b", "g", "c", "m", "y", "k"])

	import pylab
	for i in clusters:
		x = plotClustersX[i]
		y = plotClustersY[i]
		pylab.plot(x,y,'bo',color=next(colors))
		for i in centroids:
			x = i[0]
			y = i[1]
			pylab.plot(x,y,'bo',color="white")
	pylab.show()


def getRange(points):
	allPoints = []
	for i in range(len(points)):
		allPoints.append(points[i][0])
		allPoints.append(points[i][1])

	MAX = max(allPoints)
	MIN = min(allPoints)
	return MIN, MAX	

def main():
	import sys
	import random
	import math
	import copy

	#getting data from command line
	inputFile = str(sys.argv[2])
	k = str(sys.argv[1])
	k = int(k)
	print (inputFile)
	print (k)

	f = open(inputFile, "r")

	#list to put points into for now
	points = []

	#get points, convert them to int, 
	#and put them into points list
	for point in f:
		tempPoint = point.split(",")
		tempPoint[0] = int(tempPoint[0])
		tempPoint[1] = int(tempPoint[1])
		points.append(tempPoint)


	print (points)
	MIN, MAX = getRange(points)
	print ("MIN: ", MIN)
	print ("MAX: ", MAX)


	clusters = dict()

	#this alias will be compared to the clusters dictionary
	#The comparison will determine if any points change..
	#..cluster membership
	#Until there is no change in cluster membership,...
	#...algorithm will stop 
	clustersAlias = dict()

	#
	centroids = []
	for i in range(k):

		#generate 2 random points for the 
		#coordinates for the centroids
		generatedPoint = []

		#x
		randPoint = random.randint(MIN,MAX)
		generatedPoint.append(randPoint)

		#y
		randPoint = random.randint(MIN,MAX)
		generatedPoint.append(randPoint)

		centroids.append(generatedPoint)


		clusters[i] = []
		clustersAlias[i] = []

	print ("Centroids: ", centroids)
	print ("Clusters: ", clusters)




	

	#sorting into clusters
	for i in points:
	#	print (i)
		closestCentroid = closestPoint(i, centroids)
		clusters[centroids.index(closestCentroid)].append(i)
	print ("HIIIII: ",clusters)

	h = 0;

	while (clusters != clustersAlias):
		print ("CLUSTER = CLUSTERALIAS??")
		print (clusters, " == ", clustersAlias)
		print ("ITERATION NUMBER: ", h)
		clustersAlias = copy.deepcopy(clusters)
		centroids = newCentroids(clusters, centroids)
	#	print (centroids)
		h += 1
		clusters = clearClusters(clusters)
		print ("CLUSTER: ", clusters)
		print ("CLUSTERSALIAS: ", clustersAlias)

		#re-calculate the closest centroid for each point
		for i in points:
			closestCentroid = closestPoint(i, centroids)
			clusters[centroids.index(closestCentroid)].append(i)

	printClusters(clusters, centroids)






main()