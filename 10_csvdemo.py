import csv

with open("utilities/loanapp.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    print(list(csvreader))