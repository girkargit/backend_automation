import csv

name_lst = []
status_lst = []
with open("utilities/loanapp.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)
    # print(list(csvreader))
    for row in csvreader:
        print("*****", row)
        name_lst.append(row[0])
        status_lst.append(row[1])
print(name_lst)
print(status_lst)

# index = name_lst.index("Satish")
print("Loan status is %s." % status_lst[name_lst.index("Satish")])

with open("utilities/loanapp.csv", "a") as wfile:
    write = csv.writer(wfile)
    write.writerow(["Suresh" , "approved"])
