import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x value {i+1}: ")))
    y.append(float(input(f"Enter y value {i+1}: ")))

plt.scatter(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot (User Input)")
plt.show()