import numpy as np
import matplotlib.pyplot as plt

# Plot for Music.dat
with open("Music.dat", "r") as f:
    for line in f:
        if line[0].isdigit():
            amount_people = [int(number) for number in line.split(" ")]

labels = "Grunge", "Hip Hop", "Metal", "Schlager", "Rock"
sizes = [ap/sum(amount_people) for ap in amount_people]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.show()
plt.close()

# Plots for lecture grades
grades = []
with open("Grades_lecture1.dat", "r") as f:
    for line in f:
        if line[0].isdigit():
            grades.append(line[0])
grades_count = {i: grades.count(i) for i in grades}

grades2 = []
with open("Grades_lecture2.dat", "r") as f:
    for line in f:
        if line[0].isdigit():
            grades2.append(line[0])
grades_count2 = {i: grades2.count(i) for i in grades2}

grades = ["1", "2", "3", "4", "5"]
count = [grades_count[i] for i in grades]
count2 = [grades_count2[i] for i in grades]
x = np.arange(1, 6)
fig, ax = plt.subplots()
ax.bar(x - 0.2, count, color="b", width=0.4)
ax.bar(x + 0.2, count2, color="r", width=0.4)
ax.legend(labels=["Lecture 1", "Lecture 2"])
ax.set_xlabel("Grades")
ax.set_ylabel("Number of students")
plt.show()
