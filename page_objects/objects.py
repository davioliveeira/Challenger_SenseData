from selenium import webdriver
from abc import ABC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#========================================================================================#
class PageElements(ABC):
    def __init__(self,webdriver,url=''):
        self.webdriver = webdriver
        self.url = url

    # INICIAR O BROWSER E LOGAR//P/ DEIXAR AS AÇOES INDEPENDENTES   
        # def initBrowser(self):
        #     self.url= 'https://www.saucedemo.com'
        #     config = Options()
        #     config.add_argument("start-maximized")
        #     browser= self.webdriver.Chrome(options= config)
        #     browser.get(url)
        #     # FAZ O LOGIN 
        #     site = dadosLogin(browser, url)
        #     site.open()
        #     site.executa_login('standard_user','secret_sauce')
        #     url= 'https://www.saucedemo.com'
        #     site= dadosLogin(browser,url=url)  

    def open(self):
        self.webdriver.get(self.url)

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)

class dadosLogin(PageElements): 
    # armazena locators para efetuar o login
    user = (By.NAME,'user-name')
    senha = (By.NAME,'password')
    btn_login = (By.NAME,'login-button')
    
    
    def executa_login(self, user, senha):
        # insere os valores recebidos nos campos
        self.webdriver.find_element(*self.user).send_keys(user)
        sleep(1)
        self.webdriver.find_element(*self.senha).send_keys(senha)
        sleep(1)
        # clica no btn de login 
        self.webdriver.find_element(*self.btn_login).click()

class OrdenarProduto(PageElements):
    
    # acessa a barra de filtro e armazena o filtro desejado
    filter = ( By.XPATH, "//*[@class='product_sort_container']//*[@value='lohi']")

    def execute_OP(self):        
        # seleciona o filtro escolhido 
        sleep(3)
        self.webdriver.find_element(*self.filter).click()

class AddCarrinho(PageElements):
    
    # armazena o btn de Add ao carrinho do Respectivo produto
    btn_add_produto1 = By.XPATH, '//*[@id="inventory_container"]//*[@class="inventory_item_name"][contains (., "Sauce Labs Onesie")]/../../../div[2]/button'
    btn_add_produto2 = By.XPATH, '//*[@id="inventory_container"]//*[@class="inventory_item_name"][contains (., "Test.allTheThings() T-Shirt (Red)")]/../../../div[2]/button'
    
    def coloca_carrinho(self):
        # adiciona ao carrinho o produto "Sauce Labs Onesie"
        sleep(2)
        self.webdriver.find_element(*self.btn_add_produto1).click()
        # adiciona ao carrinho o produto "Test.allTheThings() T-Shirt (Red)"
        sleep(2)
        self.webdriver.find_element(*self.btn_add_produto2).click()

class efetuaCompra(PageElements):
    # armazena locators para finalizar a compra:

    icon_cart = By.CLASS_NAME,'shopping_cart_link',
    btn_checkout = By.ID, 'checkout',
    name = By.ID, 'first-name',
    last_name = By.ID,'last-name',
    postal_code = By.ID, 'postal-code',
    btn_continue = By.ID,'continue',
    btn_finish = By.ID,'finish'

    def finalizaCompra(self,name,last_name,postal_code):
        
        #Faz as devidas interações com os locators efetuando a compra:
        self.webdriver.find_element(*self.icon_cart).click()
        sleep(1)
        self.webdriver.find_element(*self.btn_checkout).click()
        sleep(1)
        self.webdriver.find_element(*self.name).send_keys(name)
        sleep(1)
        self.webdriver.find_element(*self.last_name).send_keys(last_name)
        sleep(1)
        self.webdriver.find_element(*self.postal_code).send_keys(postal_code)
        
        sleep(2)
        self.webdriver.find_element(*self.btn_continue).click()
        sleep(2)
        self.webdriver.find_element(*self.btn_finish).click()

    

