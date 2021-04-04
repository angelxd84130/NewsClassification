
import matplotlib.pyplot as plt
Alltop = ["science", "general", "health", "business", "entertainment", "sports"]
Day7 = [61, 226, 133, 294, 270, 341]
fig, ax = plt.subplots()
ax.pie(Day7, labels=Alltop, autopct='%1.1f%%', shadow=True, startangle=20)
ax.axis('equal')
plt.title("Data Distribution")
plt.savefig('PieChart.png')

#plt.show()