import numpy as np
import pandas as pd


data = pd.read_csv(r'C:\Users\админ\Downloads\Customers.csv', sep=';')
df = pd.DataFrame(data)

filtered_df1 = df[(df['Age'] > 30) & (df['Income'] < 30000)]
filtered_df2 = df[(df['Work Experience'] > 5) & (df['Profession'] == 'Lawyer')]
print(filtered_df1) #те, кому больше 30, а доход ниже 30000
print(filtered_df2) #юристы с опытом больше 5
