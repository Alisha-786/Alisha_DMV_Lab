import matplotlib.pyplot as plt

n = int(input("Enter the number of categories: "))

labels = []
values = []

for i in range(n):
    label = input(f"Enter label {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    labels.append(label)
    values.append(value)

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()