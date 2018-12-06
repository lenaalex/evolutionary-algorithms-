# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import time 

import itertools 
#exhaustive search  
#read and open data 
with open("european_cities.csv", "r") as f:
    data = list(csv.reader(f, delimiter=';'))
#array is the parmutation (6 cites)

#number of cites takes inside n and how mange steps 
#function to evaluate distance between two cites and return total amount cites   
def evaluation(permutat, distan_matrix):
    total=0
    for i in range (len(permutat)):
        if i ==(len(permutat)-1):
            city1 = permutat[i]
            city2 = permutat[0]
        else:
            city1=permutat[i]
            city2=permutat[i+1]
        dist_cities=distan_matrix[city1][city2]
        total+= float(str(dist_cities))
    return total

def printcities(cities):
    res=""
    for i in cities:
        res+=data[0][i]+" "
    print (res)

#deleting the strings in data   
matrix2=data[1:][:]
# generating different combinations of permutation and makeing list of this combinations. 
array=[0,1,2,3,4,5,6]      
t1=time.time()
generate = itertools.permutations(array)
permutation=list(generate)
#print(permutation)
# in this for loops choosing the permutation with shortest distance   
smallest = 10000000000
short_permut = []
for i in permutation:
    distanse = evaluation(i,matrix2)
    if distanse < smallest:
        smallest = distanse 
        short_permut = i


print("Sequence of 6 cities with shortest tour:")
printcities(short_permut)
        
t2=time.time()
total = t2 - t1
print ("The shortest permutation is ")
print(short_permut)
print ("The shortest distance between cites is")
print(distanse)
print("Total time takes")
print (total)


array=[0,1,2,3,4,5,6,7,8,9,10]      
t3=time.time()
generate1 = itertools.permutations(array)
permutation1=list(generate1)
#print(permutation)
# in this for loops choosing the permutation with shortest distance   
smallest1 = 10000000000
short_permut1 = []
for i in permutation1:
    distanse1 = evaluation(i,matrix2)
    if distanse1 < smallest1:
        smallest1 = distanse1 
        short_permut1 = i


print("Sequence of 10 cities with shortest tour:")
printcities(short_permut1)
        
t4=time.time()
total1 = t4 - t3
print ("The shortest permutation is ")
print(short_permut1)
print ("The shortest distance between cites is")
print(distanse1)
print("Total time takes")
print (total1)



  

    