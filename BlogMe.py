# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 08:11:32 2022

@author: admin
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#Reading Xlsx files
Data = pd.read_excel("articles.xlsx")

#Summary of the data
Data.describe()

#Summary of the columns
Data.info()

#Counting the number of articles per source
#format of groupby: dr.groupby(["column_to_group"])["column_to_count"].count()

Data.groupby(["source_name"])["article_id"].count()

#number of reactions by publisher
Data.groupby(["source_name"])["engagement_reaction_count"].sum()

#Dropping Column
Data = Data.drop("engagement_comment_plugin_count" , axis=1) #must add axis=1 to show you are refering to row.

#Functions in python
def thisFunction() :
    print("This is a function")
    
thisFunction()

#This is a function with variables
def aboutMe(name, surname, location):
    print("This is " + name + ", My Surname is " + surname + ". I am from "+ location+ ".")
    return name, surname, location
    
aboutMe("Emerson", "Mcspadden", "Switzerland")
a = aboutMe("Emerson", "Mcspadden", "Switzerland")

#Using for loops in functions
def favfood(food):
    for x in food:
        print("Top food is " + x )
fastfood = ["burgers" , "pizza" , "pie"]
favfood(fastfood)

# *** Creating a keyword flag
Keyword = "crash"

# Creating a for loop to isolate each title
# length= len(Data)
# Keyword_flag = []
# for x in range(0,length):
#     heading = Data["title"][x]
#     if Keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     Keyword_flag.append(flag)
    
#creating a function

def KeywordFlag(Keyword):
    
    length = len(Data)
    Keyword_flag = []
    for x in range(0, length):
        heading = Data["title"][x]
        try:
            if Keyword in heading:
              flag = 1
            else:
              flag = 0
        except:
            flag = 0
            Keyword_flag.append(flag)
    return Keyword_flag

KeywordFlag = KeywordFlag("murder")
    

#creating a new coulumn in data dataframe

Data["keyword_flag"] = pd.Series("keywordflag")

#setiment analysis Python / subfield mining vader sentiment analysis
#SentimentIntensityAnalyzer 

sent_int = SentimentIntensityAnalyzer() #have to initialize classes first
text = Data["title"][16] #chose the title column, index 16
    
sent = sent_int.polarity_scores(text)

neg = sent["neg"]
pos = sent["pos"]
neu = sent["neu"]

#adding a for loop to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(Data)
for x in range(0,length):
    try:
        text = Data["title"][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent["neg"]
        pos = sent["pos"]
        neu = sent["neu"]
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_pos_sentiment)

Data["title_neg_sentiment"] = title_neg_sentiment
Data["title_pos_sentiment"] = title_pos_sentiment
Data["title_neu_sentiment"] = title_neu_sentiment

#writing the data
Data.to_excel("blogme_clean.xlsx", sheet_name="blogmedata", index=False)
