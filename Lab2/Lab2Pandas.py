import  pandas as pd
import numpy as np
from pandas.conftest import names

print('Разминка')
print()
print('Задание 1')
print()

tic = pd.read_csv('sp500hst.txt', delimiter=',', names=['date',
                                                        'ticker','open','high',
                                                        'low','close','volume'])

print(tic)
print()

mean_val = tic[['open','high','low','close']].iloc[:].mean()
print(mean_val)
print()

date_form = pd.to_datetime(tic['date'], format='%Y%m%d')
mon_num = date_form.dt.month
tic['month'] = mon_num
print(mon_num)
print()
print(tic)
print()

tic_val = tic.groupby('ticker').volume.sum()
print(tic_val)
print()

tic_data = pd.read_csv('sp_data2.csv', delimiter=';',
                       names=['ticker','name'],usecols=[0,1])
tic_1 = pd.merge(tic, tic_data, on = 'ticker')
print(tic_data)
print()
print(tic_1)
print()
#tic_1.to_csv('res.csv', sep = '|')

print('Начало лаборатоной работы')
print()
print('Базовые операции с DataFrame')
print()
print('Задание 1')
print()

recipes = pd.read_csv('recipes_sample.csv', sep=',',
                      skip_blank_lines=True, skipinitialspace=True)
reviews = pd.read_csv('reviews_sample.csv', sep=',',
                      names=['id','user_id','recipe_id','date','rating','review'],
                      skiprows=1)
print(recipes)
print()
print(reviews)
print()

print('Задание 2')
print()

print(recipes.info())
print()
print(reviews.info())
print()

print('Задание 3')
print()

num_of_NaN_rev = reviews[:].iloc[:].isna().sum()
num_of_val_rev = reviews['id'].iloc[:].value_counts().sum()
print(num_of_NaN_rev)
print()
print(num_of_val_rev)
print()
print(num_of_NaN_rev/num_of_val_rev)
print()

num_of_NaN_rec = recipes[:].iloc[:].isna().sum()
num_of_val_rec = recipes['id'].iloc[:].value_counts().sum()
print(num_of_NaN_rec)
print()
print(num_of_val_rec)
print()
print(num_of_NaN_rec/num_of_val_rec)
print()

print('Задание 4')
print()

rev_mean_rate = reviews[['rating']].iloc[:].mean()
print(rev_mean_rate)
print()

rec_mean_rate = recipes[['minutes','n_steps','n_ingredients']].iloc[:].mean()
print(rec_mean_rate)
print()

print('Задание 5')
print()

rand_rec_index = pd.Series(np.random.randint(0,30000,10))
print(rand_rec_index)
print()
rand_rec = recipes['name'].iloc[rand_rec_index]
print(rand_rec)
print()

print('Задание 6')
print()

rec_sort = recipes[(recipes['minutes'] <= 20) & (recipes['n_ingredients'] <= 5)]
print(rec_sort)
print()

print('Работа с датами Pandas')
print()

print('Задание 1')
print()

submitted_date = pd.to_datetime(recipes['submitted'], format='%Y-%m-%d')
print(submitted_date)
print()

recipes_dates = pd.read_csv('recipes_sample.csv', sep=',',
                      skip_blank_lines=True,
                            skipinitialspace=True,
                            parse_dates=[4], date_format='%Y-%m-%d')
print(recipes_dates.info())
print()

print(recipes_dates[(recipes_dates['submitted'].dt.year <= 2010)])

print('Работа со строковыми данными в Pandas')
print()

print('Задание 1')
print()

desc_len = pd.DataFrame(pd.Series(recipes['description']).str.len())
print(desc_len)

#recipes['description_length'] = desc_len
#print(recipes)