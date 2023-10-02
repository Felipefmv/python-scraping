from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


while True:
    email = input("Email: ")
    senha = input("Senha: ")
    local = input("Local do arquivo: ")

    df = pd.read_excel(local)

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')


    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    driver.get("https://scaweb.saude.gov.br/scaweb/")
    search_elem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "acessar")))

    driver.find_element(By.NAME,"ds_email").send_keys(email)
    driver.find_element(By.NAME,"ds_senha_usuario").send_keys(senha)
    driver.find_element(By.NAME,"acessar").send_keys(Keys.RETURN)
    driver.find_element(By.ID,"sd3").send_keys(Keys.RETURN)


    try:
        element = driver.find_element(By.ID,"proceed-button")
        print("tem elemento")
        driver.find_element(By.ID,"proceed-button").click()
        driver.back()
        driver.find_element(By.ID,"sd3").send_keys(Keys.RETURN)
        driver.find_element(By.ID,"proceed-button").click()
    except:
        print("não tem elemento")
        
    try:
        #tempo
        search_alert = WebDriverWait(driver, 5).until(
                    EC.alert_is_present())
        alerts = Alert(driver)
        alerts.accept()
    except:
        print("erro alerta")

    menu = driver.find_element(By.ID,"j_id29:j_id48:menuDrop_13")
    submenu = driver.find_element(By.ID,"j_id29:j_id48:menuItem_15")
    ActionChains(driver).move_to_element(menu).click(submenu).perform()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "requisicaoForm:itens:0:item_produto_dsProduto")))

    lastLine = len(df.index)
    lista = []
    for i in range(lastLine):
        value = str(df.iloc[i, 4])
        if pd.isna(df.iloc[i, 4]) or df.iloc[i, 4] == 0 or not value.isalnum() or value.isalpha():
            lista.append(i)

    df.drop(index=lista, inplace=True)
    df2 = df.reset_index(drop=True)

    a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
        110, 120, 130, 140, 150, 160, 170, 180]
    b = 8
    c = 1
    print(df2)

    for j in df2.index:
        code = df2.iat[j, 0]
        amount = df2.iat[j, 4]
        if j in a:
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div["+str(
                c)+"1]/div[3]/div[2]/form/div/div/div/table/tbody/tr/td["+str(b)+"]"))).click()

            b += 1
            c += 1
        wait.until(EC.element_to_be_clickable(
            (By.ID, "requisicaoForm:itens:"+str(j)+":item_produto_dsProduto"))).send_keys(code)

        driver.find_element(By.ID,
            "requisicaoForm:itens:"+str(j)+":fireItem_produto_coSeqProdutoSuggest").send_keys(Keys.RETURN)

        if (code == "BR0345099" or code == "BR0277319" or code == "BR0401411"):
            wait.until(EC.element_to_be_clickable((By.ID, "requisicaoForm:itens:" +
                    str(j)+":item_produto_coSeqProdutoSuggest:1:j_id306"))).click()
        else:
            wait.until(EC.element_to_be_clickable((By.ID, "requisicaoForm:itens:" +
                    str(j)+":item_produto_coSeqProdutoSuggest:0:j_id306"))).click()

        driver.find_element(By.ID,
            "requisicaoForm:itens:"+str(j)+":item_qtSolicitado").send_keys(amount)
        driver.find_element(By.ID,"requisicaoForm:addItem").click()

exit()
