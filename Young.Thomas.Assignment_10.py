'''
File: Young.Thomas.Assignment-3
Name: Thomas Young
Date: 4 June 2020
Course: ICT 4370 -  Python Programming

Description:
Creates a program to read JSON Stock Data. Then the program creates a pie graph that correlates the stock portfolio valuation as of 4-Aug 2017
'''

#==============================
#Import matplolib to create pie graph
import matplotlib.pyplot as plt
#Import JSON
import json

#Load data into a list
stock_data = 'AllStocks.json'
with open(stock_data) as stock:
  Stock = json.load(stock)
#==============================

#Creates Close Price list to plot on pie graph
CloseList = []
#Dictionaries for close price stock data that pertain to the date of 4-Aug-17
for Close in Stock:
#The "if statment" to only get Date that have the '4-Aug-17 key
  if Close['Date'] == '4-Aug-17':
    CloseValues = float(Close['Close'])
    CloseList.append(CloseValues)
# Labels that correlate with the Close Prices list
Labels = "AIG","F","FB","GOOG","IBM","M","MSFT","RDS-A"

#==============================

#Creates pie graph with the intended labels to legend
plt.pie(CloseList, labels=Labels, autopct= '%0.1f%%', shadow=True, startangle=90)

#Creates title of pie graph
plt.title('Stock Portfolio Valuation as of 4-Aug 2017',fontsize=22)
#Creates title for legend
plt.legend(title='Stock Symbol')
#Shows actual graph
plt.show()
