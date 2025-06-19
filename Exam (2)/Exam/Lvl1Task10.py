#Датасет: sp_data2.csv, sp500hst.txt
#Сохранить в sp500hst_names.txt CSV с добавленным столбцом с расшифровкой названия тикера. Использовать для этого данные из файла sp_data2.csv. В случае нехватки данных об именах тикеров корректно обработать такую ситуацию (в новом столбце для этих случаев должно быть пустое значение).
#Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.


import pandas as pd

# Загрузка данных
# Данные из sp500hst.txt
file_path = 'sp500hst.txt'
sp500hst = pd.read_csv(file_path, header=None, names=['Date', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume'])

# Данные из sp_data2.csv
file_path = 'sp_data2.csv'
sp_data2 = pd.read_csv('sp_data2.csv', header=None, names=['Symbol', 'Name', 'Volume'], delimiter=";")

# Обработка данных
# Создание словаря для маппинга тикеров на их расшифровки
ticker_mapping = sp_data2.set_index('Symbol')['Name'].to_dict()

# Добавление столбца 'Name' с расшифровкой тикеров
sp500hst['Name'] = sp500hst['Symbol'].map(ticker_mapping)

# Сохранение результата
sp500hst.to_csv('sp500hst_names.txt', index=False)