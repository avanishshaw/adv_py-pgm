import csv

# Reading as a .csv file
with open("C://Users//avan1//PyCharmMiscProject//DataFormats//Data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# writing to the csv file
with open("C://Users//avan1//PyCharmMiscProject//DataFormats//Data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "marks"])
    writer.writerow([1, "Rahul", 85])
    writer.writerow([2, "Ankita", 90])


# append ding the data to csv file

with open("C://Users//avan1//PyCharmMiscProject//DataFormats//Data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([3, "Kiran", 88])



