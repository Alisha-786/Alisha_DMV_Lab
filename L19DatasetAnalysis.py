import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
plt.style.use('ggplot')

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# -------------------------------
# PRINT MISSING VALUES (IMPORTANT)
# -------------------------------
print("Missing values in each column:\n")
print(df.isnull().sum())



# Reduce + clean
df = df.head(30)
df = df[['Sex','Age','Fare','Pclass']].dropna()

# -------------------------------
# DASHBOARD LAYOUT (3 TOP, 2 BOTTOM)
# -------------------------------
fig = plt.figure(figsize=(16,10))

# ---------- ROW 1 (3 charts) ----------
ax1 = plt.subplot(2,3,1)
df['Sex'].value_counts().plot(kind='bar', ax=ax1)
ax1.set_title("Bar Chart for Gender Distribution")

ax2 = plt.subplot(2,3,2)
ax2.scatter(df['Age'], df['Fare'])
ax2.set_title("Scatter Plot of Age vs Fare")

ax3 = plt.subplot(2,3,3)
ax3.plot(df['Age'])
ax3.set_title("Line Chart of Age Trend")

# ---------- ROW 2 (2 charts centered nicely) ----------
ax4 = plt.subplot(2,3,4)
df['Pclass'].value_counts().plot(kind='pie', ax=ax4, autopct='%1.1f%%')
ax4.set_title("Pie Chart of Passenger Class")

ax5 = plt.subplot(2,3,5)
ax5.step(range(len(df)), df['Fare'])
ax5.set_title("Stair Chart for Fare")

# Hide last empty space
ax6 = plt.subplot(2,3,6)
ax6.axis('off')
plt.subplots_adjust(hspace=0.4, wspace=0.3)  # spacing between plots
plt.tight_layout()
plt.show()

input("Press Enter to exit...")
