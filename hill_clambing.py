# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:59:31 2018

@author: Lena Aleksandrova
"""

import csv

import numpy

import random

import time
#read and open data 
with open("european_cities.csv", "r") as f:
    data = list(csv.reader(f, delimiter=';'))
    
array=[0,1,2,3,4,5,6,7,8,9,10]
t1 = time.time()
# evaluating distance between two cites and find total distance 
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

# mutate permutation and find the best permutation with the shortest distance 
def mutatePermutations(permutat, distan_matrix):
    best_permutat = permutat
    num = len(permutat)
    distance_permutat = evaluation(permutat, distan_matrix) 
    for i in range(len(permutat)):
        start = random.sample(range(num), 2)
        k = start[0]
        f = start[1]
        new_permutat = permutat.copy()
        new_permutat[k],new_permutat[f] = new_permutat[f],new_permutat[k]
        
        nabo = evaluation(new_permutat,distan_matrix)
        if nabo < distance_permutat:
             best_permutat = new_permutat
             break
        else:
            pass
    return best_permutat 


matrix2=data[1:][:]

     
#
def hillClambing(array, matrix2):
    randomize_array = array[:]  
    random.shuffle(randomize_array)
    best_mutation = mutatePermutations(randomize_array, matrix2)
    isbetter = True
    while isbetter:
        best_mutation = mutatePermutations(array, matrix2)
        if best_mutation == array:
            isbetter = False
        else:
            array = best_mutation
            distance = evaluation(best_mutation, matrix2)
            return best_mutation, distance
#array with the best mutation with the best distances        

beste_mutations = []
distances = []
# running 20 times every time finding the best distance and combinations which is sent to empty list
for i in range(0,20):
    
    best_mutation1,distance1 = hillClambing(array,matrix2)
    beste_mutations.append(best_mutation1)
    distances.append(distance1)
    
t2 = time.time()    
print ("The best permutation is")
print(beste_mutations)
print("The best distance is ")
print(distances)
# average of all the best distances 
total_average = numpy.average(distances)
best_distance = min(distances)
worst_distance = max(distances)
total_time = t2 - t1
print("The worst distance after 20 runs is")
print(worst_distance)
print("The best distance after 20 runs is")
print(best_distance)
print("Total average is ")
print(total_average)
print("Total run time")
print(total_time)



    
    


    