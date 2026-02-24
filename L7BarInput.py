import matplotlib.pyplot as plt

n = int(input("Enter the number of bars:"))

labels = []
values = []

for i in range(n):
    labels.append(input("Enter label: "))
    values.append(int(input("Enter value: ")))

plt.bar(labels, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.show()