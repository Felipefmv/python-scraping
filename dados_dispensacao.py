from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

email = ""
senha = ""

# chegando na página de cadastros
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get("https://scaweb.saude.gov.br/scaweb/")
search_elem = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "acessar")))
# preencher email e senha aqui

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

menu = driver.find_element(By.ID,"j_id29:j_id48:menuDrop_21_span")
submenu = driver.find_element(By.ID,"j_id29:j_id48:menuItem_22:anchor")
ActionChains(driver).move_to_element(menu).click(submenu).perform()

# função para pesqisar e retornar a data de nascimento

cns = pd.read_excel(r"C:\Planilhas\sus insulina outubro.xlsx")

i = 0
for i in cns.index:
    sus = cns.iloc[i, 1]
    driver.find_element(By.NAME,"dispensacaoForm:nuCartaoSus").clear()
    driver.find_element(By.NAME,
        "dispensacaoForm:nuCartaoSus").send_keys(str(sus))
    driver.find_element(By.NAME,
        "dispensacaoForm:j_id299").send_keys(Keys.RETURN)
    if driver.find_elements(By.ID,"dispensacaoForm:lista:0:visualizarItem"):
        driver.find_element(By.ID,
            "dispensacaoForm:lista:0:visualizarItem").send_keys(Keys.RETURN)
        age = driver.find_element(By.ID,
            "dispensacaoForm:dtNascimento").get_attribute('value')
        cns.at[i, 2] = str(age)
        driver.back()
    else:
        driver.find_element(By.ID,
            "dispensacaoForm:lista:0:editarItem").send_keys(Keys.RETURN)
        age = driver.find_element(By.ID,
            "dispensacaoForm:dtNascimento").get_attribute('value')
        cns.at[i, 2] = str(age)
        driver.back()

print(cns)
cns.to_excel("resultado10.xlsx")
