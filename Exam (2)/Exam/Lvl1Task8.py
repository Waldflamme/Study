#Датасет: sp500hst.txt
#Создать DataFrame в котором присутствует столбец, отражающий разницу в объемах торгов по NVDA и AAPL в одинаковые дни и содержит исходные данные об объеме торгов этими акциями и модификацию этого DataFrame в котором сохранены только строки для дней, когда и акции NVDA, и акции AAPL дорожали (цена закрытия была выше цены открытия).
#Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.


import pandas as pd

# Загрузка данных
cols = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']
df = pd.read_csv('sp500hst.txt', header=None, names=cols)

# Преобразуем дату в datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# Разделим данные по тикерам
df_nvda = df[df['Ticker'] == 'NVDA'].set_index('Date')
df_aapl = df[df['Ticker'] == 'AAPL'].set_index('Date')

# Переименуем колонки, чтобы не было конфликтов при объединении
df_nvda = df_nvda.rename(columns=lambda x: x + '_NVDA')
df_aapl = df_aapl.rename(columns=lambda x: x + '_AAPL')

# Объединение по дате
merged = df_nvda.join(df_aapl, how='inner')

merged['Volume_Diff'] = merged['Volume_NVDA'] - merged['Volume_AAPL']
print(merged)

# Условия роста
condition = (merged['Close_NVDA'] > merged['Open_NVDA']) & \
            (merged['Close_AAPL'] > merged['Open_AAPL'])

# Применим фильтр
growth_days = merged[condition]
print(growth_days)

