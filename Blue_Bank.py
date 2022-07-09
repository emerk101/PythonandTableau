# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 12:25:15 2022

@author: admin
"""

import json
import pandas as pd
import numpy as np  #We will use often for linear algebra, arras, etc.
import matplotlib.pyplot as plt

#Method 1 to read json data
json_file = open("loan_data_json.json")
data = json.load(json_file)

#Another method for loading json data
with open("loan_data_json.json") as json_file:
    data = json.load(json_file)

#Transform to dataframe

LoanData = pd.DataFrame(data)

#Finding unique values for the purpose column
LoanData["purpose"].unique()

#Describe Data
LoanData.describe()

LoanData["int.rate"].describe()
LoanData["fico"].describe()
LoanData["dti"].describe()

#Using exp() to get annual income
Income = np.exp(LoanData["log.annual.inc"])
LoanData["annualincome"] = Income

#Arrays, data structure that stores data, they are ordered, and able to store non unique items. Have to be declared!
#1D Array
Arr = np.array([1,2,3,4])

#0D array
Arr = np.array(43)

#2D Array
Arr = np.array([[1, 2, 3,],[4, 5, 6]])

#Using If statements
A = 40
B = 500
C = 1000

if B > A:
    print("B is Greater Than A")
    
#More Conditions  
#And and or is interchangable

if B > A and B < C: 
    print("B is Greater Than A But Less Than C")
    
#When Condition Is Not Met?

A = 40
B = 500
C = 20

if B > A and B < C:
    print("B is Greater Than A But Less Than C")
else:
    print("It is Not")
    
    
#Another Condition, Different Metrics 
A = 40
B = 0
C = 30

if B > A and B < C:
    print("B is Greater Than A But Less Than C")
elif B > A and B > C:
    print("B is Greater Than A and C")
else:
    print("No Conditions Met")
    
    
#Fico Score
Fico = 200
# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good
# fico >=780: 'Excellent'

if Fico >= 300 and Fico < 400:
    ficocat = "Very Poor"
elif Fico >= 400 and Fico < 600:
    ficocat = "Poor"
elif Fico >= 601 and Fico < 660:
    ficocat = "Fair"
elif Fico >= 660 and Fico < 780:
    ficocat = "Good"
elif Fico >= 780:
    ficocat = "Excellent"
else:
    ficocat = "Uknown"

print(ficocat)
    

#For Loops

fruits = ["apple", "pear", "banana", "cherry"]

for x in fruits:
    print(x)
    y = x + " Fruit"
    print(y)
    
#Loops based on Position

for x in range(0,3):
    y = fruits[x]
    print(y)
    
    
#applying for loops to loan data

#using first 10
length = len(LoanData) #finds the lenght of rows and columns
ficocat = []

for x in range(0,length):
    category = LoanData["fico"][x]
    if category >= 300 and category < 400:
        cat = "Very Poor"
    elif category >= 400 and category < 600:
        cat = "Poor"
    elif category >= 601 and category < 660:
        cat = "Fair"
    elif category >= 660 and category < 700:
        cat = "Good"
    elif category >= 700:
        cat = "Excellent"
    else:
        cat = "Unknown"
        
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

LoanData["fico.category"] = ficocat

#while loops

I = 1
while I > 10:
    print(I)
    I = I +1
    
    
#df.loca as conditional statements
# df.loc[df[columnname] conddtion, newcolumname] = "value if the condition is met"

#New column for interest rates if rate is > 0.12 then high, else low.

LoanData.loc[LoanData["int.rate"] > 0.12, "int.rate.type"] = "High"
LoanData.loc[LoanData["int.rate"] <= 0.12, "int.rate.type"] = "Low"

#Number of loans/rows by fico.category

catplot = LoanData.groupby(["fico.category"]).size()
catplot.plot.bar() #please plot bar chart from our variable catplot()
plt.show()
#Changing colors
#catplot.plot.bar(color = "green", width = 0.1)


Purpplot = LoanData.groupby(["purpose"]).size()
Purpplot.plot.bar(color = 	(1,0,1) , width = 0.5) #can use rgb but not hex, only rgb 0-1
plt.show()

#Scatter Plots, you always need an X and a Y

xpoint = LoanData["annualincome"]
ypoint = LoanData["dti"]
plt.scatter(xpoint, ypoint, color ="#4caf50", linewidths = 0.1)
plt.show()

#Writing to csv
LoanData.to_csv("loan_cleaned.csv", index = True)