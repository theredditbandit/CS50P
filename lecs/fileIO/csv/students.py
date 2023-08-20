import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","home"]) # we need to provide fieldnames to the Dict writer method
    writer.writerow({"name":name,"home":home}) # write row takes as input a dictionary

