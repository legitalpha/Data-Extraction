import csv
import sys

print("Press 1 to search hospital facility in a state \nPress 2 to search hospital facility in a city \n")
n = int(input())
if n==1:
    state = input('Enter state\n')


    csv_file = csv.reader(open('B:\\Python programs\\New folder\\hospital.csv', "r"), delimiter=",")

    for row in csv_file:
        if state == row[0]:
             print("addres=", row[5], "pin-code", row[6])
if n==2:
    city = input('Enter city\n')
    csv_file = csv.reader(open('B:\\Python programs\\New folder\\hospital.csv', "r"), delimiter=",")

    for row in csv_file:
        if city == row[1]:
            print("addres=", row[5], "pin-code", row[6])
else:
    print("Invalid input")