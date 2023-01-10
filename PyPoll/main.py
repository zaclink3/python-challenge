import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile)
    
    total_votes_count = -1

    Charles_count = Diana_count = Raymon_count = 0

    Charles_percent = Diana_percent = Raymon_percent = 0

    for row in csv_reader:

        total_votes_count += 1

        if row[2] == "Charles Casper Stockham":
            Charles_count +=1
        elif row[2] == "Diana DeGette":
            Diana_count +=1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_count +=1

    Results = {"Charles Casper Stockham":Charles_count, "Diana DeGette":Diana_count, "Raymon Anthony Doane":Raymon_count}

    Charles_percent = round((Charles_count/total_votes_count)*100, 3)
    Diana_percent = round((Diana_count/total_votes_count)*100, 3)
    Raymon_percent = round((Raymon_count/total_votes_count)*100, 3)

    Winner = max(Results, key=Results.get)

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

textfile = os.path.join("analysis","PyPoll.txt")
with open(textfile, "w") as f:
    f.write(printresults)