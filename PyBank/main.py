import os
import csv
import math


pybank_csv= os.path.join("Resources","budget_data.csv")

print("Financial Analysis")
print("__________________________________________")

month = []
profit_losses = []
change_pl = []

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimeter=",")
    month_of_increase = 0
    greatestincrease = 0
    greatestdecrease = 0 
    month_of_decrease = 0

    change_pl.append(row[2])

    next(csvreader)
    

    for row in csvreader:
        print("Total Months:", len(month))
        print("Total:", sum(profit_losses))
        print("Average Change:", sum(change_pl)/len(change_pl))

        if float(row[1])> greatestincrease:
            month_of_increase, greatestincrease = row[0],float(row[1])
        
        if float(row[1])< greatestdecrease:
            month_of_decrease, greatestdecrease = row[0],float(row[1])


print(f'Greatest increase in profit: {month_of_increase} , ({greatestincrease})')
print(f'Greatest decrease in profit: {month_of_decrease} , ({greatestdecrease})')
     


