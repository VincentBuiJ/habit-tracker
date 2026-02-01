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


def show_sleep_trend():
    dates = []
    sleep_hours = []

    with open("habits.csv", "r") as csv_file:
        file_reader = csv.DictReader(csv_file)
        for date_row in file_reader:
            dates.append(date_row["date"])
            sleep_hours.append(int(date_row["sleep_hours"]))

    plt.figure(figsize = (10,6))

    #Plot using indices
    plt.plot(range(len(sleep_hours)), sleep_hours, marker = "o")

    plt.xlabel("Days")
    plt.ylabel("Sleep Hours")
    plt.title("Sleep Trend Over Time")

    #Set x-axis to show dates
    step = max(1, len(dates) // 5)
    tick_positions = list(range(0, len(dates), step))
    tick_labels = [dates[i] for i in tick_positions]

    plt.xticks(tick_positions, tick_labels, rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

#Display mood chart
plt.bar(mood_counts.keys(), mood_counts.values())
plt.xlabel("Mood")
plt.ylabel("Number of Days")
plt.title("Mood Distribution")
plt.show()

#Display mood trend
show_sleep_trend()



