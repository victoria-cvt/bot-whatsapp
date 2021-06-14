# bibliotecas
from selenium import webdriver
import time     
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 

# iniciando navegação
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

#Definir quem e o que recebe
contatos = ['Contato']
mensagem = 'Olá, prazer em conhecê-lo :D'
def buscar_contato(contato):
    pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(1.5)
    pesquisa.click()
    pesquisa.send_keys(contato)
    pesquisa.send_keys(Keys.ENTER)
    time.sleep(1)
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
