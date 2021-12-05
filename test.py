from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


df = pd.read_excel(
    r"C:\Users\felip\OneDrive\Documentos\exercicios\teste_pedido.xlsx")

lista = []
for i in range(143):
    if pd.isna(df.iloc[i, 5]):
        lista.append(i)

df.drop(index=lista, inplace=True)
df.drop(df.index[len(df)-1], inplace=True)
df.drop(df.index[0], inplace=True)
df2 = df.reset_index(drop=True)

for j in df2.index:
    code = df2.iat[j, 0]
    amount = df2.iat[j, 5]
