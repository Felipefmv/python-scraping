from numpy import string_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
menu = driver.find_element_by_id("j_id29:j_id48:menuDrop_1_span")
submenu = driver.find_element_by_id("j_id29:j_id48:menuItem_7:anchor")
ActionChains(driver).move_to_element(menu).click(submenu).perform()

# função para pesqisar e retornar a data de nascimento
wait = WebDriverWait(driver, 100)
cns = pd.read_excel(r"C:\Users\felip\OneDrive\Documentos\na porta.xlsx")


i = 210
# for i in cns.index:
while i < 215:
    sus = cns.iloc[i, 1]
    wait.until(EC.visibility_of_element_located((By.ID, "pacienteForm:cns")))
    # driver.find_element_by_name("pacienteForm:cns").clear()
    driver.find_element_by_name(
        "pacienteForm:cns").send_keys(Keys.CONTROL + "a")
    driver.find_element_by_name("pacienteForm:cns").send_keys(Keys.DELETE)
    # driver.find_element_by_name("pacienteForm:cns").click()
    for j in str(sus):
        driver.find_element_by_name("pacienteForm:cns").send_keys(j)
    # driver.find_element_by_name("pacienteForm:cns").send_keys(str(sus))

    driver.find_element_by_name("pacienteForm:j_id289").click()

    if driver.find_elements_by_id("pacienteForm:j_id297:lista:0:editarItem"):
        driver.find_element_by_id(
            "pacienteForm:j_id297:lista:0:editarItem").click()
        wait.until(EC.presence_of_element_located(
            (By.ID, "pacienteForm:nuCpf")))
        ident = driver.find_element_by_id(
            "pacienteForm:nuCpf").get_attribute("value")
        age = driver.find_element_by_id(
            "pacienteForm:dtNascInputDate").get_attribute("value")
        cns.at[i, 3] = str(ident)
        cns.at[i, 2] = str(age)

        driver.back()
    i += 1

cns = cns.drop(cns.columns[[0]], axis=1)
cns.to_excel("na porta.xlsx")
