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
    prior_loss_gain = 0
    current_loss_gain = 0
    change_total = 0
    rolling_change_total = 0
    next(csvreader)
    

    for row in csvreader:
        total_month_count += 1
        total_profit = total_profit + float(row[1])
        
        current_loss_gain = float(row[1])
        change_total = current_loss_gain - prior_loss_gain
        prior_loss_gain = current_loss_gain
        rolling_change_total = rolling_change_total + change_total

        if change_total > greatestincrease:
            greatestincrease = change_total
            month_of_increase = row [0]
        elif change_total < greatestdecrease:
            greatestdecrease = change_total
            month_of_decrease = row [0]


print("Total Months:", total_month_count)
print("Total:", total_profit)
print("Average Change:", rolling_change_total/total_month_count)
print("Greatest increase in profits:", month_of_increase, greatestincrease)
print("Greatest decrease in profits:", month_of_decrease, greatestdecrease)
     


