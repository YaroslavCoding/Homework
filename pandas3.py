import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\админ\Downloads\Customers (1).csv', sep=';')

df = pd.DataFrame(data)

filtered_df = df.fillna('Значение отсутствует')

filtered_df = filtered_df.groupby('Profession')['Income'].mean()

print(filtered_df)