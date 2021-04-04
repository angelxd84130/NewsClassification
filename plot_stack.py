import matplotlib.pyplot as plt

Alltop = ["science", "general", "health", "business", "entertainment", "sports"]
science = [8, 8, 13, 11, 12, 6, 3]
general = [37, 33, 34, 29, 33, 30, 30]
health = [20, 31, 24, 26, 20, 5, 7]
business = [50, 50, 46, 46, 40, 23, 39]
entertainment = [45, 34, 46, 47, 43, 25, 30]
sports = [50, 50, 49, 49, 50, 49, 44]

day1 = [8, 37, 20, 50, 45, 50]
day2 = [8, 33, 31, 50, 34, 50]
day3 = [13, 34, 24, 46, 46, 49]
day4 = [11, 29, 26, 46, 47, 49]
day5 = [12, 33, 20, 40, 43, 50]
day6 = [6, 30, 5, 23, 25, 49]
day7 = [3, 30, 7, 39, 30, 44]

Day1 = [8, 37, 20, 50, 45, 50]
Day2 = [16, 70, 51, 100, 79, 100]
Day3 = [29, 104, 75, 146, 125, 149]
Day4 = [40, 133, 101, 192, 172, 198]
Day5 = [52, 166, 121, 232, 215, 248]
Day6 = [58, 196, 126, 255, 240, 297]
Day7 = [61, 226, 133, 294, 270, 341]

width = 0.35
fig, ax = plt.subplots()

ax.bar(Alltop, Day6, width, label='Day6')
ax.bar(Alltop, Day5, width, label='Day5')
ax.bar(Alltop, Day4, width, label='Day4')
ax.bar(Alltop, Day3, width, label='Day3')
ax.bar(Alltop, Day2, width, label='Day2')
ax.bar(Alltop, Day1, width, label='Day1')
ax.set_ylabel('articles')
ax.set_title('Data Accumulation')
ax.legend()
plt.savefig('DataAccumulation.png')
#plt.show()
