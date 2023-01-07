import os
import csv

pybank_csv= os.path.join("..","Resources","budget_data.csv")

print("Financial Analysis")
print("__________________________________________")

month = []
profit_losses = []

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimeter=",")

    csv_header = next(csvfile)
    print(f"Header:{csv_header}")

    for row in csvreader:
        month = (row [0])
        profit_losses = (row [1])


        



       list.count(month)= count(row[0])
       print("Total Months" "=" total_months)


