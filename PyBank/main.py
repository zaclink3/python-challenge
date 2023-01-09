import os
import csv


pybank_csv= os.path.join("Resources","budget_data.csv")


month = []
profit_losses = []
change_pl = []

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    month_of_increase = 0
    greatestincrease = 0
    greatestdecrease = 0 
    month_of_decrease = 0
    total_profit = 0
    total_month_count = 0
    change_average = 0
    change_difference = 0
    change_total = 0
    change_total_average = 0
    next(csvreader)
    

    for row in csvreader:
        total_month_count += 1
        total_profit = total_profit + float(row[1])
        change_difference = change_total
        change_total = change_difference + float(row [1]) 
        change_total_average = change_total - change_difference

        if change_total_average > greatestincrease:
            greatestincrease = change_total_average
            month_of_increase = row [0]
        elif change_total_average < greatestdecrease:
            greatestdecrease = change_total_average
            month_of_decrease = row [0]

print(greatestdecrease)
print(greatestincrease)
print(change_total_average)

#print("Total Months:", len(month))
#print("Total:", sum(profit_losses))
#print("Average Change:", sum(change_pl)/len(change_pl))
#print(f'Greatest increase in profit: {month_of_increase} , ({greatestincrease})')
#print(f'Greatest decrease in profit: {month_of_decrease} , ({greatestdecrease})')
     


