#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 03:15:50 2017

@author: admin
"""
#First, get the number of trips
numTrips = input('Input number of trips')

#Initialize our lists


#For each trip, get the inputs for that trip and place into appropriate list
for i in range(numTrips):
    #For the cash available cast the input to an int and place into its list
    money = int(input('Input Available Cash for This Trip'))
    
    #Ask for the number of ice creams
    numOptions = int(input('Input num options'))
    
    #Ask for input of the costs and split into a reverse sorted list
    tempInput = input('Input Ice Cream Costs')
    costs = sorted(map(int, tempInput.split()), reverse = True)
    
    #Iterate down the list attempting to find another value in the list that
    #adds up to the value in money. Slightly optimize by only starting the 
    #search when we reach the first value that is less than the money that we 
    #have
    for option in range(numOptions):
        
    
    
    
