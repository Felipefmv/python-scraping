from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

email = ""
senha = ""

df = pd.read_excel(
    r"C:\Users\felip\OneDrive\Documentos\exercicios\PEDIDO MEDICACAO.xlsx")
driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
wait = WebDriverWait(driver, 20)

driver.get("https://scaweb.saude.gov.br/scaweb/")
driver.find_element_by_name("ds_email").send_keys(email)
driver.find_element_by_name("ds_senha_usuario").send_keys(senha)
driver.find_element_by_name("acessar").send_keys(Keys.RETURN)
driver.find_element_by_id("sd3").send_keys(Keys.RETURN)
driver.find_element_by_id("proceed-button").send_keys(Keys.RETURN)
alerts = driver.switch_to.alert
alerts.accept()
menu = driver.find_element_by_id("j_id29:j_id48:menuDrop_13")
submenu = driver.find_element_by_id("j_id29:j_id48:menuItem_15")
ActionChains(driver).move_to_element(menu).click(submenu).perform()

wait.until(EC.element_to_be_clickable(
    (By.ID, "requisicaoForm:itens:0:item_produto_dsProduto")))


lastLine = len(df.index)
lista = []
for i in range(lastLine):
    if pd.isna(df.iloc[i, 4]) or df.iloc[i, 4] == 0:
        lista.append(i)

df.drop(index=lista, inplace=True)
df.drop(df.index[len(df)-1], inplace=True)
df.drop(df.index[0], inplace=True)
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

    driver.find_element_by_id(
        "requisicaoForm:itens:"+str(j)+":fireItem_produto_coSeqProdutoSuggest").send_keys(Keys.RETURN)

    wait.until(EC.element_to_be_clickable((By.ID, "requisicaoForm:itens:" +
               str(j)+":item_produto_coSeqProdutoSuggest:0:j_id306"))).click()

    driver.find_element_by_id(
        "requisicaoForm:itens:"+str(j)+":item_qtSolicitado").send_keys(amount)
    driver.find_element_by_id("requisicaoForm:addItem").click()

exit()
