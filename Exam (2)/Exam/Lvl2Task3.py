import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# === Шаг 1: Чтение XML ===
tree = ET.parse("addres-book-q.xml")
root = tree.getroot()

data = []
for country in root.findall("country"):
    for addr in country.findall("address"):
        name = addr.find("name").text
        gender = addr.find("gender").text
        email = addr.find("email").text
        position = addr.find("position").text
        company = addr.find("company").text
        phones = [phone.text for phone in addr.find("phones").findall("phone")]
        country_name = country.get("name")

        data.append({
            "name": name,
            "gender": gender,
            "email": email,
            "position": position,
            "company": company,
            "phones": phones,
            "country": country_name
        })

# === Шаг 2: Преобразование в Pandas DataFrame ===
df = pd.DataFrame(data)

print("📄 DataFrame:\n", df)

# === Шаг 3: NumPy массив ===
np_data = df.to_numpy()
print("\n📦 NumPy массив:\n", np_data)

# === Шаг 4: Визуализация ===
# График количества людей по странам
df["country"].value_counts().plot(kind="bar", title="Количество адресов по странам")
plt.ylabel("Количество")
plt.xlabel("Страна")
plt.tight_layout()
plt.show()