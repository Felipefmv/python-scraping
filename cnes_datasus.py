from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get("https://cnes.datasus.gov.br/pages/estabelecimentos/consulta.jsp")
wait = WebDriverWait(driver, 20)


driver.find_element_by_xpath(
    '/html/body/div[2]/main/div/div[2]/div/form[1]/div[2]/div[1]/div/select').send_keys("Pernambuco")

wait.until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/main/div/div[2]/div/form[1]/div[2]/div[2]/div/select/option[46]')))


driver.find_element_by_xpath(
    '/html/body/div[2]/main/div/div[2]/div/form[1]/div[2]/div[2]/div/select').send_keys("caruaru")

driver.find_element_by_xpath(
    '/html/body/div[2]/main/div/div[2]/div/form[2]/div/button').send_keys(Keys.ENTER)

wait.until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]')))

driver.find_element_by_xpath(
    '/html/body/div[2]/main/div/div[2]/div/div[2]/div[2]/form/div/select').send_keys("30")

paginas = driver.find_element_by_xpath(
    '/html/body/div[2]/main/div/div[2]/div/div[3]/div/div/div/ul/li[10]/a/span').text
data = []
for j in range(1, int(paginas)+1):
    for i in range(1, 31):
        try:
            uf = (driver.find_element_by_xpath(
                '/html/body/div[2]/main/div/div[2]/div/div[3]/table/tbody/tr['+str(i)+']/td[1]').text)
            cidade = (driver.find_element_by_xpath(
                '/html/body/div[2]/main/div/div[2]/div/div[3]/table/tbody/tr['+str(i)+']/td[2]').text)
            cnes = (driver.find_element_by_xpath(
                '/html/body/div[2]/main/div/div[2]/div/div[3]/table/tbody/tr['+str(i)+']/td[3]').text)
            nome = (driver.find_element_by_xpath(
                '/html/body/div[2]/main/div/div[2]/div/div[3]/table/tbody/tr['+str(i)+']/td[4]').text)
            natureza = (driver.find_element_by_xpath(
                '/html/body/div[2]/main/div/div[2]/div/div[3]/table/tbody/tr['+str(i)+']/td[5]').text)
            gestão = (driver.find_element_by_xpath(
                '/html/body/div[2]/main/div/div[2]/div/div[3]/table/tbody/tr['+str(i)+']/td[6]').text)
            atendeSUS = (driver.find_element_by_xpath(
                '/html/body/div[2]/main/div/div[2]/div/div[3]/table/tbody/tr['+str(i)+']/td[7]').text)
            row = [uf, cidade, cnes, nome, natureza, gestão, atendeSUS]
            data.append(row)
        except:
            break
    driver.find_element_by_xpath(
        '/html/body/div[2]/main/div/div[2]/div/div[3]/div/div/div/ul/li[11]/a').click()

df = pd.DataFrame(data, columns=[
                  'UF', 'Município', 'CNES', 'Nome Fantasia', 'Natureza', 'Gestão', 'Atende SUS'])

df.to_excel('exemplo.xlsx')
print('salvo')
