from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

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
menu = driver.find_element_by_id("j_id29:j_id48:menuDrop_21_span")
submenu = driver.find_element_by_id("j_id29:j_id48:menuItem_22:anchor")
ActionChains(driver).move_to_element(menu).click(submenu).perform()

# função para pesqisar e retornar a data de nascimento

cns = pd.read_excel(r"C:\Planilhas\sus insulina outubro.xlsx")

i = 0
for i in cns.index:
    sus = cns.iloc[i, 1]
    driver.find_element_by_name("dispensacaoForm:nuCartaoSus").clear()
    driver.find_element_by_name(
        "dispensacaoForm:nuCartaoSus").send_keys(str(sus))
    driver.find_element_by_name(
        "dispensacaoForm:j_id299").send_keys(Keys.RETURN)
    if driver.find_elements_by_id("dispensacaoForm:lista:0:visualizarItem"):
        driver.find_element_by_id(
            "dispensacaoForm:lista:0:visualizarItem").send_keys(Keys.RETURN)
        age = driver.find_element_by_id(
            "dispensacaoForm:dtNascimento").get_attribute('value')
        cns.at[i, 2] = str(age)
        driver.back()
    else:
        driver.find_element_by_id(
            "dispensacaoForm:lista:0:editarItem").send_keys(Keys.RETURN)
        age = driver.find_element_by_id(
            "dispensacaoForm:dtNascimento").get_attribute('value')
        cns.at[i, 2] = str(age)
        driver.back()

print(cns)
cns.to_excel("resultado10.xlsx")
