import csv
from datetime import date

#Get today's date
today = date.today().strftime("%Y-%m-%d")

#Ask user for input
exercise = input("Did you exercise today? (yes/no): ")
water = input("How many glasses of water? ")
sleep = input("How many hours of sleep? ")
mood = input("How's your mood? (great/good/okay/tired): ")

#Open CSV in append mode
with open("habits.csv", "a", newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write a new row
    writer.writerow([today, exercise, water, sleep, mood])
    
#End of program
print("Habit logged!")