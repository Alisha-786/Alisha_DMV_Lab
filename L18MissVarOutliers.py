import pandas as pd

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# -------------------------------
# Missing Values Detection
# -------------------------------
print("Missing Values in Dataset:\n")
missing_values = df.isnull().sum()
print(missing_values)

# -------------------------------
# Outlier Detection using IQR
# -------------------------------
def detect_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = column[(column < lower_bound) | (column > upper_bound)]
    return outliers

print("\nOutliers in Dataset:\n")

# Check only numerical columns
for col in ['Age', 'Fare']:
    outliers = detect_outliers(df[col].dropna())
    print(f"{col} Outliers:\n{outliers}\n")
