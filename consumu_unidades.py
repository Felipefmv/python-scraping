import pandas as pd

while True:
    try:
        arqu = input("Nome do arquivo: ")
        df1 = pd.read_excel(
            r"C:\Users\felip\Downloads\{}".format(arqu), sheet_name="plan3")
        print(df1)
        break
    except FileNotFoundError:
        print("Arquivo não encontrado, tente novamente.")

for i in df1.index:
    arquivo = df1.iloc[i, 0] + ".xls"
    df = pd.read_excel(
        r"C:\Users\felip\Downloads\{}".format(arquivo))
    print(df)
