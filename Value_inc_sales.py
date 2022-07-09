# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:47:02 2022

@author: admin
"""

import pandas as pd
data = pd.read_csv("transaction.csv") 
data = pd.read_csv("transaction.csv", sep=";")

# summary of the data
data.info()
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau
ProfitPerItem = 21.11 - 11.73   
# CostPerTransaction = CostPerITem * NumberofItemsPurchased

#variable = dataframe["column_name"]

CostPerItem = data["CostPerItem"]
NumberofItemsPurchased = data["NumberOfItemsPurchased"]

CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding column to data frame
data["CostPerTransaction"] = data["CostPerItem"] * data["NumberOfItemsPurchased"]

#sales per tansaction
data["SalesPerTransaction"] = data["SellingPricePerItem"] * data["NumberOfItemsPurchased"]
#profit calculation = sales - cost
data["ProfitPerTransaction"] = data["SalesPerTransaction"] - data["CostPerTransaction"]

data["Markup"] = (data["SalesPerTransaction"] - data["CostPerTransaction"] )/ data["CostPerTransaction"]
#Rounding Markup
RoundMarkup = round(data["Markup"], 2)
data["Markup"] = round(data["Markup"], 2)

#Combining Date fields, concatonation
My_name = "Emerson" + "Mcspadden"
My_Date = "Day"+"-"+"Month"+"-"+"Year"
#Checking columns in data type
print(data["Day"].dtype)

#Change Columns Type
Day = data["Day"].astype(str)
Year = data["Year"].astype(str)
print(Day.dtype)
My_Date = Day + "-"+data["Month"]+"-"+Year
data["Date"] = My_Date

#using iloc to view specific Columns/rows
data.iloc[0] #views the row with index = 0 can do range here [0:5] can do last five [-5:]
data.head(5) #bings in the first 5 rows
data.iloc[:,2] #brings in all columns starts at 0 in python. 
data.iloc[4,2]# brings in 4th row, 2nd column

#splitting the column into more than one field using split
#spit_var = column.str.split("sep" , expand= True)

split_col = data["ClientKeywords"].str.split(",", expand=True)

#create three new columns, because of the split in ClientKeywords
data["ClientAge"] = split_col[0]
data["ClientType"] = split_col[1]
data["LengthofContract"] = split_col[2]

#using the replace function, taking the brackets out of columns
data["ClientAge"] = data["ClientAge"].str.replace("[", "")
data["LengthofContract"] = data["LengthofContract"].str.replace("]","")
data["ClientAge"] = data["ClientAge"].str.replace("'","")
data["ClientType"] = data["ClientType"].str.replace("'","")
data["LengthofContract"] = data["LengthofContract"].str.replace("'","")


#use the lower function to change item to lowercase
data["ItemDescription"] = data["ItemDescription"].str.lower()

#Merging files, data sets, Joining.
#erge_dataframe = pd.merge(dataframe_old, dataframe_new, on = "key")

#bringing in a new dataset
NewData = pd.read_csv("value_inc_seasons.csv", sep = ";")

data = pd.merge(data, NewData, on = "Month")

#droping columns 
#df = df.drop("columnname" , axis = 1) 1 is column, 0 = row 
data = data.drop("ClientKeywords", axis=1)
data = data.drop("Day", axis=1)
data = data.drop("Year", axis = 1)
data = data.drop("Month", axis = 1)

#drop multiple columns
#ata = data.drop(["year", "month"] , axis =1)


#exporting into CSV


data.to_csv("ValueInc_Cleaned.csv", index = False)