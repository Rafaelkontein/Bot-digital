from  selenium import  webdriver
from time import sleep
import pyautogui as py

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )
    def acessar(self, site):
        self.chrome.get(site)


    def login(self):
        camp_nome=self.chrome.find_element_by_id('login')
        camp_senha=self.chrome.find_element_by_id('password')
        camp_entrar=self.chrome.find_element_by_class_name('jss10')
        camp_nome.send_keys('t.i')
        camp_senha.send_keys('179202*')
        camp_entrar.click()


    def proposta(self):
        camp_cliente= self.chrome.find_element_by_css_selector('#menu-100 > div > div > div > ul:nth-child(2) > li > a > div > small')
        sleep(5)
        camp_cliente.click()


    def atualizar(self):
        py.press('f5')

    def abrir(self):
        py.press('f11')

    def pontos(self):

        pontos= self.chrome.find_element_by_css_selector('#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(1) > td:nth-child(10) > div > button > span.jss134')
        pontos.click()
    def visualizar(self):
        visualizar = self.chrome.find_element_by_css_selector('body > div.jss71.menu-suspenso > div.jss39.jss69.jss49.jss40.jss70 > ul > li:nth-child(1)')
        visualizar.click()
if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
    chrome.login()
    sleep(4)
    chrome.proposta()
    sleep(2)
    chrome.atualizar()
    sleep(1)
    chrome.abrir()
    sleep(5)
    chrome.pontos()
    chrome.visualizar()