from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.xbox.com/pt-BR/games/all-games")
time.sleep(30)

infosLista = driver.find_elements(By.CLASS_NAME, "context-game")
nomesLista = driver.find_elements(By.XPATH, "//a[@class='gameDivLink']")

nomes = []
for nome in nomesLista:
    nomes.append(nome.get_attribute("data-clickname"))


classificacoes = []
precos = []
datasLancamento = []
for info in infosLista:
    classificacoes.append(info.get_attribute("data-rating"))
    precos.append(info.get_attribute("data-listprice"))
    datasLancamento.append(info.get_attribute("data-releasedate"))

print("Nomes:")
print(nomes)
print("\nClassificações:")
print(classificacoes)
print("\nPreços:")
print(precos)
print("\nDatas de lançamento:")
print(datasLancamento)