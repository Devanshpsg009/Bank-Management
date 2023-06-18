import csv
with open("account.csv","r") as file:
    db = csv.reader(file)
    for row in db:
        usrnm = row[0]
        accno = row[1]
        print(usrnm)
        print(accno)