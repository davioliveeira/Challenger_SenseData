from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.objects import OrdenarProduto, AddCarrinho, dadosLogin, efetuaCompra

#==================================================================================================

# ESTABELECE AS CONFIGURAÇÕES DO NAVEGADOR 
url= 'https://www.saucedemo.com'
config = Options()
config.add_argument("start-maximized")
# config.add_argument('--headless')
browser= webdriver.Chrome(options= config)
browser.get(url)

# FAZ O LOGIN 
site = dadosLogin(browser, url)
site.open()
site.executa_login('standard_user','secret_sauce')

# ESTABELECE O FILTRO DO PRODUTO COMO LOW TO HIGTH
filtra_produtro= OrdenarProduto(browser)
sleep(5)
filtra_produtro.execute_OP()

add_carrinho = AddCarrinho(browser)
add_carrinho.coloca_carrinho()
sleep(5)

# INSERE OS DADOS E FINALIZA A COMPRA:

compra= efetuaCompra(browser)

compra.finalizaCompra(name='davi',
last_name= 'oliveira',
postal_code= '600000000'
)

browser.close()