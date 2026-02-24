import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D']
values = [3, 8, 1, 10]

plt.bar(categories, values, color='skyblue')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart')

plt.show()