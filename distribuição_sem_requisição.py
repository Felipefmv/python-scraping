from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

# chegando na página de cadastros
driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get("https://scaweb.saude.gov.br/scaweb/")
# preencher email e senha aqui

driver.find_element_by_name("ds_email").send_keys(
    "")
driver.find_element_by_name("ds_senha_usuario").send_keys("")


driver.find_element_by_name("acessar").send_keys(Keys.RETURN)
driver.find_element_by_id("sd3").send_keys(Keys.RETURN)
driver.find_element_by_id("proceed-button").send_keys(Keys.RETURN)
alerts = driver.switch_to.alert
alerts.accept()
menu = driver.find_element_by_id("j_id29:j_id48:menuDrop_13")
submenu = driver.find_element_by_id("j_id29:j_id48:menuItem_15")
ActionChains(driver).move_to_element(menu).click(submenu).perform()

time.sleep(10)

# organizar dados da planilha

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


a = [10, 20, 30, 40, 50, 60]
b = 8
c = 1
# iterar pelo produtos
for j in df2.index:
    code = df2.iat[j, 0]
    amount = df2.iat[j, 5]
    # preencher pedido
    if j in a:
        nextPage = driver.find_element_by_xpath(
            "/html/body/div["+str(c)+"1]/div[3]/div[2]/form/div/div/div/table/tbody/tr/td["+str(b)+"]")
        nextPage.click()
        time.sleep(3)
        b += 1
        c += 1
    driver.find_element_by_id(
        "requisicaoForm:itens:"+str(j)+":item_produto_dsProduto").send_keys(code)
    driver.find_element_by_id(
        "requisicaoForm:itens:"+str(j)+":fireItem_produto_coSeqProdutoSuggest").send_keys(Keys.RETURN)

    time.sleep(5)

    driver.find_element_by_id(
        "requisicaoForm:itens:"+str(j)+":item_produto_coSeqProdutoSuggest:0:j_id306").click()
    driver.find_element_by_id(
        "requisicaoForm:itens:"+str(j)+":item_qtSolicitado").send_keys(amount)
    driver.find_element_by_id("requisicaoForm:addItem").click()

    time.sleep(5)
exit()
