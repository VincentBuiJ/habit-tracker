import csv

#Variables to track stats
exercise_count = 0
total_water = 0
total_sleep = 0
days = 0
mood_counts = {}  #To count moods

with open("habits.csv", "r") as file:
    csv_file = csv.DictReader(file)
    #Each row is a dictionary 
    for row in csv_file:
        days += 1  # Count total days
        
        #Count exercise days
        if row['exercise'] == 'yes':
            exercise_count += 1
        #Convert CSV values/strings to integer)
        #Add up water glasses
        total_water += int(row['water_glasses']) 
        #Add up sleep hours
        total_sleep += int(row['sleep_hours'])
        #Count moods
        if row['mood'] in mood_counts:
            mood_counts[row['mood']] += 1
        else:
            mood_counts[row['mood']] = 1

#Calculate and print results
if days == 0:
    #Check if there's an empty CSV file
    print("\nNo data to analyze!")
    exit()

print(f"📊 Habit Tracker Stats")
print(f"─" * 30)
print(f"Exercise days: {exercise_count} out of {days}")
print(f"Average water: {total_water / days:.1f} glasses")
print(f"Average sleep: {total_sleep / days:.1f} hours")
print(f"\n😊 Mood breakdown:")
for mood, count in mood_counts.items():
    print(f"  {mood}: {count} days")

most_common_mood = ""
mood_count = 0
#Loop through and track the highest value
for key, value in mood_counts.items():
    if value > mood_count:
        mood_count = value
        most_common_mood = key

#Display the most common mood
print(f"\n🎯 Most common mood: {most_common_mood}")

