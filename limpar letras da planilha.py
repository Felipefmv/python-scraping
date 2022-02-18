from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import re


df = pd.read_excel(
    r"C:\Users\felip\Downloads\RELAÇÃO DE MEDICAMENTOS.xlsx")

rows = len(df)
columns = len(df.columns)

for i in range(1, rows):
    for j in range(4, columns):
        cell = df.iloc[i, j]
        string = str(cell)
        if not pd.isna(df.iloc[i, j]):
            newCell = ''.join(re.findall(r'\d+', string))
            df.iloc[i, j] = newCell

df.to_excel("Relação de Medicamentos.xlsx")
exit()
