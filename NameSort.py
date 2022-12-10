#Get file from professor
import csv
import time
import numpy
import matplotlib.pyplot as plt

def NameSort(unsorted):
    sorted = [unsorted[0]]
    for i in unsorted[1:]:
        if i > sorted[-1]:
            #If i is bigger than the last element in the sorted portion than add 
            # it to the end of the sorted list.
            sorted = sorted + [i]
        else:    
            #Compare i to each element to the sorted list till you find the element it is less than.
            # Insert it into list and break for loop to go back to outer loop. 
            for j in range(0,len(sorted)):
                if i<sorted[j]:
                    sorted = sorted[:j] + [i] + sorted[j:]
                    break
    return sorted

    




    