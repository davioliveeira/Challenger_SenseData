from operator import contains
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from seleniumbase import BaseCase
# configurando o browser para utilização no selenium
url= 'https://www.saucedemo.com'
config = Options()
config.add_argument("start-maximized")
# config.add_argument('--headless')
browser= webdriver.Chrome(options= config)
# browser.get(url)


# Realizar login
def login(user,password):
    nome_usuario= browser.find_element_by_name('user-name')
    nome_usuario.send_keys(f'{user}')
    sleep(2)
    senha= browser.find_element_by_name('password')
    senha.send_keys(f'{password}')
    sleep(2)
    botao_login= browser.find_element_by_name('login-button')
    botao_login.click()

# login('standard_user','secret_sauce')    
# sleep(2)

# Ordenar os produtos pelo valor (low to high) 
def OrdenarProduto():
    change_filters = browser.find_element_by_xpath("//*[@class='product_sort_container']//*[@value='lohi']") #Seleciona o filtro de ordem por produtos low to hight
    change_filters.click() 

# OrdenarProduto()
# sleep(2)

# Adicionar os seguintes produtos ao carrinho: Sauce Labs Onesie e Test.allTheThings() T-Shirt (Red)
def addProdutos(produto1,produto2):
    login('standard_user','secret_sauce')
    sleep(2)   

    # adiciona ao carrinho o produto "Sauce Labs Oneise"
    button_add_cart= browser.find_element(By.XPATH, f'//*[@id="inventory_container"]//*[@class="inventory_item_name"][contains (., "{produto1}")]/../../../div[2]/button')
    button_add_cart.click()

    # adiciona ao carrinho o produto "Test.allTheThings() T-Shirt (Red)"
    button_add_cart= browser.find_element(By.XPATH, f'//*[@id="inventory_container"]//*[@class="inventory_item_name"][contains (., "{produto2}")]/../../../div[2]/button')
    button_add_cart.click()

addProdutos('Sauce Labs Onesie','Test.allTheThings() T-Shirt (Red)')

def efetuaCompra():
    icon_cart= browser.find_element_by_class_name('shopping_cart_link')
    icon_cart.click()
    sleep(2)
    btn_checkout= browser.find_element_by_id('checkout')
    btn_checkout.click()
    sleep(1)
    input_name = browser.find_element_by_id('first-name')
    input_name.send_keys('Davi')
    sleep(1)
    input_last_name= browser.find_element_by_id('last-name')
    input_last_name.send_keys('Oliveira')
    sleep(1)
    postal_code= browser.find_element_by_id('postal-code')
    postal_code.send_keys('6000000')
    sleep(1)
    btn_continue= browser.find_element_by_id('continue')
    btn_continue.click()
    sleep(1)
    btn_finish= browser.find_element_by_id('finish')
    btn_finish.click()
    
    




def kaka():
    open('www.google.com')


kaka()