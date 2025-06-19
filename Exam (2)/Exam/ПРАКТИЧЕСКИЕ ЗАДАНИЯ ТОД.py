import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#############
# ЗАДАНИЕ №1 (1 ур.)
#############

ar1 = np.random.randint(-5, 6, size=(10, 4))
ar2 = np.random.randint(-5, 6, size=(10, 4))

result = np.where(ar1 > ar2, ar1 * 2, 0) # условие - ar1 > ar2; если выполняется, оно удвоит зн-е, если нет - обнулит
print("################ ЗАДАНИЕ 1 (1 УР) ################\n")
print("ar1:\n", ar1)
print("ar2:\n", ar2)
print("result:\n", result)
print("\n\n")

#############
# ЗАДАНИЕ №2 (1 ур.)
#############

import numpy as np

ar1 = np.random.randint(0, 16, size=(25, 4))
rowMax = ar1.max(axis=1)
isRowMax = ar1 == rowMax[:, None]  # shape: (25, 4)
colCnts = isRowMax.sum(axis=0)  # shape: (4,)
colsWith5OrMoreMax = np.where(colCnts >= 5)[0]
print("################ ЗАДАНИЕ 2 (1 УР) ################\n")
print("ar1:\n", ar1)
print("Индексы столбцов, где максимум по строке встречается не менее 5 раз:", colsWith5OrMoreMax)

maxCol = np.argmax(colCnts)

print(f"Столбец с наибольшим количеством максимумов по строке: {maxCol} (количество: {colCnts[maxCol]})")
ar1Mod = ar1.copy()
ar1Mod[isRowMax[:, maxCol], maxCol] = -1

print("ar1 после замены максимумов на -1 в выбранном столбце:\n", ar1Mod)
print("\n\n")

#############
# ЗАДАНИЕ №3 (1 ур.)
#############

ar = np.random.randint(0, 101, size=(30, 4))

norms = np.linalg.norm(ar, axis=1)

top5Indices = np.argsort(norms)[-5:][::-1]

top5Vectors = ar[top5Indices]
print("################ ЗАДАНИЕ 3 (1 УР) ################\n")
print("Исходный массив:\n", ar)
print("Евклидовы нормы:\n", norms)
print("Индексы 5 векторов с наибольшей длиной:", top5Indices)
print("Массив 5x4 из векторов с наибольшей длиной:\n", top5Vectors)
print("\n\n")

#############
# ЗАДАНИЕ №4 (1 ур.)
#############

arr = np.random.randint(0, 5, size=10)

# Получаем отсортированные уникальные значения и индексы для восстановления исходного порядка
uniq, inv = np.unique(arr, return_inverse=True)

oneHot = np.eye(len(uniq))[inv]
print("################ ЗАДАНИЕ 4 (1 УР) ################\n")
print("Исходный массив:\n", arr)
print("One-hot encoding:\n", oneHot)
print("\n\n")

#############
# ЗАДАНИЕ №5 (1 ур.)
#############

arr = np.random.randint(0, 51, size=(10, 4))

# 2. Находим самое частое число (или числа)
flat = arr.ravel()
values, counts = np.unique(flat, return_counts=True)
maxCnt = counts.max()
mostFreq = values[counts == maxCnt]
print("################ ЗАДАНИЕ 5 (1 УР) ################\n")
print("Исходный массив:\n", arr)
print("Самое частое(ые) число(а):", mostFreq, "встречается(ются)", maxCnt, "раз(а)")

# 3. Информация о расположении всех этих значений
# Создаём булев массив, где True — если элемент равен одному из самых частых чисел
mask = np.isin(arr, mostFreq)
positions = np.argwhere(mask)
print("Позиции самых частых значений (строка, столбец):\n", positions)

# 4. Для каждой строки считаем, сколько в ней самых частых значений
rowCnts = mask.sum(axis=1)

# 5. Находим индексы 3 строк с наибольшим количеством самых частых значений
# Если таких строк больше 3, берём первые 3 по убыванию количества
top3Rows = np.argsort(rowCnts)[-3:][::-1]

# 6. Возвращаем массив (3, 4) из этих строк
result = arr[top3Rows]
print("3 строки с наибольшим количеством самых частых значений:\n", result)
print("\n\n")

#############
# ЗАДАНИЕ №6 (1 ур.)
#############

xValues = np.linspace(0, 5, 100)
yValues = np.linspace(0, 5, 100)
xGrid, yGrid = np.meshgrid(xValues, yValues)
zValues = xGrid * yGrid * np.sin(xGrid) * np.cos(yGrid) # это МАССИВ!

greaterThanThreshold = zValues > 0.25 # отсеиваем нужные значения
areaGreaterThanThreshold = np.sum(greaterThanThreshold)
totalArea = zValues.size # это даст всю площадь прямоугольника т.к. пересчёт значений функций ведётся по всем точкам в нём
proportion = areaGreaterThanThreshold / totalArea
print("################ ЗАДАНИЕ 6 (1 УР) ################\n")
print(f"Часть прямоугольника, на которой функция превышает 0.25: {proportion * 100}%")
print("\n\n")

#############
# ЗАДАНИЕ №7 (1 ур.)
#############

df = pd.read_csv('sp500hst.txt', header=None, names=['date', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

nvda = df[df['ticker'] == 'NVDA'].copy()
nvda['date'] = pd.to_datetime(nvda['date'], format='%Y%m%d')

idxMax = nvda['open'].idxmax()
idxMin = nvda['open'].idxmin()

dateMax = nvda.loc[idxMax, 'date']
dateMin = nvda.loc[idxMin, 'date']

dateStart = min(dateMax, dateMin)
dateEnd = max(dateMax, dateMin)

daysBetween = (dateEnd - dateStart).days

period = nvda[(nvda['date'] >= dateStart) & (nvda['date'] <= dateEnd)]

totalVlm = period['volume'].sum()
print("################ ЗАДАНИЕ 7 (1 УР) ################\n")
print(f"Между максимумом ({dateMax.date()}) и минимумом ({dateMin.date()}) прошло {daysBetween} дней (включительно: {daysBetween+1} дней).")
print(f"Суммарный объем торгов за этот период: {totalVlm}")
print("\n\n")

#############
# ЗАДАНИЕ №8 (1 ур.)
#############

data = pd.read_csv('sp500hst.txt', header=None, names=['date', 'symbol', 'open', 'high', 'low', 'close', 'volume'])
nvdaData = data[data['symbol'] == 'NVDA'][['date', 'volume', 'close', 'open']]
aaplData = data[data['symbol'] == 'AAPL'][['date', 'volume', 'close', 'open']]
# объединяем по дате
mergedData = pd.merge(nvdaData, aaplData, on='date', suffixes=('_nvda', '_aapl'))
mergedData['volumeDifference'] = mergedData['volume_nvda'] - mergedData['volume_aapl']
# модифицируем (оставляем только там, где дорожает)
filteredData = mergedData[(mergedData['close_nvda'] > mergedData['open_nvda']) & (mergedData['close_aapl'] > mergedData['open_aapl'])]
print("################ ЗАДАНИЕ 8 (1 УР) ################\n")
print(filteredData)
print("\n\n")

#############
# ЗАДАНИЕ №9 (1 ур.)
#############

df = pd.read_csv('Titanic.csv')

# Сохраним маску пропусков возраста
ageNA = df['Age'].isna()

# Сохраним маску, где известны и Pclass, и Sex (для остальных не заполняем)
hasClassAndSex = df['Pclass'].notna() & df['Sex'].notna()

# Группируем по Pclass и Sex и считаем средний возраст по этим группам (игнорируя NaN)
groupMeans = df.groupby(['Pclass', 'Sex'])['Age'].transform('mean')

# Заполняем только там, где Age пропущен, но Pclass и Sex известны
df['Age'] = df['Age'].mask(ageNA & hasClassAndSex, groupMeans)
print("################ ЗАДАНИЕ 9 (1 УР) ################\n")
print(df.loc[ageNA, ['PassengerId', 'Pclass', 'Sex', 'Age']].head(20)) # тут я вывожу именно те строки, где возраста у пассажиров нет
print("\n\n")

#############
# ЗАДАНИЕ №10 (1 ур.)
#############
# я это с прошлого семинара взял, не серчайте

tickerData = pd.read_csv('sp_data2.csv', header=None, names=['ticker', 'name', 'percentage'], delimiter=";")
tradeHistoryData = pd.read_csv('sp500hst.txt', header=None, names=['date', 'ticker', 'open', 'high', 'low', 'close', 'volume'])
mergedData = tradeHistoryData.merge(tickerData[['ticker', 'name']], on='ticker', how='left')

mergedData.to_csv('sp500hst_names.txt', header=False, index=False)

print("################ ЗАДАНИЕ 10 (1 УР) ################\n")
print("оно находится в .csv-файле\n\n\n")

#############
# ЗАДАНИЕ №11 (1 ур.)
#############

df2 = pd.read_csv('sp500hst.txt', header=None, names=['date', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

# Преобразуем столбец 'date' в тип datetime
df2['date'] = pd.to_datetime(df2['date'], format='%Y%m%d')

# Фильтруем данные за 2010 год
df2010 = df2[df2['date'].dt.year == 2010]

# Группируем по тикеру и рассчитываем среднее значение по столбцам OHLC (open, high, low, close)
result = df2010.groupby('ticker')[['open', 'high', 'low', 'close']].mean().reset_index()

result.to_csv('sp500_2010_avg.csv', index=False)
print("################ ЗАДАНИЕ 11 (1 УР) ################\n")
print("оно находится в .csv файле\n\n\n")

#############
# ЗАДАНИЕ №12 (1 ур.)
#############

df3 = pd.read_csv('sp500hst.txt', header=None, names=['date', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

# Преобразуем столбец 'date' в тип datetime
df3['date'] = pd.to_datetime(df3['date'], format='%Y%m%d')

# Создаем сводную таблицу, где индекс - это дата, а столбцы - тикеры, значения - объемы торгов
pivotTable = df3.pivot_table(index='date', columns='ticker', values='volume', aggfunc='sum')

pivotTable.to_csv('sp500_trade_volumes.csv')

#############
# ЗАДАНИЕ №13 (1 ур.)
#############
data = pd.read_csv('Titanic.csv')
print(data.head()) # первые 5 строк
print("################ ЗАДАНИЕ 13 (1 УР) ################\n")
print(f"Форма у таблицы: {data.shape}") # выбивает кол-во строк и столбцов
print(f"Информация о таблице: {data.info()}") # выбивает информацию о столбцах (название, кол-во непустых зн-ий и тип)

missingRows = data[data.isnull().any(axis=1)]
data = data.dropna()

meanFareByPclass = data.groupby('Pclass')['Fare'].mean()
print(f"Табличка с средними ценами на билет по классу: \n{meanFareByPclass}")

survivedUnder18 = data[(data['Survived'] == 1) & (data['Age'] < 18)]
countSurvivedUnder18 = survivedUnder18.shape[0]
print(f"Выживших младше 18 лет: {countSurvivedUnder18}\n\n")
print("\n\n")

#############
# ЗАДАНИЕ №14 (1 ур.)
#############

# Поскольку чтение таблицы+принт информации я уже делал, я не собираюсь это счастье по второму кругу делать
data1 = pd.read_csv('Titanic.csv')

missingRows1 = data1[data1.isnull().any(axis=1)]

numericColumns = data1.select_dtypes(include='number').columns # Выбираем количественные колонки
data1[numericColumns] = data1[numericColumns].fillna(data1[numericColumns].mean()) # В количественных колонках заполняем пустые значения средним по столбцу
print("################ ЗАДАНИЕ 14 (1 УР) ################\n")
print(data1.loc[29]) # в этой строке нет возраста, значит в столбце возраста должно выдать что-то усреднённое
meanAgeByEmbarked = data1.groupby('Embarked')['Age'].mean() # Группируем по портам отправления, берём возраст, рассчитываем ср. знач-е
print(f"Средний возраст людей по портам отправления: {meanAgeByEmbarked}")

diedOlderCount = data1[(data1['Survived'] == 0) & (data1['Age'] > 30)].shape[0] # survived == 0 - не выжил; возраст больше 30
print(f"Погибших старше 30 лет: {diedOlderCount}")
print("\n\n")

#############
# ЗАДАНИЕ №1 (2 ур.)
#############

from bs4 import BeautifulSoup
import json


def parseAddressBook(xmlFile):
    with open(xmlFile, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'xml')
    addressBook = {}

    for address in soup.find_all('address'):
        position = address.find('position').text.lower()
        name = address.find('name').text
        company = address.find('company').text
        phones = [phone.text for phone in address.find('phones').find_all('phone')]

        if position not in addressBook:
            addressBook[position] = []

        addressBook[position].append({
            'name': name,
            'company': company,
            'phones': phones
        })
    return addressBook

def saveToJson(data, jsonFile):
    with open(jsonFile, 'w') as f:
        json.dump(data, f, indent=4)
def loadFromJson(jsonFile):
    with open(jsonFile, 'r') as f:
        return json.load(f)
addressBook = parseAddressBook('addres-book-q.xml')
saveToJson(addressBook, 'address_book.json')
loadedAddressBook = loadFromJson('address_book.json')
print("################ ЗАДАНИЕ 1 (2 УР) ################\n")
print(f"Проверка на идентичность данных: {addressBook == loadedAddressBook}")
print(f"Сами данные: \n{loadedAddressBook}")
print("\n\n")

#############
# ЗАДАНИЕ №2 (2 ур.)
#############

import pickle

with open('addres-book-q.xml', encoding='utf-8') as f:
    xml_data = f.read()

soup = BeautifulSoup(xml_data, 'xml')

menList = []
womenList = []

for address in soup.find_all('address'):
    gender = address.gender.text.strip()
    name = address.find('name').text.strip()
    company = address.company.text.strip() if address.company else None

    # Словарь телефонов по типу
    phones = {p['type']: p.text.strip() for p in address.find_all('phone')}

    if gender == 'm':
        workPhone = phones.get('work')
        menList.append((name, company, workPhone))
    elif gender == 'f':
        persPhone = phones.get('personal')
        womenList.append((name, persPhone))

# Сохраняем в pickle
with open('men_list.pkl', 'wb') as f:
    pickle.dump(menList, f)

with open('women_list.pkl', 'wb') as f:
    pickle.dump(womenList, f)

# Загружаем обратно
with open('men_list.pkl', 'rb') as f:
    menLoaded = pickle.load(f)

with open('women_list.pkl', 'rb') as f:
    womenLoaded = pickle.load(f)

# Проверка
print("################ ЗАДАНИЕ 2 (2 УР) ################\n")
print('Мужчины:', menLoaded)
print('Женщины:', womenLoaded)
print("\n\n")

#############
# ЗАДАНИЕ №3 (2 ур.)
#############

countriesDf = pd.read_csv('countries-of-the-world.csv')
countriesNp = countriesDf.values

print("################ ЗАДАНИЕ 3 (2 УР) ################\n")
print('countriesDf:') # отображаем датафрейм, потом массив numpy

print(countriesDf.head())
print('countriesNp:')
print(countriesNp[:5])

countriesDf['Region'].value_counts().plot(kind='bar', title='Кол-во стран по регионам')
plt.xlabel('Регион')
plt.ylabel('Кол-во стран')
plt.show()
print("\nСреднее население в странах:")
print(countriesDf['Population'].mean())
# litw-win
litwData = []
with open('litw-win.txt') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2 and parts[0].isdigit():
            litwData.append([int(parts[0]), parts[1]])
litwDf = pd.DataFrame(litwData, columns=['count', 'word'])
litwNp = litwDf.values

print('litwDf:')
print(litwDf.head())
print('litwNp:')
print(litwNp[:5])

litwDf['wordLength'] = litwDf['word'].apply(len)
wordLengthCounts = litwDf.groupby('wordLength')['count'].sum()
wordLengthCounts.plot(kind='bar', title='Количество слов по длине слова')
plt.xlabel('Длина слова')
plt.ylabel('Количество слов')
plt.show()

print(f'среднее значение по первому столбцу в litwDf: {litwDf['count'].mean()}' )

# addres-book-q
with open('addres-book-q.xml', 'r', encoding='utf-8') as f:
    xmlData = f.read()

soup = BeautifulSoup(xmlData, 'xml')
addresses = soup.find_all('address')

# Извлечение информации в структуру данных
address_data = []
for address in addresses:
    country = address.find_parent('country')['name']
    name = address.find('name').text
    email = address.find('email').text
    position = address.find('position').text
    company = address.find('company').text
    phones = [phone.text for phone in address.find_all('phone')]

    address_data.append({
        'Country': country,
        'Name': name,
        'Email': email,
        'Position': position,
        'Company': company,
        'Phones': phones
    })

addressDf = pd.DataFrame(address_data)
addressNp = addressDf.values


print('addresBookDf:')
print(addressDf.head())
print('addresBookNp:')
print(addressNp[:5])

countryCounts = addressDf['Country'].value_counts() # берём страны, затем отделяем значения т.е. адреса
countryCounts.plot(kind='bar', title='Количество адресов по странам')
plt.xlabel('Страна')
plt.ylabel('Количество адресов')
plt.show()

print(f'Среднее количество адресов на страну: {countryCounts.mean()}')
print("\n\n")

#############
# ЗАДАНИЕ №4 (2 ур.)
#############
# спойлер! я не знаю, можно ли пользоваться библиотекой Levenshtein. вроде на лекциях она не упоминалась, значит нельзя

import re

def levenshteinDistance(s1, s2):
    len1, len2 = len(s1), len(s2)
    dp = [[0]*(len2+1) for _ in range(len1+1)]
    for i in range(len1+1):
        dp[i][0] = i
    for j in range(len2+1):
        dp[0][j] = j
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i-1][j] + 1,      # удаление
                           dp[i][j-1] + 1,      # вставка
                           dp[i-1][j-1] + cost) # замена
    return dp[len1][len2]

def splitIntoSentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]

def findCloseSentencePairs(sentences, maxDistance=3, maxLength=40, minPairs=3):
    shortSentences = [s for s in sentences if len(s) <= maxLength]
    pairs = []
    n = len(shortSentences)
    for i in range(n):
        s1 = shortSentences[i]
        len1 = len(s1)
        for j in range(i+1, n):
            s2 = shortSentences[j]
            len2 = len(s2)
            if abs(len1 - len2) <= maxDistance:
                dist = levenshteinDistance(s1, s2)
                if 0 < dist <= maxDistance:
                    pairs.append((s1, s2, dist))
                    if len(pairs) >= minPairs:
                        return pairs
    return pairs

with open('AnnaKarenina_.txt', encoding='utf-8') as f:
    text = f.read()

sentences = splitIntoSentences(text)
pairs = findCloseSentencePairs(sentences)

print("################ ЗАДАНИЕ 4 (2 УР) ################\n")
for i, (s1, s2, dist) in enumerate(pairs, 1):
    print(f'Пара {i}:')
    print(f'  Предложение 1: {s1}')
    print(f'  Предложение 2: {s2}')
    print(f'  Расстояние Левенштейна: {dist}\n')

print("\n\n")

#############
# ЗАДАНИЕ №6 (2 ур.)
#############

import nltk
from collections import Counter

nltk.download('stopwords')
from nltk.corpus import stopwords

with open('AnnaKarenina_.txt', encoding='utf-8') as f:
    text = f.read().lower()

words = text.split()

freqCounter = Counter(words)
mostCommon200 = freqCounter.most_common(200)
print("################ ЗАДАНИЕ 6 (2 УР) ################\n")
print("200 самых частых слов с их частотами:", mostCommon200)
for word, freq in mostCommon200:
    print(f"{word}: {freq}")

stopWords = set(stopwords.words('english'))

nonStopWords = [word for word, freq in mostCommon200 if word not in stopWords]

print("\nСлова из топ-200, не входящие в список стоп-слов:")
for word in nonStopWords:
    print(word)

print("\n\n")

#############
# ЗАДАНИЕ №7 (2 ур.)
#############

import re

def findSpecWords(text):
    # \b - граница слова
    # [a-z]+ - одна или более латинских строчных букв
    # _ - подчеркивание
    # @+ - один или более символов "@"
    # \b - граница слова
    pattern = r'(?<![a-zA-Z0-9_@])([a-z]+_@+)(?=\s|$)'
    return re.findall(pattern, text)
print("################ ЗАДАНИЕ 7 (2 УР) ################\n")
examples = [
    "hello_@ world test_@@@ foo_bar_@ baz_@",
    "abc_@ def_@@ ghi_@ jkl_mno_@ pqr_@ stu_@@@",
    "one_@ two_@@ three_@ four_@ five_@@@"
]

# Контрпримеры (не должны находиться)
cntrExamples = [
    "Hello_@ (с заглавной буквы)",
    "foo_bar (нет @ после _)",
    "foo__@ (два подчеркивания)",
    "foo_@@@bar (нет границы слова после @)",
    "foo_@1 (цифра после @)",
    "foo_@_bar (ещё одно подчеркивание после @)",
    "foo_@! (спецсимвол после @)",
    "foo_@bar (буквы после @)",
    "foo_@ bar_@baz"
]
print("Примеры:")
for text in examples:
    print(f"Текст: {text}")
    print("Найдено:", findSpecWords(text))
    print()

print("Контрпримеры:")
for text in cntrExamples:
    print(f"Текст: {text}")
    print("Найдено:", findSpecWords(text))
    print()


#############
# ЗАДАНИЕ №5 (2 ур.)
#############
# теоретически оно работает, фактически мне выбивает No module named 'pkg_resources'
# ПОТОМУ ОНО В КОНЦЕ, ЧТОБЫ МОЖНО БЫЛО ПРОВЕРИТЬ ВСЁ ОСТАЛЬНОЕ!
import pymorphy2
from collections import Counter

morph = pymorphy2.MorphAnalyzer()

with open('AnnaKarenina_.txt', encoding='utf-8') as f:
    text = f.read()

words = text.split()

targetName = 'Anna'
targetNameLower = targetName.lower()

# Меморизация для ускорения
cache = {}

def getParse(word):
    if word not in cache:
        cache[word] = morph.parse(word)[0]
    return cache[word]

formsCount = Counter()

for word in words:
    if len(word) < 3:  # для ускорения — пропускаем слишком короткие слова
        continue
    parsed = getParse(word)
    lemma = parsed.normal_form
    if lemma == targetNameLower:
        case = parsed.tag.case
        formsCount[(word, case)] += 1

print("################ ЗАДАНИЕ 5 (2 УР) ################\n")
print(f'Формы слова "{targetName}" и частоты по падежам:')
for (form, case), count in formsCount.most_common():
    caseStr = case if case else 'нет падежа'
    print(f'{form} ({caseStr}): {count}')



