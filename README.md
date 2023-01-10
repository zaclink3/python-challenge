# python-challenge

PYBANK ---------

#import dependencies
import os
import csv

#locate the csv file
pybank_csv= os.path.join("Resources","budget_data.csv")

#create lists (went a seperate way but still)
month = []
profit_losses = []
change_pl = []

#open csv file and establish your variables
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
    
#start forloop with your formulas on how you are going to find each answer
    for row in csvreader:
        total_month_count += 1
        total_profit = total_profit + float(row[1])

        current_loss_gain = float(row[1])
        change_total = current_loss_gain - prior_loss_gain
        prior_loss_gain = current_loss_gain
        rolling_change_total = rolling_change_total + change_total

#if statements for specific increase/decrease
        if change_total > greatestincrease:
            greatestincrease = change_total
            month_of_increase = row [0]
        elif change_total < greatestdecrease:
            greatestdecrease = change_total
            month_of_decrease = row [0]

average_change = rolling_change_total / total_month_count

#capture all of this in one print by using three """
printresults = f"""

Total Months: {total_month_count}
Total: {total_profit}
Average Change: {average_change}
Greatest increase in profits: {month_of_increase}, {greatestincrease}
Greatest decrease in profits: {month_of_decrease}, {greatestdecrease}"""

   #print results  
print(printresults)

#print to a text file in the analysis folder
textfile = os.path.join("analysis","PyBank.txt")
with open(textfile, "w") as f:
    f.write(printresults)


PY POLL -----------------------
#import your dependencies
    import csv
import os

#select the CSVfile
csvpath = os.path.join("Resources","election_data.csv")

#open the csv file and establish parameters on how you are doing to test this
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile)
    
    total_votes_count = -1

    Charles_count = Diana_count = Raymon_count = 0

    Charles_percent = Diana_percent = Raymon_percent = 0

#create a for loop to establish how you should count each vote based on row 2
    for row in csv_reader:

        total_votes_count += 1

        if row[2] == "Charles Casper Stockham":
            Charles_count +=1
        elif row[2] == "Diana DeGette":
            Diana_count +=1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_count +=1

#set what the results should be equal to
    Results = {"Charles Casper Stockham":Charles_count, "Diana DeGette":Diana_count, "Raymon Anthony Doane":Raymon_count}
#establish percentages
    Charles_percent = round((Charles_count/total_votes_count)*100, 3)
    Diana_percent = round((Diana_count/total_votes_count)*100, 3)
    Raymon_percent = round((Raymon_count/total_votes_count)*100, 3)
#use key function to find winner
    Winner = max(Results, key=Results.get)
#use """ to capture all of the print function
printresults = f"""Election Results
___________________________________
Total Votes: {total_votes_count}
___________________________________
Charles Casper Stockham: {Charles_percent}% ({Charles_count})
Diana Degette: {Diana_percent}% ({Diana_count})
Raymon Anthony Doane: {Raymon_percent}% ({Raymon_count})
___________________________________
Winner: {Winner}
___________________________________"""

print(printresults)
#write the text file in the analysis file
textfile = os.path.join("analysis","PyPoll.txt")
with open(textfile, "w") as f:
    f.write(printresults)