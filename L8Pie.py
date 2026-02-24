import matplotlib.pyplot as plt

sizes = [35, 25, 25, 15]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']

plt.pie(sizes, labels=labels)

plt.axis('equal') 

plt.title('Fruit Preferences')

plt.show()