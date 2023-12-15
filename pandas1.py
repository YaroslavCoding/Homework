import numpy as np
import pandas as pd

data = {'Race': ['Asian', 'Indian', 'Mixed', 'European', 'Asian', 'African'], 'Age': [15, 53, 6, 7, 76, 23], 'ID': np.arange(1,7)}

df = pd.DataFrame(data)

print('--------------------------------------------')
print(df.head(3)) #первые три строки
print('--------------------------------------------')
print(df.tail(3)) #последние три строки

df.to_csv('dataframe.csv') #сохранение в csv формат
