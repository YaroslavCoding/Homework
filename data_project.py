import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\админ\Downloads\Housing.csv")
df = pd.DataFrame(data)
#1 часть
#1)
cheapest_house = df.groupby('price').min()['bedrooms'].head(1) #спальни в самом дешевом доме (объект Series)
print(f'Количество спален в самом дешевом доме - {cheapest_house.iloc[0]}') #количество спален в самом дешевом доме
print('**************************************************')

#2)
houses = df[df['bedrooms'] <= df['bathrooms']].shape[0]
print(f'Количество домов, где спален не больше ванных - {houses}')
print('**************************************************')

#3)
guestrooms = df[df['guestroom'] == 'yes']
cheapest_house = guestrooms.groupby('price').min().head(1)
print(f'Цена самого дешевого дома с гостевой - {cheapest_house.reset_index()["price"].iloc[0]}')
print('**************************************************')

#4)
houses = df[(df['price'] >= 5000000) | (df['price'] < 2000000)]
airconditioning = houses[houses['airconditioning'] == 'yes']
percentage = airconditioning.size/houses.size*100
print(int(percentage), "- столько процентов могут похвастаться наличием кондиционера")
print('**************************************************')

#2 часть
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 6))
axes[0].scatter(df['price'], df['area'], marker='o', alpha=0.4)
axes[0].scatter(df[df['parking'] == 0]['price'], df[df['parking'] == 0]['area'], c='black', label='отсутствие парковочных мест')
axes[0].scatter(df[df['parking'] == 1]['price'], df[df['parking'] == 1]['area'], c='gray', label='одно парковочное место')
axes[0].scatter(df[df['parking'] == 2]['price'], df[df['parking'] == 2]['area'], c='blue', label='два парковочных места')
axes[0].scatter(df[df['parking'] == 3]['price'], df[df['parking'] == 3]['area'], c='yellow', label='три и более парковочных места')
axes[0].set_xlabel('Цена')
axes[0].set_ylabel('Площадь')
axes[0].legend()
plt.tight_layout()
plt.show()

#3 часть
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].scatter(df['price'], df['area'])
axes[0, 0].scatter(df[df['guestroom'] == 'yes']['price'], df[df['guestroom'] == 'yes']['area'], color='red', label='есть гостиная')
axes[0, 0].scatter(df[df['guestroom'] == 'no']['price'], df[df['guestroom'] == 'no']['area'], color='blue', label='нет гостиной')
axes[0, 0].set_title('Дома с гостевой комнатой')
axes[0, 0].grid()
axes[0, 0].legend()
axes[0, 0].set_xlabel('цена')
axes[0, 0].set_ylabel('площадь')
axes[0, 0].text(4900000, 2000, 'наличие или отсутствие гостиной в квартирах', fontsize=8)
axes[0, 1].scatter(df['price'], df['area'])
axes[0, 1].scatter(df[df['basement'] == 'yes']['price'], df[df['basement'] == 'yes']['area'], color='red', label='есть подвал')
axes[0, 1].scatter(df[df['basement'] == 'no']['price'], df[df['basement'] == 'no']['area'], color='blue', label='нет подвала')
axes[0, 1].set_title('Дома с подвалом')
axes[0, 1].grid()
axes[0, 1].legend()
axes[0, 1].set_xlabel('цена')
axes[0, 1].set_ylabel('площадь')
axes[0, 1].text(4900000, 2000, 'наличие или отсутствие гостиной в квартирах', fontsize=8)
axes[1, 0].scatter(df['price'], df['area'])
axes[1, 0].scatter(df[df['hotwaterheating'] == 'yes']['price'], df[df['hotwaterheating'] == 'yes']['area'], color='red', label='есть отопление')
axes[1, 0].scatter(df[df['hotwaterheating'] == 'no']['price'], df[df['hotwaterheating'] == 'no']['area'], color='blue', label='нет отопления')
axes[1, 0].set_title('Дома с обогревом')
axes[1, 0].grid()
axes[1, 0].legend()
axes[1, 0].set_xlabel('цена')
axes[1, 0].set_ylabel('площадь')
axes[1, 0].text(4900000, 2000, 'наличие или отсутствие гостиной в квартирах', fontsize=8)
axes[1, 1].scatter(df['price'], df['area'])
axes[1, 1].scatter(df[df['prefarea'] == 'yes']['price'], df[df['prefarea'] == 'yes']['area'], color='red', label='есть отопление')
axes[1, 1].scatter(df[df['prefarea'] == 'no']['price'], df[df['prefarea'] == 'no']['area'], color='blue', label='нет отопления')
axes[1, 1].set_title('Дома с предбанником')
axes[1, 1].grid()
axes[1, 1].legend()
axes[1, 1].set_xlabel('цена')
axes[1, 1].set_ylabel('площадь')
axes[1, 1].text(4900000, 2000, 'наличие или отсутствие гостиной в квартирах', fontsize=8)
plt.tight_layout()
plt.show()
