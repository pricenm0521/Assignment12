# dataFrameThings.py

# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 12
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is an in-class assignment
# Citations: In-Class work on 4/13/2023
# Anything else that's relevant: 

import pandas as pd
import matplotlib.pyplot as plt

def dataFrameWork():
    titanic=pd.read_csv('train.csv')
    # Data Info
    '''
    print(titanic.head())
    print(titanic.columns)
    print(titanic.info())
    print(titanic.describe())
    print(titanic['Sex'].head())
    '''
#    compute and print the counts of each different value in titanic column survival
    survived = titanic["Survived"].value_counts()
    print(survived)
#    one line would look like this
#    print(titanic["Survived"].value_counts())
#    to print with notation
#    no_sum = titanic["Survived"].eq(0).sum()
#    yes_sum = titanic["Survived"].eq(1).sum()
#    print("Didnt survive", no_sum)
#    print("Did survive", yes_sum)

#    bar chart/graph/histogram/frequency graph with frequency counts count on y axis, survived/not survived on x axis
    labels = {1: "Survived", 0: "Not Survived"}
    survived_labels = titanic["Survived"].map(labels)
#   create the histogram
    survived_labels.hist()
#   add lables and a title
    plt.xlabel("Survival Status")
    plt.ylabel("Frequency")
    plt.title("Survival Status of Titanic Passengers")
#   add the numbers at the top of each bar
    ax = survived_labels.hist()
    for rect in ax.patches:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height, height, ha='center', va='bottom')
#   show the histogram
    plt.show()
    
    
#   scatter plot of survived and fare 
#   creates the plot
    plt.scatter(titanic["Survived"], titanic["Fare"])
#   labels everything
    plt.xlabel("Survived")
    plt.ylabel("Fare")
    plt.title("Survival by Fare")
#   shows the plot
    plt.show()
    
    