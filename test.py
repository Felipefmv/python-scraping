from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


df = pd.read_excel(
    r"C:\Users\Downloads\.xlsx")

lastLine = len(df.index)
lista = []
for i in range(lastLine):
    value = str(df.iloc[i, 4])

    if pd.isna(df.iloc[i, 4]) or df.iloc[i, 4] == 0 or not value.isalnum() or value.isalpha():
        lista.append(i)

df.drop(index=lista, inplace=True)
df2 = df.reset_index(drop=True)

print(df2)
exit()
