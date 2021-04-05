import matplotlib.pyplot as plt
Models = ['Naive Bayes', 'SVM', 'Logistic Regression']
day1 = [0.283018, 0.452830, 0.283018]
day2 = [0.384615, 0.471153, 0.365384]
day3 = [0.484076, 0.579617, 0.477707]
day4 = [0.550239, 0.645933, 0.588516]
day5 = [0.590733, 0.640926, 0.610038]
day6 = [0.593856, 0.638225, 0.631399]
day7 = [0.539156, 0.608433, 0.551204]

fig, ax = plt.subplots()
plt.title("Supervised Learning")
plt.xlabel("Models")
plt.ylabel("Accuracy")
ax.plot(Models, day1, label='Day1')
ax.plot(Models, day2, label='Day2')
ax.plot(Models, day3, label='Day3')
ax.plot(Models, day4, label='Day4')
ax.plot(Models, day5, label='Day5')
ax.plot(Models, day6, label='Day6')
ax.plot(Models, day7, label='Day7')
plt.legend()
plt.savefig('SupervisedLearning.png')

