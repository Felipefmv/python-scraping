import pandas as pd


df1 = pd.read_excel(
    r"C:\Users\felip\Downloads\farmácia central março\07-11.xls")
df1.drop(columns=df1.columns[[0, 1, 2]], axis=1, inplace=True)
print(df1)

lastLine = len(df1.index)
lista = []
for i in range(lastLine):
    value = str(df1.iloc[i, 8])

    if value != "ATENDIDO":
        lista.append(i)

df1.drop(index=lista, inplace=True)

df2 = pd.read_excel(
    r"C:\Users\felip\Downloads\farmácia central março\21-25.xls")
df2.drop(columns=df2.columns[[0, 1, 2]], axis=1, inplace=True)
print(df2)

lastLine = len(df2.index)
lista = []
for i in range(lastLine):
    value = str(df2.iloc[i, 8])

    if value != "ATENDIDO":
        lista.append(i)

df2.drop(index=lista, inplace=True)

df3 = pd.read_excel(
    r"C:\Users\felip\Downloads\farmácia central março\14-18.xls")
df3.drop(columns=df3.columns[[0, 1, 2]], axis=1, inplace=True)
print(df3)

lastLine = len(df3.index)
lista = []
for i in range(lastLine):
    value = str(df3.iloc[i, 8])

    if value != "ATENDIDO":
        lista.append(i)

df3.drop(index=lista, inplace=True)

df4 = pd.read_excel(
    r"C:\Users\felip\Downloads\farmácia central março\01-04.xls")
df4.drop(columns=df4.columns[[0, 1, 2]], axis=1, inplace=True)
print(df4)

lastLine = len(df4.index)
lista = []
for i in range(lastLine):
    value = str(df4.iloc[i, 8])

    if value != "ATENDIDO":
        lista.append(i)

df4.drop(index=lista, inplace=True)

df5 = pd.read_excel(
    r"C:\Users\felip\Downloads\farmácia central março\28-31.xls")
df5.drop(columns=df5.columns[[0, 1, 2]], axis=1, inplace=True)
print(df5)

lastLine = len(df5.index)
lista = []
for i in range(lastLine):
    value = str(df5.iloc[i, 8])

    if value != "ATENDIDO":
        lista.append(i)

df5.drop(index=lista, inplace=True)

frames = [df1, df2, df3, df4, df5]
result = pd.concat(frames)
result.to_excel("farmácia central março.xlsx")
exit()
