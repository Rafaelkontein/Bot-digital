import pyautogui
import selenium.webdriver.common.alert
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
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

    # Fazendo login e acessando caminho
    def login(self):
        try:
            camp_nome=self.chrome.find_element_by_id('login')
            camp_senha=self.chrome.find_element_by_id('password')
            camp_entrar=self.chrome.find_element_by_class_name('jss10')
            camp_nome.send_keys('t.i')
            camp_senha.send_keys('179202*')
            camp_entrar.click()
        except Exception:
            chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
            camp_nome = self.chrome.find_element_by_id('login')
            camp_senha = self.chrome.find_element_by_id('password')
            camp_entrar = self.chrome.find_element_by_class_name('jss10')
            camp_nome.send_keys('t.i')
            camp_senha.send_keys('179202*')
            camp_entrar.click()



    def proposta(self):
        try:
            sleep(2)
            camp_cliente= self.chrome.find_element_by_css_selector('#menu-100 > div > div > div > ul:nth-child(3)')
            sleep(5)
            camp_cliente.click()
        except Exception:
            camp_cliente = self.chrome.find_element_by_css_selector('#menu-100 > div > div > div > ul:nth-child(3)')
            sleep(5)
            camp_cliente.click()


    def atualizar(self):
        py.press('f5')

    def abrir(self):
        py.press('f11')

   # def pontos(self):

    #    pontos= self.chrome.find_element_by_css_selector('#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(1) > td:nth-child(25) > div > button > span.jss134')
     #   pontos.click()
    #def visualizar(self):
     #   visualizar = self.chrome.find_element_by_css_selector('body > div.jss71.menu-suspenso > div.jss39.jss69.jss49.jss40.jss70 > ul > li:nth-child(4)')
      #  visualizar.click()

    def captura_de_campos(self):
        try:
            financiaado = self.chrome.find_element_by_css_selector('#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(1) > td:nth-child(19) > div').text
            CO = self.chrome.find_element_by_css_selector('#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(4) > td:nth-child(12) > div').text
            pesquisa = self.chrome.find_element_by_css_selector('#searchInput')
            pesquisa.send_keys('33478520606')
            pyautogui.press('enter')
            sleep(6)

            pontos = self.chrome.find_element_by_css_selector('#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(1) > td:nth-child(25) > div > button > span.jss134')
            pontos.click()
            visualizar = self.chrome.find_element_by_css_selector('body > div.jss71.menu-suspenso > div.jss39.jss69.jss49.jss40.jss70 > ul > li:nth-child(4)')
            visualizar.click()
            sleep(2)
            #Captura de dados


            cpf = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(1) > input[type=text]').get_attribute('value')
            nome = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(2) > input').get_attribute('value')
            data = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(3) > label:nth-child(1) > input').get_attribute('value')
            genero = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(3) > label:nth-child(3) > select').get_property('value')
            estado1 = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(3) > label:nth-child(2) > select').get_property('value')
            produto = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(3) > select').get_property('value')
            venda = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(4) > select').get_property('value')
            RG = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(4) > label:nth-child(1) > input').get_property('value')
            dataRG = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(4) > label:nth-child(2) > input').get_property('value')
            orgao = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(4) > label:nth-child(3) > input').get_property('value')
            estado = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(4) > label:nth-child(4) > select').get_property('value')
            pai = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(5) > label:nth-child(1) > input').get_property('value')
            mae = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(5) > label:nth-child(2) > input').get_property('value')
            casado = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(5) > label:nth-child(3) > input').get_property('value')
            email = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(6) > label.mr2 > input').get_property('value')
            email2 = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(6) > label:nth-child(2) > input').get_property('value')
            dataemiss = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(1) > input').get_property('value')
            salario = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(2) > input[type=text]').get_property('value')
            datademiss = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(3) > input').get_property('value')
            nacionalidade = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(4) > input').get_property('value')
            naturalidade = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(5) > input').get_property('value')
            cep = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div:nth-child(2) > label.mr2.i-zipcode > input').get_property('value')
            rua = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div:nth-child(2) > label.mr2.i-address > input').get_property('value')
            numero = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div:nth-child(2) > label.mr2.i-number > input').get_property('value')
            bairro = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div.label-grid.i-district > label:nth-child(1) > input').get_property('value')
            cidade = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div.label-grid.i-district > label.mr2.i-city > input').get_property('value')
            est = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div.label-grid.i-district > label.i-state > select').get_property('value')
            numeroTel = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(3) > fieldset > fieldset > div > label:nth-child(1) > input').get_property('value')
            tipotel = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(3) > fieldset > fieldset > div > label:nth-child(2) > select').get_property('value')
            uso = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(3) > fieldset > fieldset > div > label:nth-child(3) > select').get_property('value')
            beneficio = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(1) > input').get_attribute('value')
            senha = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(2) > input').get_property('value')
            especie = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(3) > input[type=tel]').get_property('value')
            UF = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(4) > select').get_property('value')
            salario1 = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(5) > input').get_property('value')
            margem = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(6) > input').get_property('value')
            conta = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(1) > select').get_property('value')
            banco = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(2) > select').get_property('value')
            agencia = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(3) > input').get_property('value')
            numeroconta = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(4) > input').get_property('value')
            print('Capturando dados....')
            sleep(5)

            print(CO)
            print('valor do financiad R${}'.format(financiaado))
            print('CPF: {}'.format(cpf))
            print('Nome: {}'.format(nome))
            print('Data: {}'.format(data))
            print('Genero: {}'.format(genero))
            print('UF: {}'.format(estado))
            print('Produto: {}'.format(produto))
            print('Venda: {}'.format(venda))
            print('Numero de do RG: {}'.format(RG))
            print('Data de emissão : {}'.format(dataRG))
            print('Orgão de emissaão: {}'.format(orgao))
            print('Estado: {}'.format(estado))
            print('Nome do pai: {}'.format(pai))
            print('Nome da Mãe: {}'.format(mae))
            print('Nome de casado: {}'.format(casado))
            print('Email: {}'.format(email))
            print('Segundo email: {}'.format(email2))
            print('Salario:'.format(salario))
            print('Data de demissão: {}'.format(dataemiss))
            print('Data de demissão: {}'.format(datademiss))
            print('Nacionalidade: {} '.format(nacionalidade))
            print('Naturalidade : {}'.format(naturalidade))
            print('CEP: {}'.format(cep))
            print('Rua : {}'.format(rua))
            print('Numero da casa : {}'.format(numero))
            print('Bairro : {}'.format(bairro))
            print('Cidade : {}'.format(cidade))
            print('Estado '.format(est))
            print('Numero de celular : {}'.format(numeroTel))
            print('Tipo de Contato: {}'.format(tipotel))
            print('Uso: {}'.format(uso))
            print('Beneficio: {} '.format(beneficio))
            print('Senha : {}'.format(senha))
            print('Especie do beneficio:'.format(especie))
            print('UF: {}'.format(UF))
            print('Salario: {}'.format(salario1))
            print('Margem: {} '.format(margem))
            print('Conta: {} '.format(conta))
            print('Tipo de banco: {} '.format(banco))
            print('Numero de Agencia: {} '.format(agencia))
            print('Numero da conta : {}'.format(numeroconta))
            print('Estado : {}'.format(estado1))
        except Exception:
            chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
            camp_nome = self.chrome.find_element_by_id('login')
            camp_senha = self.chrome.find_element_by_id('password')
            camp_entrar = self.chrome.find_element_by_class_name('jss10')
            camp_nome.send_keys('t.i')
            camp_senha.send_keys('179202*')
            camp_entrar.click()
            print('Erro a captuar dados')
            print('Tentando novamente.....')
            financiaado = self.chrome.find_element_by_css_selector(
                '#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(1) > td:nth-child(19) > div').text
            CO = self.chrome.find_element_by_css_selector(
                '#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(4) > td:nth-child(12) > div').text
            pesquisa = self.chrome.find_element_by_css_selector('#searchInput')
            pesquisa.send_keys('19838590010')
            pyautogui.press('enter')
            sleep(6)

            pontos = self.chrome.find_element_by_css_selector(
                '#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(1) > td:nth-child(25) > div > button > span.jss134')
            pontos.click()
            visualizar = self.chrome.find_element_by_css_selector(
                'body > div.jss71.menu-suspenso > div.jss39.jss69.jss49.jss40.jss70 > ul > li:nth-child(4)')
            visualizar.click()
            sleep(2)
            # Captura de dados

            cpf = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(1) > input[type=text]').get_attribute(
                'value')
            nome = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(2) > input').get_attribute(
                'value')
            data = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(3) > label:nth-child(1) > input').get_attribute(
                'value')
            genero = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(3) > label:nth-child(3) > select').get_property(
                'value')
            estado1 = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(3) > label:nth-child(2) > select').get_property(
                'value')
            produto = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(3) > select').get_property(
                'value')
            venda = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(2) > label:nth-child(4) > select').get_property(
                'value')
            RG = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(4) > label:nth-child(1) > input').get_property(
                'value')
            dataRG = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(4) > label:nth-child(2) > input').get_property(
                'value')
            orgao = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(4) > label:nth-child(3) > input').get_property(
                'value')
            estado = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(4) > label:nth-child(4) > select').get_property(
                'value')
            pai = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(5) > label:nth-child(1) > input').get_property(
                'value')
            mae = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(5) > label:nth-child(2) > input').get_property(
                'value')
            casado = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(5) > label:nth-child(3) > input').get_property(
                'value')
            email = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(6) > label.mr2 > input').get_property(
                'value')
            email2 = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(6) > label:nth-child(2) > input').get_property(
                'value')
            dataemiss = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(1) > input').get_property(
                'value')
            salario = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(2) > input[type=text]').get_property(
                'value')
            datademiss = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(3) > input').get_property(
                'value')
            nacionalidade = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(4) > input').get_property(
                'value')
            naturalidade = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(1) > div:nth-child(7) > label:nth-child(5) > input').get_property(
                'value')
            cep = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div:nth-child(2) > label.mr2.i-zipcode > input').get_property(
                'value')
            rua = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div:nth-child(2) > label.mr2.i-address > input').get_property(
                'value')
            numero = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div:nth-child(2) > label.mr2.i-number > input').get_property(
                'value')
            bairro = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div.label-grid.i-district > label:nth-child(1) > input').get_property(
                'value')
            cidade = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div.label-grid.i-district > label.mr2.i-city > input').get_property(
                'value')
            est = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > fieldset:nth-child(2) > div.label-grid.i-district > label.i-state > select').get_property(
                'value')
            numeroTel = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(3) > fieldset > fieldset > div > label:nth-child(1) > input').get_property(
                'value')
            tipotel = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(3) > fieldset > fieldset > div > label:nth-child(2) > select').get_property(
                'value')
            uso = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(3) > fieldset > fieldset > div > label:nth-child(3) > select').get_property(
                'value')
            beneficio = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(1) > input').get_attribute(
                'value')
            senha = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(2) > input').get_property(
                'value')
            especie = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(3) > input[type=tel]').get_property(
                'value')
            UF = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(4) > select').get_property(
                'value')
            salario1 = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(5) > input').get_property(
                'value')
            margem = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(6) > input').get_property(
                'value')
            conta = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(1) > select').get_property(
                'value')
            banco = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(2) > select').get_property(
                'value')
            agencia = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(3) > input').get_property(
                'value')
            numeroconta = self.chrome.find_element_by_css_selector(
                'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(4) > input').get_property(
                'value')
            print('Capturando dados....')
            sleep(5)

            print(CO)
            print('valor do financiad R${}'.format(financiaado))
            print('CPF: {}'.format(cpf))
            print('Nome: {}'.format(nome))
            print('Data: {}'.format(data))
            print('Genero: {}'.format(genero))
            print('UF: {}'.format(estado))
            print('Produto: {}'.format(produto))
            print('Venda: {}'.format(venda))
            print('Numero de do RG: {}'.format(RG))
            print('Data de emissão : {}'.format(dataRG))
            print('Orgão de emissaão: {}'.format(orgao))
            print('Estado: {}'.format(estado))
            print('Nome do pai: {}'.format(pai))
            print('Nome da Mãe: {}'.format(mae))
            print('Nome de casado: {}'.format(casado))
            print('Email: {}'.format(email))
            print('Segundo email: {}'.format(email2))
            print('Salario:'.format(salario))
            print('Data de demissão: {}'.format(dataemiss))
            print('Data de demissão: {}'.format(datademiss))
            print('Nacionalidade: {} '.format(nacionalidade))
            print('Naturalidade : {}'.format(naturalidade))
            print('CEP: {}'.format(cep))
            print('Rua : {}'.format(rua))
            print('Numero da casa : {}'.format(numero))
            print('Bairro : {}'.format(bairro))
            print('Cidade : {}'.format(cidade))
            print('Estado '.format(est))
            print('Numero de celular : {}'.format(numeroTel))
            print('Tipo de Contato: {}'.format(tipotel))
            print('Uso: {}'.format(uso))
            print('Beneficio: {} '.format(beneficio))
            print('Senha : {}'.format(senha))
            print('Especie do beneficio:'.format(especie))
            print('UF: {}'.format(UF))
            print('Salario: {}'.format(salario1))
            print('Margem: {} '.format(margem))
            print('Conta: {} '.format(conta))
            print('Tipo de banco: {} '.format(banco))
            print('Numero de Agencia: {} '.format(agencia))
            print('Numero da conta : {}'.format(numeroconta))
            print('Estado : {}'.format(estado1))

        '''
        #ITAU
        # Entrando no site do Itau
        self.chrome.get('https://www.ibconsigweb.com.br/Index.do?method=prepare')

        # fazendo logiin no itau

        loginn=self.chrome.find_element_by_css_selector('#Table_02 > tbody > tr > td > form > table > tbody > tr:nth-child(1) > td:nth-child(3) > input')
        senhaa=self.chrome.find_element_by_css_selector('#Table_02 > tbody > tr > td > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > font > strong > input')
        loginn.send_keys('CONSIG.61686O ')
        senhaa.send_keys('Digital@2021')
        sleep(30)
        botom=self.chrome.find_element_by_css_selector('#Table_02 > tbody > tr > td > form > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(1) > td:nth-child(3)')
        botom.click()
        proposta=self.chrome.find_element_by_css_selector('#top')
        proposta.click()
        nova=self.chrome.find_element_by_css_selector('#slidingMenu > div > div:nth-child(2) > a:nth-child(1)')
        nova.click()
        entidade=self.chrome.find_element_by_css_selector('#identificacao-form\:orgao\:find\:txt-value')
        entidade.send_keys('1581')
        cpf1=self.chrome.find_element_by_css_selector('#identificacao-form\:cpf')
        cpf1.send_keys(cpf)
        matriculo = self.chrome.find_element_by_css_selector('#identificacao-form\:matricula')
        matriculo.send_keys(beneficio)
        data_nacimento=self.chrome.find_element_by_css_selector('#identificacao-form\:dataDeNascimento')
        data_nacimento.send_keys(data)'''


        # FACTA
        # Entrando no site
        try:
            try:
                chrome.acessar('http://desenv.facta.com.br/sistemaNovo/login.php')
                usuario = self.chrome.find_element_by_css_selector('#login')
                senhaa = self.chrome.find_element_by_css_selector('#senha')
                entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                usuario.send_keys('600045_Beatriz')
                senhaa.send_keys('Dezembro@20')
                entrar.click()
            except Exception:
                chrome.acessar('http://desenv.facta.com.br/sistemaNovo/login.php')
                usuario = self.chrome.find_element_by_css_selector('#login')
                senhaa = self.chrome.find_element_by_css_selector('#senha')
                entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                usuario.send_keys('600045_Beatriz')
                senhaa.send_keys('Dezembro@20')
                entrar.click()
            try:
                print('Acessando a primeira pagina....')
                pyautogui.click(x=550, y=550)
                pyautogui.click(x=550, y=550)
                sleep(2)
                operacional = self.chrome.find_element_by_css_selector('#main-nav > div > ul > li:nth-child(2) > a')
                operacional.click()
                sleep(1)
                cadastro = self.chrome.find_element_by_css_selector('#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(2) > a')
                cadastro.click()
                sleep(1)
                simulacao = self.chrome.find_element_by_css_selector('#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(2) > ul > li:nth-child(2) > a > span')
                simulacao.click()
                sleep(3)
                produto = self.chrome.find_element_by_css_selector('#produto')
                produto.click()
                sleep(2)
                vendadigital = self.chrome.find_element_by_css_selector('#produto > option:nth-child(8)')
                vendadigital.click()
                pyautogui.click(x=550, y=550)
                sleep(2)
                tipo_operacao = self.chrome.find_element_by_css_selector('#tipoOperacao')
                tipo_operacao.click()
                sleep(2)
                novo = self.chrome.find_element_by_css_selector('#tipoOperacao > option:nth-child(4)')
                novo.click()
                pyautogui.click(x=550, y=550)
                sleep(4)
                orgaa = self.chrome.find_element_by_css_selector('#averbador')
                orgaa.click()
                inss = self.chrome.find_element_by_css_selector('#averbador > option:nth-child(27)')
                inss.click()
                pyautogui.click(x=550, y=550)
                sleep(2)
                fig=self.chrome.find_element_by_css_selector('#divContakoWidgetJSPopUpIntegrado > img:nth-child(1)')
                fig.click()
                pyautogui.press('enter')
                sleep(15)
                bancoo = self.chrome.find_element_by_css_selector('#banco')
                bancoo.click()
                sleep(2)
                facta = self.chrome.find_element_by_css_selector('#banco > option:nth-child(7)')
                facta.click()
                pyautogui.click(x=550, y=550)
                sleep(2)
                cpff = self.chrome.find_element_by_css_selector('#cpf')
                cpff.send_keys(cpf)

                pyautogui.click(x=550, y=550)
                sleep(3)
                #data_ = self.chrome.find_element_by_css_selector('#dataNascimento')
                #data_.clear()
                #data_.send_keys(data)
                solicitado = self.chrome.find_element_by_css_selector('#valor')
                solicitado.send_keys(financiaado)
                valor_solicitado = self.chrome.find_element_by_css_selector('#opcaoValor')
                valor_solicitado.click()
                sleep(1.5)
                selecionar = self.chrome.find_element_by_css_selector('#opcaoValor > option:nth-child(2)')
                selecionar.click()
                prazo = self.chrome.find_element_by_css_selector('#prazo')
                prazo.send_keys('84')
                pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                pesquisa.click()
                sleep(5)

                In = self.chrome.find_element_by_css_selector('#myTable > tbody > tr:nth-child(6) > td:nth-child(2)')
                In.click()
                sleep(4)
                btnn = self.chrome.find_element_by_css_selector('#etapa1')
                btnn.click()
            except Exception:
                sleep(1)
                chrome.acessar('http://desenv.facta.com.br/sistemaNovo/login.php')
                sleep(1)
                try:
                    usuario = self.chrome.find_element_by_css_selector('#login')
                    senhaa = self.chrome.find_element_by_css_selector('#senha')
                    entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                    sleep(1)
                    usuario.send_keys('600045_Beatriz')
                    sleep(1)
                    senhaa.send_keys('Dezembro@20')
                    sleep(1)
                    entrar.click()
                except Exception:
                    usuario = self.chrome.find_element_by_css_selector('#login')
                    senhaa = self.chrome.find_element_by_css_selector('#senha')
                    entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                    sleep(1)
                    usuario.send_keys('600045_Beatriz')
                    sleep(1)
                    senhaa.send_keys('Dezembro@20')
                    sleep(1)
                    entrar.click()
                try:
                sleep(2)
                pyautogui.press('f5')
                pyautogui.click(x=550, y=550)
                pyautogui.click(x=550, y=550)
                sleep(2)
                operacional = self.chrome.find_element_by_css_selector('#main-nav > div > ul > li:nth-child(2) > a')
                operacional.click()
                sleep(1)
                cadastro = self.chrome.find_element_by_css_selector(
                    '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(2) > a')
                cadastro.click()
                sleep(1)
                simulacao = self.chrome.find_element_by_css_selector(
                    '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(2) > ul > li:nth-child(2) > a > span')
                simulacao.click()
                sleep(3)
                produto = self.chrome.find_element_by_css_selector('#produto')
                produto.click()
                sleep(2)
                vendadigital = self.chrome.find_element_by_css_selector('#produto > option:nth-child(8)')
                vendadigital.click()
                pyautogui.click(x=550, y=550)
                sleep(2)
                tipo_operacao = self.chrome.find_element_by_css_selector('#tipoOperacao')
                tipo_operacao.click()
                sleep(2)
                novo = self.chrome.find_element_by_css_selector('#tipoOperacao > option:nth-child(4)')
                novo.click()
                pyautogui.click(x=550, y=550)
                sleep(4)
                orgaa = self.chrome.find_element_by_css_selector('#averbador')
                orgaa.click()
                inss = self.chrome.find_element_by_css_selector('#averbador > option:nth-child(27)')
                inss.click()
                pyautogui.click(x=550, y=550)
                sleep(2)
                fig = self.chrome.find_element_by_css_selector('#divContakoWidgetJSPopUpIntegrado > img:nth-child(1)')
                fig.click()
                pyautogui.press('enter')
                sleep(15)
                bancoo = self.chrome.find_element_by_css_selector('#banco')
                bancoo.click()
                sleep(2)
                facta = self.chrome.find_element_by_css_selector('#banco > option:nth-child(7)')
                facta.click()
                pyautogui.click(x=550, y=550)
                sleep(2)
                cpff = self.chrome.find_element_by_css_selector('#cpf')
                cpff.send_keys(cpf)

                pyautogui.click(x=550, y=550)
                sleep(3)
                # data_ = self.chrome.find_element_by_css_selector('#dataNascimento')
                # data_.clear()
                # data_.send_keys(data)
                solicitado = self.chrome.find_element_by_css_selector('#valor')
                solicitado.send_keys(financiaado)
                valor_solicitado = self.chrome.find_element_by_css_selector('#opcaoValor')
                valor_solicitado.click()
                sleep(1.5)
                selecionar = self.chrome.find_element_by_css_selector('#opcaoValor > option:nth-child(2)')
                selecionar.click()
                prazo = self.chrome.find_element_by_css_selector('#prazo')
                prazo.send_keys('84')
                pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                pesquisa.click()
                sleep(5)

                In = self.chrome.find_element_by_css_selector('#myTable > tbody > tr:nth-child(6) > td:nth-child(2)')
                In.click()
                sleep(4)
                btnn = self.chrome.find_element_by_css_selector('#etapa1')
                btnn.click()





            sleep(1)
            alert = self.chrome.switch_to.alert
            alert.accept()
            sleep(1)

            login = self.chrome.find_element_by_css_selector('#tab2 > fieldset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > select').click()
            sleep(1)
            Daine = self.chrome.find_element_by_css_selector('#tab2 > fieldset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > select > option:nth-child(25)').click()

            pyautogui.click(x=550, y=550)

            sleep(2)
            vendedor = self.chrome.find_element_by_css_selector('#vendedor').click()
            vendedorB=self.chrome.find_element_by_css_selector('#vendedor > option:nth-child(6)').click()
            pyautogui.click(x=550, y=550)
            sleep(1.5)
            btnw = self.chrome.find_element_by_css_selector('#etapa_2')
            btnw.click()
            sleep(70)
            cliente = self.chrome.find_element_by_css_selector('#clienteAnalfabeto').click()
            nao = self.chrome.find_element_by_css_selector('#clienteAnalfabeto > option:nth-child(3)').click()
            sleep(1)
            renda = self.chrome.find_element_by_css_selector('#valorDoBeneficio').send_keys(salario)
            sleep(1)
            cepp=self.chrome.find_element_by_css_selector('#cep')
            cepp.click()
            cepp.send_keys(cep)
            sleep(1)
            pesquisaa = self.chrome.find_element_by_css_selector('#pesquisar_cep').click()
            end= self.chrome.find_element_by_css_selector('#endereco').clear()
            sleep(1)
            en=self.chrome.find_element_by_css_selector('#endereco').send_keys(rua)
            sleep(2)
            nuber= self.chrome.find_element_by_css_selector('#numero').clear()
            nube=self.chrome.find_element_by_css_selector('#numero').send_keys('12')
            sleep(2)
            bairrr= self.chrome.find_element_by_css_selector('#bairro').clear()
            bairrrr=self.chrome.find_element_by_css_selector('#bairro').send_keys(bairro)
            sleep(2)
            cidadee= self.chrome.find_element_by_css_selector('#cidade').click()
            pyautogui.press('down')
            pyautogui.press('enter')
            cel = self.chrome.find_element_by_css_selector('#celular')
            cel.click()
            cel1= self.chrome.find_element_by_css_selector('#celular')
            cel1.send_keys(numeroTel)
            sleep(2)
            resi= self.chrome.find_element_by_css_selector('#tipoResidencia').click()
            familiar = self.chrome.find_element_by_css_selector('#tipoResidencia > option:nth-child(3)').click()
            sleep(2)
            emaill=self.chrome.find_element_by_css_selector('#email').click()
            sleep(1)
            emaii= self.chrome.find_element_by_css_selector('#email').send_keys(email)

            sleep(4)
            btn3 = self.chrome.find_element_by_css_selector('#etapa_3')
            btn3.click()
            sleep(10)
            Ramo= self.chrome.find_element_by_css_selector('#id_ramo_atividade_or').click()
            ram= self.chrome.find_element_by_css_selector('#id_ramo_atividade_or > option:nth-child(8)').click()
            sleep(1)
            prof= self.chrome.find_element_by_css_selector('#id_tipo_profissao_or').click()
            prof1= self.chrome.find_element_by_css_selector('#id_tipo_profissao_or > option:nth-child(2)').click()

            sleep(1.5)

            btn4= self.chrome.find_element_by_css_selector('#etapa_4').click()
        except Exception:
            print('erro no processo')








        












if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
    chrome.login()
    sleep(6)
    chrome.proposta()
    sleep(2)
    chrome.atualizar()
    sleep(1)
    chrome.abrir()
    sleep(5)

    chrome.captura_de_campos()