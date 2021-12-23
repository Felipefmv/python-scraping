from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


df = pd.read_excel(
    r"C:\Users\felip\OneDrive\Documentos\exercicios\Padre Inácio MEDICO HOSPITALAR.xlsx")

lastLine = len(df.index)
lista = []
for i in range(lastLine):
    if pd.isna(df.iloc[i, 4]) or df.iloc[i, 4] == 0:
        lista.append(i)

df.drop(index=lista, inplace=True)
df.drop(df.index[len(df)-1], inplace=True)
df.drop(df.index[0], inplace=True)
df2 = df.reset_index(drop=True)

print(df2)
exit()
