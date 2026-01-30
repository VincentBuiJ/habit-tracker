import csv
import matplotlib.pyplot as plt

moods = []

#Read habits data
with open("habits.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        moods.append(row["mood"])

#Count each mood
mood_counts = {}
for mood in moods:
    if mood in mood_counts:
        mood_counts[mood] += 1
    else:
        mood_counts[mood] = 1

#Create bar chart
plt.bar(mood_counts.keys(), mood_counts.values())
plt.xlabel("Mood")
plt.ylabel("Number of Days")
plt.title("Mood Distribution")
plt.show()
