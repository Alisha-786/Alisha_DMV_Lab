import pandas as pd
import numpy as np

data = {'A': [10, 20, np.nan, 40],
        'B': [5, np.nan, 15, 20]}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Handling missing values (replace with column mean)
df.fillna(df.mean(), inplace=True)

print("\nAfter Handling Missing Values:")
print(df)