import pyautogui
import selenium.webdriver.common.alert
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
import pygame
import os
import time
from time import sleep
import pyautogui as py
import  pyperclip

inicio=time.time()
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
            sleep(2)
            camp_nome=self.chrome.find_element_by_id('login')
            camp_senha=self.chrome.find_element_by_id('password')
            camp_entrar=self.chrome.find_element_by_class_name('jss10')
            camp_nome.send_keys('t.i')
            camp_senha.send_keys('179202*')
            camp_entrar.click()
            sleep(10)
        except Exception:
            self.chrome.refresh()
            chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
            camp_nome = self.chrome.find_element_by_id('login')
            camp_senha = self.chrome.find_element_by_id('password')
            camp_entrar = self.chrome.find_element_by_class_name('jss10')
            camp_nome.send_keys('t.i')
            camp_senha.send_keys('179202*')
            camp_entrar.click(10)


    def uso(self):
        pyttsx3.speak('Olá Gabriel, sou Lura. No que posso te ajudar?')



        microfone = sr.Recognizer()  # habilita o microfone

        with sr.Microphone() as source:  # usando o microfone

            print('Fale algo:')

            microfone.adjust_for_ambient_noise(source)  # Isso tira os ruidos do abiente

            audio = microfone.listen(source)  # Aqui estamos armazenando o
            try:
                frase = microfone.recognize_google(audio,
                                                   language='pt-BR')  # faz que o o algoritimo reconeça a lingua Brasileira

                print('Ok, você disse:' + frase)
            except sr.UnknownValueError:
                print('desculpa não entendi...')
    def proposta(self):

        try:
            sleep(15)
            camp_cliente = self.chrome.find_element_by_css_selector('#menu-100 > div > div > div > ul:nth-child(3)')
            sleep(5)
            camp_cliente.click()
            self.chrome.refresh()
            sleep(2)
            self.chrome.maximize_window()
            sleep(4)
            status = self.chrome.find_element_by_xpath('//*[@id="filtro-paper"]/div/div[1]/div[8]').click()
            sleep(2)
            aceite = self.chrome.find_element_by_class_name('input-busca-filtro').send_keys('AGUARDANDO DIGITAÇÃO')
            sleep(5)
            aceite = self.chrome.find_element_by_css_selector(
                'body > div.jss71.jss144.jss145 > div.jss39.jss65.jss40.jss147.jss148.jss151 > div.jss321.dialog-filter > label:nth-child(5)').click()
            sleep(3)
            aplicar = self.chrome.find_element_by_css_selector(
                'body > div.jss71.jss144.jss145 > div.jss39.jss65.jss40.jss147.jss148.jss151 > div.jss322 > button.jss105.jss81.jss83.jss86.applyFilters.jss323 > span.jss82').click()
            sleep(3)

            banco = self.chrome.find_element_by_css_selector(
                '#filtro-paper > div > div:nth-child(1) > div:nth-child(4)').click()
            sleep(3)
            aceite = self.chrome.find_element_by_class_name('input-busca-filtro').send_keys('facta')
            sleep(3)
            facta1 = self.chrome.find_element_by_class_name('checkbox-description').click()
            sleep(1)
            plicar = self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/button[2]').click()
            sleep(3)
            data = self.chrome.find_element_by_css_selector('#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div > input[type=text]').click()
            sleep(4)
            seta = self.chrome.find_element_by_css_selector('#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()
            seta = self.chrome.find_element_by_css_selector('#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()
            seta = self.chrome.find_element_by_css_selector('#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()

            data1= self.chrome.find_element_by_css_selector('#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(1) > div.react-datepicker__day.react-datepicker__day--wed').click()
            sleep(3)

            filtro= self.chrome.find_element_by_xpath('//*[@id="filtro-paper"]/div/div[3]/div[2]').click()
            sleep(5)
            menu = self.chrome.find_element_by_css_selector('#topo > button.jss105.jss81.jss90.jss93.hamburguer').click()




            while True:
                      try:
                            sleep(15)
                            aguar = self.chrome.find_element_by_xpath(
                                '//*[@id="main-content"]/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[22]')
                            aguar1 = aguar.get_attribute('innerHTML')
                            digita = 'AGUARDANDO DIGITAÇÃO'


                            if digita in aguar1:
                                print('Tem proposta sim, vou executar realiza a digitção... ')
                                try:
                                    sleep(40)
                                    financiaado = self.chrome.find_element_by_xpath('//*[@id="main-content"]/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[19]').text
                                    print(financiaado)
                                    sleep(3)

                                    pontos = self.chrome.find_element_by_xpath('//*[@id="main-content"]/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[25]/div')
                                    pontos.click()
                                    sleep(5)
                                    editar= self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[2]').click()
                                    sleep(4)
                                    tabela= self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/form/fieldset[1]/div[3]/label[1]/select/option[2]').text
                                    print(tabela)
                                    sleep(3)
                                    quitar= self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/button/span[1]').click()

                                    pontos = self.chrome.find_element_by_xpath(
                                        '//*[@id="main-content"]/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[25]/div')
                                    pontos.click()
                                    cliente = self.chrome.find_element_by_css_selector(
                                        'body > div.jss71.menu-suspenso > div.jss39.jss69.jss49.jss40.jss70 > ul > li:nth-child(4)')
                                    cliente.click()
                                    sleep(10)
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
                                    especie = self.chrome.find_element_by_css_selector('body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div.label-grid.flex-start > label:nth-child(3) > input[type=tel]').get_property('value')
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
                                    banco = self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/form/div[3]/fieldset/fieldset/div[2]/label[2]/select').get_property('value')
                                    agencia = self.chrome.find_element_by_css_selector(
                                        'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(3) > input').get_property(
                                        'value')
                                    numeroconta = self.chrome.find_element_by_css_selector(
                                        'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(4) > input').get_property(
                                        'value')


                                    print('Capturando dados....')
                                    sleep(5)


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
                                    print(especie)
                                    print('UF: {}'.format(UF))
                                    print('Salario: {}'.format(salario1))
                                    print('Margem: {} '.format(margem))
                                    print('Conta: {} '.format(conta))
                                    print('Tipo de banco: {} '.format(banco))
                                    print('Numero de Agencia: {} '.format(agencia))
                                    print('Numero da conta : {}'.format(numeroconta))
                                    print('Estado : {}'.format(estado1))


                                except Exception as e:
                                    print(e)
                                    print('Erro a captuar dados')
                                    print('Tentando novamente.....')
                                    chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
                                    camp_nome = self.chrome.find_element_by_id('login')
                                    camp_senha = self.chrome.find_element_by_id('password')
                                    camp_entrar = self.chrome.find_element_by_class_name('jss10')
                                    camp_nome.send_keys('t.i')
                                    camp_senha.send_keys('179202*')
                                    camp_entrar.click()
                                    sleep(10)
                                    camp_cliente = self.chrome.find_element_by_css_selector(
                                        '#menu-100 > div > div > div > ul:nth-child(3)')
                                    sleep(5)
                                    camp_cliente.click()

                                    financiaado = self.chrome.find_element_by_css_selector(
                                        '#main-content > div:nth-child(1) > div > div.jss39.jss43.jss40.jss246 > div.jss250 > table > tbody > tr:nth-child(1) > td:nth-child(19) > div').text

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
                                    banco = self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/form/div[3]/fieldset/fieldset/div[2]/label[2]/select').text
                                    agencia = self.chrome.find_element_by_css_selector(
                                        'body > div.jss71.modal > div:nth-child(2) > div.modalBody > form > div:nth-child(5) > fieldset > fieldset > div:nth-child(3) > label:nth-child(3) > input').get_property(
                                        'value')
                                    numeroconta = self.chrome.find_element_by_css_selector(
                                        'body > div.jss164.modal.modal-minimizavel > div:nth-child(2) > div.modalBody.modal-propostas > form > fieldset:nth-child(1) > div:nth-child(5) > label.mr2 > selectbody > div.jss164.modal.modal-minimizavel > div:nth-child(2) > div.modalBody.modal-propostas > form > fieldset:nth-child(1) > div:nth-child(5) > label.mr2 > select').get_property(
                                        'value')
                                    tabela = self.chrome.find_element_by_css_selector('body > div.jss164.modal.modal-minimizavel > div:nth-child(2) > div.modalBody.modal-propostas > form > fieldset:nth-child(1) > div:nth-child(5) > label.mr2 > select').get_property('value')
                                    print('Capturando dados....')
                                    sleep(5)

                                    print(tabela)
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
                                        senhaa.send_keys('Dezembro@202')
                                        entrar.click()
                                        sleep(2)
                                    except Exception as e:
                                        chrome.acessar('http://desenv.facta.com.br/sistemaNovo/login.php')
                                        usuario = self.chrome.find_element_by_css_selector('#login')
                                        senhaa = self.chrome.find_element_by_css_selector('#senha')
                                        entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                                        usuario.send_keys('600045_Beatriz')
                                        senhaa.send_keys('Dezembro@202')
                                        entrar.click()
                                        sleep(2)
                                    try:
                                        print('Acessando a primeira pagina....')
                                        sleep(3)
                                        try:
                                            fechar = self.chrome.find_element_by_css_selector(
                                                '#modalMuralAlertas > div > div.modal-footer > button').click()
                                        except Exception:
                                            print('alo')
                                        sleep(3)
                                        operacional = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > a')
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
                                        vendadigital = self.chrome.find_element_by_css_selector(
                                            '#produto > option:nth-child(8)')
                                        vendadigital.click()
                                        pyautogui.click(x=550, y=550)
                                        sleep(2)
                                        tipo_operacao = self.chrome.find_element_by_css_selector('#tipoOperacao')
                                        tipo_operacao.click()
                                        novo = self.chrome.find_element_by_css_selector(
                                            '#tipoOperacao > option:nth-child(4)')
                                        novo.click()
                                        pyautogui.click(x=550, y=550)
                                        sleep(4)
                                        orgaa = self.chrome.find_element_by_css_selector('#averbador')
                                        orgaa.click()

                                        inss = self.chrome.find_element_by_css_selector(
                                            '#averbador > option:nth-child(27)')
                                        inss.click()
                                        pyautogui.click(x=550, y=550)
                                        sleep(2)
                                        try:
                                            fig = self.chrome.find_element_by_css_selector(
                                                '#divContakoWidgetJSPopUpIntegrado > img:nth-child(1)')
                                            fig.click()
                                        except Exception:
                                            print('sem figura')
                                        pyautogui.press('enter')
                                        sleep(15)
                                        try:
                                            bancoo = self.chrome.find_element_by_css_selector('#banco')
                                            bancoo.click()
                                            sleep(3)
                                            facta = self.chrome.find_element_by_css_selector(
                                                '#banco > option:nth-child(7)')
                                            facta.click()
                                            pyautogui.click(x=550, y=550)
                                        except Exception as e:
                                            print(e)
                                            print('erro ao tentar clicar no banco.... ')
                                            print('Tenatando novamente')
                                            sleep(8)
                                            bancoo = self.chrome.find_element_by_css_selector('#banco')
                                            bancoo.click()
                                            sleep(2)
                                            facta = self.chrome.find_element_by_css_selector(
                                                '#banco > option:nth-child(7)')
                                            facta.click()
                                            pyautogui.click(x=550, y=550)
                                        cpff = self.chrome.find_element_by_css_selector('#cpf')
                                        cpff.send_keys(cpf)

                                        pyautogui.click(x=550, y=550)
                                        try:
                                            dataaa = self.chrome.find_element_by_css_selector('#dataNascimento').click()
                                            dataaaa = self.chrome.find_element_by_css_selector(
                                                '#dataNascimento').send_keys(data)
                                            sleep(0.5)
                                            nomee = self.chrome.find_element_by_id('#nomeCliente').click()
                                            nomee = self.chrome.find_element_by_css_selector('#nomeCliente').send_keys(
                                                nome)
                                            pyautogui.click(x=550, y=550)
                                            sleep(3)
                                            solicitado = self.chrome.find_element_by_css_selector('#valor')
                                            solicitado.send_keys(financiaado)
                                            valor_solicitado = self.chrome.find_element_by_css_selector('#opcaoValor')
                                            valor_solicitado.click()
                                            valor_solicitado.send_keys(financiaado)
                                            sleep(1.5)
                                            selecionar = self.chrome.find_element_by_css_selector(
                                                '#opcaoValor > option:nth-child(2)')
                                            selecionar.click()
                                            prazo = self.chrome.find_element_by_css_selector('#prazo')
                                            prazo.send_keys('84')
                                            pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                                            pesquisa.click()
                                            sleep(10)
                                            self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                            sleep(2)
                                            if tabela == 'DESBLOQUEADOS SEM CARENCIA FACTA 2,14, 120 DIAS' or tabela == 'BLOQUEADOS SEM CARENCIA FACTA 2,14 COM 120 DIAS':
                                                In = self.chrome.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[4]')
                                                In.click()
                                            if tabela == 'DESBLOQUEADOS COM CARENCIA FACTA 120 DIA 2,14' or tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS':
                                                In1 = self.chrome.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[6]')
                                                In1.click()
                                            if tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS - 1X A 84X':
                                                In2 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In2.click()
                                            if tabela == 'DIG INSS - NOVO 1,30 - SEM CARENCIA E SEM SEGURO - 1X A 84X':
                                                In3 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In3.click()
                                            else:
                                                print('Tabela incompativel....')


                                            sleep(5)

                                            btnn = self.chrome.find_element_by_css_selector('#etapa1')
                                            btnn.click()
                                        # data_ = self.chrome.find_element_by_css_selector('#dataNascimento')
                                        # data_.clear()
                                        # data_.send_keys(data)
                                        except Exception as e:
                                            print('Campos nome e data preenchidos, continuando....')
                                            solicitado = self.chrome.find_element_by_css_selector('#valor')
                                            solicitado.send_keys(financiaado)
                                            valor_solicitado = self.chrome.find_element_by_css_selector('#opcaoValor')
                                            valor_solicitado.click()
                                            sleep(1.5)
                                            selecionar = self.chrome.find_element_by_css_selector(
                                                '#opcaoValor > option:nth-child(2)')
                                            selecionar.click()
                                            prazo = self.chrome.find_element_by_css_selector('#prazo')
                                            prazo.send_keys('84')
                                            pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                                            pesquisa.click()
                                            sleep(10)
                                            self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                            sleep(2)
                                            if tabela == 'DESBLOQUEADOS SEM CARENCIA FACTA 2,14, 120 DIAS' or tabela == 'BLOQUEADOS SEM CARENCIA FACTA 2,14 COM 120 DIAS':
                                                In = self.chrome.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[4]')
                                                In.click()
                                            if tabela == 'DESBLOQUEADOS COM CARENCIA FACTA 120 DIA 2,14' or tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS':
                                                In1 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In1.click()
                                            if tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS - 1X A 84X':
                                                In2 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                            if tabela == 'DIG INSS - NOVO 1,30 - SEM CARENCIA E SEM SEGURO - 1X A 84X':
                                                In3 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In3.click()
                                            if tabela == 'FACTA INSS 1,80 SEM CARENCIA - 1X A 84X':
                                                In4 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In4.click()
                                            else:
                                                print('Tabela incompativel....')

                                            sleep(2)
                                            btnn = self.chrome.find_element_by_css_selector('#etapa1')
                                            btnn.click()

                                    except Exception as e:
                                        print(e)
                                        print('Erro ao tentar conecta de primeira...')
                                        print('Tenatndo novamente....')
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
                                            senhaa.send_keys('Dezembro@202')
                                            sleep(1)
                                            entrar.click()
                                            sleep(3)
                                        except Exception:
                                            print('Erro ao tenatar reconectar b...')
                                            print('tenatando novamente...')
                                            usuario = self.chrome.find_element_by_css_selector('#login')
                                            senhaa = self.chrome.find_element_by_css_selector('#senha')
                                            entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                                            sleep(1)
                                            usuario.send_keys('600045_Beatriz')
                                            sleep(1)
                                            senhaa.send_keys('Dezembro@202')
                                            sleep(1)
                                            entrar.click()
                                            sleep(3)
                                        try:
                                            sleep(3)
                                            try:
                                                fechar = self.chrome.find_element_by_css_selector(
                                                    '#modalMuralAlertas > div > div.modal-footer > button').click()
                                            except Exception:
                                                print('alo')
                                            sleep(2)
                                            operacional = self.chrome.find_element_by_css_selector(
                                                '#main-nav > div > ul > li:nth-child(2) > a')
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
                                            vendadigital = self.chrome.find_element_by_css_selector(
                                                '#produto > option:nth-child(8)')
                                            vendadigital.click()
                                            pyautogui.click(x=550, y=550)
                                            sleep(2)
                                            tipo_operacao = self.chrome.find_element_by_css_selector('#tipoOperacao')
                                            tipo_operacao.click()
                                            sleep(2)
                                            novo = self.chrome.find_element_by_css_selector(
                                                '#tipoOperacao > option:nth-child(4)')
                                            novo.click()
                                            pyautogui.click(x=550, y=550)
                                            sleep(4)
                                            orgaa = self.chrome.find_element_by_css_selector('#averbador')
                                            orgaa.click()
                                            inss = self.chrome.find_element_by_css_selector(
                                                '#averbador > option:nth-child(27)')
                                            inss.click()
                                            pyautogui.click(x=550, y=550)

                                            sleep(15)
                                            try:
                                                print('tentando conectar de primeira no banco..')
                                                bancoo = self.chrome.find_element_by_css_selector('#banco')
                                                bancoo.click()
                                                sleep(2)
                                                facta = self.chrome.find_element_by_css_selector(
                                                    '#banco > option:nth-child(7)')
                                                facta.click()
                                                pyautogui.click(x=550, y=550)
                                            except Exception:
                                                print('erro ao tentar clicar no banco.... ')
                                                print('Tentando novamente')
                                                sleep(6)
                                                bancoo = self.chrome.find_element_by_css_selector('#banco')
                                                bancoo.click()
                                                sleep(2)
                                                facta = self.chrome.find_element_by_css_selector(
                                                    '#banco > option:nth-child(7)')
                                                facta.click()
                                                pyautogui.click(x=550, y=550)
                                            sleep(2)
                                            cpff = self.chrome.find_element_by_css_selector('#cpf')
                                            cpff.send_keys(cpf)
                                            sleep(1)
                                            try:
                                                dataaa = self.chrome.find_element_by_css_selector(
                                                    '#dataNascimento').click()
                                                dataaaa = self.chrome.find_element_by_css_selector(
                                                    '#dataNascimento').send_keys(data)
                                                sleep(0.5)
                                                nomee = self.chrome.find_element_by_id('#nomeCliente').click()
                                                nomee = self.chrome.find_element_by_css_selector(
                                                    '#nomeCliente').send_keys(nome)
                                                pyautogui.click(x=550, y=550)
                                                sleep(3)
                                                solicitado = self.chrome.find_element_by_css_selector('#valor')
                                                solicitado.send_keys(financiaado)
                                                valor_solicitado = self.chrome.find_element_by_css_selector(
                                                    '#opcaoValor')
                                                valor_solicitado.click()
                                                sleep(1.5)
                                                selecionar = self.chrome.find_element_by_css_selector(
                                                    '#opcaoValor > option:nth-child(2)')
                                                selecionar.click()
                                                prazo = self.chrome.find_element_by_css_selector('#prazo')
                                                prazo.send_keys('84')
                                                pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                                                pesquisa.click()
                                                sleep(10)

                                                if tabela == 'DESBLOQUEADOS SEM CARENCIA FACTA 2,14, 120 DIAS' or tabela == 'BLOQUEADOS SEM CARENCIA FACTA 2,14 COM 120 DIAS':
                                                    In = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[4]')
                                                    In.click()
                                                if tabela == 'DESBLOQUEADOS COM CARENCIA FACTA 120 DIA 2,14' or tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS':
                                                    In1 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                    In1.click()
                                                if tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS - 1X A 84X':
                                                    In2 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]').click()
                                                if tabela == 'DIG INSS - NOVO 1,30 - SEM CARENCIA E SEM SEGURO - 1X A 84X':
                                                    In3 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                    In3.click()
                                                else:
                                                    print('Tabela incompativel....')

                                                sleep(2)
                                                btnn = self.chrome.find_element_by_css_selector('#etapa1')
                                                btnn.click()
                                            # data_ = self.chrome.find_element_by_css_selector('#dataNascimento')
                                            # data_.clear()
                                            # data_.send_keys(data)
                                            except Exception as e:
                                                print(e)
                                                solicitado = self.chrome.find_element_by_css_selector('#valor')
                                                solicitado.send_keys(financiaado)
                                                valor_solicitado = self.chrome.find_element_by_css_selector(
                                                    '#opcaoValor')
                                                valor_solicitado.click()
                                                sleep(1.5)
                                                selecionar = self.chrome.find_element_by_css_selector(
                                                    '#opcaoValor > option:nth-child(2)')
                                                selecionar.click()
                                                prazo = self.chrome.find_element_by_css_selector('#prazo')
                                                prazo.send_keys('84')
                                                pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                                                pesquisa.click()
                                                sleep(10)
                                                if tabela == 'DESBLOQUEADOS SEM CARENCIA FACTA 2,14, 120 DIAS' or tabela == 'BLOQUEADOS SEM CARENCIA FACTA 2,14 COM 120 DIAS':
                                                    In = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[4]')
                                                    In.click()
                                                if tabela == 'DESBLOQUEADOS COM CARENCIA FACTA 120 DIA 2,14' or tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS':
                                                    In1 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                    In1.click()
                                                if tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS - 1X A 84X':
                                                    In2 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                if tabela == 'DIG INSS - NOVO 1,30 - SEM CARENCIA E SEM SEGURO - 1X A 84X':
                                                    In3 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                    In3.click()
                                                else:
                                                    print('Tabela incompativel....')

                                                sleep(2)
                                                btnn = self.chrome.find_element_by_css_selector('#etapa1')
                                                btnn.click()

                                        except Exception as e:
                                            print('Error Prineiro processo...', e)

                                    print('Segunda etapa...')
                                    try:
                                        sleep(2)
                                        alert = self.chrome.switch_to.alert
                                        alert.accept()
                                        sleep(1)

                                        login = self.chrome.find_element_by_css_selector(
                                            '#tab2 > fieldset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > select').click()
                                        sleep(1)
                                        Daine = self.chrome.find_element_by_xpath(
                                            '//*[@id="tab2"]/fieldset[1]/div[1]/div[1]/select/option[26]').click()
                                        pyautogui.click(x=550, y=550)

                                        sleep(2)
                                        vendedor = self.chrome.find_element_by_css_selector('#vendedor').click()
                                        vendedorB = self.chrome.find_element_by_css_selector(
                                            '#vendedor > option:nth-child(6)').click()
                                        pyautogui.click(x=550, y=550)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        btnw = self.chrome.find_element_by_css_selector('#etapa_2')
                                        btnw.click()
                                        sleep(70)
                                    except Exception as e:
                                        print(e)
                                        print('Erro no segundo processo.....')
                                        print('Tentando novamente......')
                                        pyautogui.press('f5')
                                        sleep(2)
                                        alert = self.chrome.switch_to.alert
                                        alert.accept()
                                        sleep(1)

                                        login = self.chrome.find_element_by_css_selector(
                                            '#tab2 > fieldset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > select').click()
                                        sleep(1)
                                        Daine = self.chrome.find_element_by_xpath('//*[@id="tab2"]/fieldset[1]/div[1]/div[1]/select/option[26]').click()

                                        pyautogui.click(x=550, y=550)

                                        sleep(2)
                                        vendedor = self.chrome.find_element_by_css_selector('#vendedor').click()
                                        vendedorB = self.chrome.find_element_by_css_selector(
                                            '#vendedor > option:nth-child(6)').click()
                                        pyautogui.click(x=550, y=550)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(1.5)
                                        btnw = self.chrome.find_element_by_css_selector('#etapa_2')
                                        btnw.click()
                                        sleep(70)

                                    try:
                                        print('tereceiro processo.....')
                                        try:
                                            sleep(2)
                                            alert = self.chrome.switch_to.alert
                                            alert.accept()
                                            sleep(1)

                                        except Exception:
                                            print('Sem mensagem ')
                                        cliente = self.chrome.find_element_by_css_selector('#clienteAnalfabeto').click()

                                        nao = self.chrome.find_element_by_css_selector(

                                            '#clienteAnalfabeto > option:nth-child(3)').click()
                                        sleep(1)


                                        renda = self.chrome.find_element_by_css_selector('#valorDoBeneficio').send_keys(salario)
                                        esp= self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]').click()
                                        sleep(4)
                                        if especie == '21':
                                            B21= self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]/option[11]').click()
                                        if especie == '32':
                                            b32= self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]/option[19]').click()
                                        if especie == '41':
                                            b41= self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]/option[24]').click()
                                        if especie == '42':
                                            b42= self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]/option[25]').click()
                                        if especie == '46':
                                            b46= self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]/option[29]').click()
                                        if especie == '57':
                                            b57= self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]/option[36]').click()
                                        if especie == '92':
                                            b92 = self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]/option[46]').click()
                                        if especie == '93':
                                            b93= self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]/option[47]').click()
                                        else:
                                            print('Especie vazia ou não compativel')
                                        sleep(2)
                                        UFF= self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]').click()
                                        sleep(2)
                                        if UF == 'AC':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[2]').click()
                                        if UF == 'AL':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[3]').click()
                                        if UF == 'AM':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[4]').click()
                                        if UF == 'AP':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[5]').click()
                                        if UF == 'AL':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[6]').click()
                                        if UF == 'BA':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[6]').click()
                                        if UF == 'CE':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[7]').click()

                                        if UF == 'DF':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[8]').click()
                                        if UF == 'ES':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[9]').click()
                                        if UF == 'GO':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[10]').click()
                                        if UF == 'MA':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[11]').click()
                                        if UF == 'MG':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[12]').click()
                                        if UF == 'MS':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[13]').click()
                                        if UF == 'MT':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[14]').click()
                                        if UF == 'PA':
                                            self.chrome.find_element_by_xpath('#ufBeneficio > option:nth-child(15)').click()
                                        if UF == 'PB':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[16]').click()
                                        if UF == 'PE':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[17]').click()
                                        if UF == 'PI':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[18]').click()
                                        if UF == 'PR':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[19]').click()
                                        if UF == 'RJ':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[20]').click()
                                        if UF == 'RN':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[21]').click()
                                        if UF == 'RO':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[22]').click()
                                        if UF == 'RR':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[23]').click()
                                        if UF == 'RS':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[24]').click()
                                        if UF == 'SC':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[25]').click()
                                        if UF == 'SE':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[26]').click()
                                        if UF == 'SP':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[27]').click()
                                        if UF == 'TO':
                                            self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]/option[28]').click()
                                        sleep(1)
                                        tipo = self.chrome.find_element_by_xpath(
                                            '//*[@id="mesaCreditoTipoBeneficio"]').click()
                                        tipoC = self.chrome.find_element_by_xpath(
                                            '//*[@id="mesaCreditoTipoBeneficio"]/option[2]').click()
                                        sleep(1)
                                        cepp = self.chrome.find_element_by_css_selector('#cep')
                                        cepp.click()
                                        cepp.send_keys(cep)
                                        sleep(1)
                                        pesquisaa = self.chrome.find_element_by_css_selector('#pesquisar_cep').click()
                                        end = self.chrome.find_element_by_css_selector('#endereco').clear()
                                        sleep(1)
                                        sleep(3)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        en = self.chrome.find_element_by_css_selector('#endereco').send_keys(rua)
                                        sleep(2)

                                        nuber = self.chrome.find_element_by_css_selector('#numero').clear()
                                        nube = self.chrome.find_element_by_css_selector('#numero').send_keys('12')
                                        sleep(2)
                                        bairrr = self.chrome.find_element_by_css_selector('#bairro').clear()
                                        bairrrr = self.chrome.find_element_by_css_selector('#bairro').send_keys(bairro)
                                        sleep(2)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(1)
                                        cidadee = self.chrome.find_element_by_css_selector('#cidade').click()
                                        pyautogui.press('down')
                                        pyautogui.press('enter')
                                        cel = self.chrome.find_element_by_css_selector('#celular')
                                        cel.click()
                                        cel1 = self.chrome.find_element_by_css_selector('#celular')
                                        cel1.send_keys(numeroTel)
                                        sleep(2)
                                        resi = self.chrome.find_element_by_css_selector('#tipoResidencia').click()
                                        familiar = self.chrome.find_element_by_css_selector(
                                            '#tipoResidencia > option:nth-child(3)').click()
                                        sleep(2)
                                        emaill = self.chrome.find_element_by_css_selector('#email').click()
                                        sleep(1)
                                        emaii = self.chrome.find_element_by_css_selector('#email').send_keys(email)

                                        sleep(4)
                                        btn3 = self.chrome.find_element_by_css_selector('#etapa_3')
                                        btn3.click()
                                        sleep(20)
                                    except Exception as e:
                                        self.chrome.refresh()
                                        print(e)
                                        print('Erro no terceiro processo')
                                        print(' Tentando novamenete.....')
                                        print('tereceiro processo.....')
                                        try:
                                            sleep(2)
                                            alert = self.chrome.switch_to.alert
                                            alert.accept()
                                            sleep(1)

                                        except Exception:
                                            print('Sem mensagem ')
                                        cliente = self.chrome.find_element_by_css_selector('#clienteAnalfabeto').click()
                                        nao = self.chrome.find_element_by_css_selector(
                                            '#clienteAnalfabeto > option:nth-child(3)').click()
                                        sleep(1)

                                        renda = self.chrome.find_element_by_css_selector('#valorDoBeneficio').send_keys(
                                            salario)
                                        esp = self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]').click()
                                        sleep(1)
                                        if especie == '21':
                                            B21 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[11]').click()
                                        if especie == '32':
                                            b32 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[19]').click()
                                        if especie == '41':
                                            b41 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[24]').click()
                                        if especie == '42':
                                            b42 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[25]').click()
                                        if especie == '46':
                                            b46 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[29]').click()
                                        if especie == '57':
                                            b57 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[36]').click()
                                        if especie == '92':
                                            b92 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[46]').click()
                                        if especie == '93':
                                            b93 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[47]').click()
                                        else:
                                            print('Especie vazia ou não compativel')
                                        sleep(2)
                                        UFF = self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]').click()
                                        sleep(2)
                                        if UF == 'AC':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[2]').click()
                                        if UF == 'AL':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[3]').click()
                                        if UF == 'AM':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[4]').click()
                                        if UF == 'AP':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[5]').click()
                                        if UF == 'AL':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[6]').click()
                                        if UF == 'BA':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[6]').click()
                                        if UF == 'CE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[7]').click()

                                        if UF == 'DF':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[8]').click()
                                        if UF == 'ES':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[9]').click()
                                        if UF == 'GO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[10]').click()
                                        if UF == 'MA':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[11]').click()
                                        if UF == 'MG':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[12]').click()
                                        if UF == 'MS':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[13]').click()
                                        if UF == 'MT':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[14]').click()
                                        if UF == 'PA':
                                            self.chrome.find_element_by_xpath(
                                                '#ufBeneficio > option:nth-child(15)').click()
                                        if UF == 'PB':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[16]').click()
                                        if UF == 'PE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[17]').click()
                                        if UF == 'PI':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[18]').click()
                                        if UF == 'PR':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[19]').click()
                                        if UF == 'RJ':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[20]').click()
                                        if UF == 'RN':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[21]').click()
                                        if UF == 'RO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[22]').click()
                                        if UF == 'RR':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[23]').click()
                                        if UF == 'RS':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[24]').click()
                                        if UF == 'SC':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[25]').click()
                                        if UF == 'SE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[26]').click()
                                        if UF == 'SP':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[27]').click()
                                        if UF == 'TO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[28]').click()

                                        sleep(1)
                                        tipo = self.chrome.find_element_by_xpath(
                                            '//*[@id="mesaCreditoTipoBeneficio"]').click()
                                        tipoC = self.chrome.find_element_by_xpath(
                                            '//*[@id="mesaCreditoTipoBeneficio"]/option[2]').click()
                                        sleep(1)
                                        cepp = self.chrome.find_element_by_css_selector('#cep')
                                        cepp.click()
                                        cepp.send_keys(cep)
                                        sleep(1)
                                        pesquisaa = self.chrome.find_element_by_css_selector('#pesquisar_cep').click()
                                        end = self.chrome.find_element_by_css_selector('#endereco').clear()
                                        sleep(1)
                                        sleep(3)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        en = self.chrome.find_element_by_css_selector('#endereco').send_keys(rua)
                                        sleep(2)

                                        nuber = self.chrome.find_element_by_css_selector('#numero').clear()
                                        nube = self.chrome.find_element_by_css_selector('#numero').send_keys('12')
                                        sleep(2)
                                        bairrr = self.chrome.find_element_by_css_selector('#bairro').clear()
                                        bairrrr = self.chrome.find_element_by_css_selector('#bairro').send_keys(bairro)
                                        sleep(2)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(1)
                                        cidadee = self.chrome.find_element_by_css_selector('#cidade').click()
                                        pyautogui.press('down')
                                        pyautogui.press('enter')
                                        cel = self.chrome.find_element_by_css_selector('#celular')
                                        cel.click()
                                        cel1 = self.chrome.find_element_by_css_selector('#celular')
                                        cel1.send_keys(numeroTel)
                                        sleep(2)
                                        resi = self.chrome.find_element_by_css_selector('#tipoResidencia').click()
                                        familiar = self.chrome.find_element_by_css_selector(
                                            '#tipoResidencia > option:nth-child(3)').click()
                                        sleep(2)
                                        emaill = self.chrome.find_element_by_css_selector('#email').click()
                                        sleep(1)
                                        emaii = self.chrome.find_element_by_css_selector('#email').send_keys(email)

                                        sleep(4)
                                        btn3 = self.chrome.find_element_by_css_selector('#etapa_3')
                                        btn3.click()
                                        sleep(20)
                                    print('Quarto  Processo...')
                                    try:
                                        sleep(2)
                                        bac= self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]').click()
                                        if banco== '25':
                                            c1= self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[24]')
                                        if banco == '28':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[3]')
                                        if banco == '40':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[24]')
                                        if banco == '37':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[37]')
                                        if banco == '1':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[2]')
                                        if banco == '27':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[5]')
                                        if banco == '33':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[14]')
                                        if banco == '17':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[4]')
                                        if banco == '22':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[19]')
                                        #if banco == '26':
                                            #c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '21':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[31]')
                                        if banco == '19':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[55]')
                                        if banco == '32':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[11]')
                                        if banco == '15':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[13]')
                                        #if banco == '11':
                                            #c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '5':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[36]')
                                        if banco == '12':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[32]')
                                        if banco == '35':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[15]')
                                        if banco == '4':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[10]')
                                        if banco == '16':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[16]')
                                        if banco == '9':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[51]')
                                        if banco == '20':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[38]')
                                        if banco == '3':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[23]')
                                        if banco == '31':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[15]')
                                        if banco == '10':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[52]')
                                        #if banco == '36':
                                           # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '6':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[39]')
                                        if banco == '34':
                                            c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '14':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[42]')
                                        if banco == '30':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[33]')
                                        if banco == '23':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[35]')
                                        #if banco == '18':
                                            #c1 = self.chrome.find_element_by_xpath('')
                                       # if banco == '29':
                                           # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '8':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[49]')
                                        if banco == '7':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[46]')
                                        if banco == '2':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[9]')
                                        if banco == '24':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[55]')
                                        if banco == '13':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[54]')

                                        if banco == '38':
                                            c1 = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]/option[20]')
                                        
                                        sleep(15)
                                        agenciacamp= self.chrome.find_element_by_xpath('//*[@id="agenciaLiberacao"]').send_keys(agencia)
                                        sleep(1)
                                        contaa= self.chrome.find_element_by_xpath('//*[@id="contaLiberacao"]').send_keys(numeroconta)
                                        sleep(2)
                                        Ramo = self.chrome.find_element_by_xpath('//*[@id="id_ramo_atividade_or"]').click()
                                        ram = self.chrome.find_element_by_css_selector(
                                            '#id_ramo_atividade_or > option:nth-child(8)').click()
                                        sleep(3)
                                        prof = self.chrome.find_element_by_css_selector('#id_tipo_profissao_or').click()
                                        prof1 = self.chrome.find_element_by_css_selector(
                                            '#id_tipo_profissao_or > option:nth-child(2)').click()
                                        sleep(3)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        btn4 = self.chrome.find_element_by_css_selector('#etapa_4').click()
                                    except Exception as e:
                                        print(e)
                                        sleep(40)
                                        print('Erro no quarto processo....')
                                        print('Tenatndo novamente ')
                                        sleep(2)
                                        bac = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]').click()
                                        if banco == '25':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[24]')
                                        if banco == '28':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[3]')
                                        if banco == '40':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[24]')
                                        if banco == '37':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[37]')
                                        if banco == '1':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[2]')
                                        if banco == '27':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[5]')
                                        if banco == '33':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[14]')
                                        if banco == '17':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[4]')
                                        if banco == '22':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[19]')
                                        # if banco == '26':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '21':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[31]')
                                        if banco == '19':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[55]')
                                        if banco == '32':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[11]')
                                        if banco == '15':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[13]')
                                        # if banco == '11':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '5':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[36]')
                                        if banco == '12':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[32]')
                                        if banco == '35':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[15]')
                                        if banco == '4':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[10]')
                                        if banco == '16':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[16]')
                                        if banco == '9':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[51]')
                                        if banco == '20':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[38]')
                                        if banco == '3':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[23]')
                                        if banco == '31':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[15]')
                                        if banco == '10':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[52]')
                                        # if banco == '36':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '6':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[39]')
                                        if banco == '34':
                                            c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '14':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[42]')
                                        if banco == '30':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[33]')
                                        if banco == '23':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[35]')
                                        # if banco == '18':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        # if banco == '29':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '8':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[49]')
                                        if banco == '7':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[46]')
                                        if banco == '2':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[9]')
                                        if banco == '24':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[55]')
                                        if banco == '13':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[54]')

                                        if banco == '38':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[20]')

                                        sleep(15)
                                        agenciacamp = self.chrome.find_element_by_xpath(
                                            '//*[@id="agenciaLiberacao"]').send_keys(agencia)
                                        sleep(1)
                                        contaa = self.chrome.find_element_by_xpath(
                                            '//*[@id="contaLiberacao"]').send_keys(numeroconta)
                                        sleep(2)
                                        Ramo = self.chrome.find_element_by_css_selector('#id_ramo_atividade_or').click()
                                        ram = self.chrome.find_element_by_css_selector(
                                            '#id_ramo_atividade_or > option:nth-child(8)').click()
                                        sleep(1)
                                        prof = self.chrome.find_element_by_css_selector('#id_tipo_profissao_or').click()
                                        prof1 = self.chrome.find_element_by_css_selector(
                                            '#id_tipo_profissao_or > option:nth-child(2)').click()
                                        sleep(3)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        btn4 = self.chrome.find_element_by_css_selector('#etapa_4').click()

                                    try:
                                        print('Quinto processo...')
                                        sleep(40)
                                        codigo = self.chrome.find_element_by_css_selector(
                                            '#content-wrapper > div > div > div > div:nth-child(2) > h3:nth-child(1)').text
                                        print(codigo)
                                        digital = self.chrome.find_element_by_css_selector(
                                            '#content-wrapper > div > div > div > div:nth-child(3) > div.span6 > div:nth-child(3) > input[type=radio]').click()
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        form = self.chrome.find_element_by_css_selector(
                                            '#btnRealizaFormalizacao').click()
                                        sleep(2)
                                        try:
                                            py = self.chrome.find_element_by_css_selector(
                                                '#corpo > div.bootbox.modal.fade.in > div.modal-footer > a').click()
                                            sleep(2)
                                        except Exception:
                                            print('mesagem não apareceu')
                                        op = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > a').click()

                                        sleep(1)
                                        consultas = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(6) > a').click()
                                        anda = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(6) > ul > li:nth-child(2) > a > span').click()
                                        sleep(2)

                                        cod = self.chrome.find_element_by_css_selector('#cpf').click()
                                        cod1 = self.chrome.find_element_by_css_selector('#cpf').send_keys(cpf)

                                        pes = self.chrome.find_element_by_css_selector('#pesquisar').click()
                                        sleep(10)
                                        self.chrome.execute_script("window.scrollTo(0, 620)")
                                        sleep(5)
                                        link = self.chrome.find_element_by_css_selector(
                                            '#tblListaProposta > tbody > tr:nth-child(1) > td:nth-child(22) > i').click()
                                        print(link)
                                        sleep(2)
                                        alert = self.chrome.switch_to.alert
                                        alert.accept()
                                        sleep(1)


                                    except Exception as e:
                                        print(e)
                                        self.chrome.refresh()
                                        print('Tentando o quinto processooo.....')
                                        sleep(40)
                                        codigo = self.chrome.find_element_by_css_selector(
                                            '#content-wrapper > div > div > div > div:nth-child(2) > h3:nth-child(1)').text
                                        print(codigo)
                                        digital = self.chrome.find_element_by_css_selector(
                                            '#content-wrapper > div > div > div > div:nth-child(3) > div.span6 > div:nth-child(3) > input[type=radio]').click()
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        form = self.chrome.find_element_by_css_selector(
                                            '#btnRealizaFormalizacao').click()
                                        sleep(2)
                                        try:
                                            py = self.chrome.find_element_by_css_selector(
                                                '#corpo > div.bootbox.modal.fade.in > div.modal-footer > a').click()
                                            sleep(2)
                                        except Exception:
                                            print('mesagem não apareceu')
                                        op = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > a').click()
                                        self.chrome.execute_script("window.scrollTo(0, 55)")
                                        sleep(1)
                                        consultas = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(6) > a').click()
                                        anda = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(6) > ul > li:nth-child(2) > a > span').click()
                                        sleep(2)

                                        cod = self.chrome.find_element_by_css_selector('#cpf').click()
                                        cod1 = self.chrome.find_element_by_css_selector('#cpf').send_keys(cpf)

                                        pes = self.chrome.find_element_by_css_selector('#pesquisar').click()

                                        sleep(6)
                                        self.chrome.execute_script("window.scrollTo(0, 120)")
                                        sleep(15)

                                        link = self.chrome.find_element_by_css_selector(
                                            '#tblListaProposta > tbody > tr:nth-child(1) > td:nth-child(22) > i').click()
                                        print(link)
                                        sleep(2)
                                        alert = self.chrome.switch_to.alert
                                        alert.accept()
                                        sleep(1)
                                    chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
                                    self.chrome.refresh()
                                    sleep(16)
                                    print('Sexto processo....')

                                    try:

                                        sleep(4)
                                        camp_nome = self.chrome.find_element_by_id('login')
                                        sleep(1)
                                        camp_senha = self.chrome.find_element_by_id('password')
                                        sleep(1)
                                        camp_entrar = self.chrome.find_element_by_class_name('jss10')
                                        camp_nome.send_keys('t.i')
                                        sleep(3)
                                        camp_senha.send_keys('179202*')
                                        sleep(1)
                                        camp_entrar.click()
                                        sleep(6)
                                        camp_cliente = self.chrome.find_element_by_xpath('//*[@id="menu-100"]/div/div/div/ul[2]/li')
                                        camp_cliente.click()

                                        sleep(4)
                                        pesquisa = self.chrome.find_element_by_css_selector('#searchInput')
                                        sleep(1)
                                        pesquisa.send_keys(cpf)
                                        sleep(1)
                                        pyautogui.press('enter')
                                        sleep(25)

                                        status = self.chrome.find_element_by_css_selector(
                                            '#main-content > div:nth-child(1) > div > div.jss132.jss136.jss133.jss339 > div.jss343 > table > tbody > tr:nth-child(1) > td:nth-child(22) > div > span')
                                        status.click()
                                        sleep(2)
                                        visualizar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss164.modal > div:nth-child(2) > div.modalBody.modal-status > div > form > fieldset > label:nth-child(2) > select')
                                        visualizar.click()
                                        sleep(2)
                                        aceite = self.chrome.find_element_by_css_selector(
                                            'body > div.jss164.modal > div:nth-child(2) > div.modalBody.modal-status > div > form > fieldset > label:nth-child(2) > select > option:nth-child(3)').click()
                                        sleep(1)
                                        colar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss164.modal > div:nth-child(2) > div.modalBody.modal-status > div > form > fieldset > label.mt2 > textarea')
                                        colar.click()
                                        pyautogui.hotkey('ctrl', 'v')
                                        sleep(1)
                                        salvar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss164.modal > div:nth-child(2) > div.modalBody.modal-status > div > form > fieldset > button')
                                        salvar.click()
                                        sleep(10)
                                        status = self.chrome.find_element_by_xpath(
                                            '//*[@id="filtro-paper"]/div/div[1]/div[8]').click()
                                        sleep(2)
                                        aceite = self.chrome.find_element_by_class_name('input-busca-filtro').send_keys(
                                            'AGUARDANDO DIGITAÇÃO')
                                        sleep(1)
                                        aceite = self.chrome.find_element_by_css_selector(
                                            'body > div.jss71.jss144.jss145 > div.jss39.jss65.jss40.jss147.jss148.jss151 > div.jss321.dialog-filter > label:nth-child(5)').click()
                                        sleep(1)
                                        aplicar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss71.jss144.jss145 > div.jss39.jss65.jss40.jss147.jss148.jss151 > div.jss322 > button.jss105.jss81.jss83.jss86.applyFilters.jss323 > span.jss82').click()
                                        sleep(3)

                                        banco = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(1) > div:nth-child(4)').click()
                                        sleep(1)
                                        aceite = self.chrome.find_element_by_class_name('input-busca-filtro').send_keys(
                                            'facta')
                                        sleep(1)
                                        facta1 = self.chrome.find_element_by_class_name('checkbox-description').click()
                                        sleep(1)
                                        plicar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss71.jss144.jss145 > div.jss39.jss65.jss40.jss147.jss148.jss151 > div.jss337 > button.jss105.jss81.jss83.jss86.applyFilters.jss338 > span.jss82').click()
                                        sleep(3)
                                        data = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div > input[type=text]').click()
                                        sleep(4)
                                        seta = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()
                                        seta = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()
                                        seta = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()

                                        data1 = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(1) > div.react-datepicker__day.react-datepicker__day--wed').click()
                                        sleep(1)
                                        filtro = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(3) > div.sc-jAaTju.fVRxI').click()
                                        sleep(5)
                                        menu = self.chrome.find_element_by_css_selector(
                                            '#topo > button.jss105.jss81.jss90.jss93.hamburguer').click()
                                        print('atualizando...')
                                        sleep(5)
                                        refre = self.chrome.find_element_by_xpath(
                                            '//*[@id="filtro-paper"]/div/div[3]/div[2]').click()



                                    except Exception as a:
                                        print(a)
                                        print('erro')


                                ################################################################################################################
                                except Exception:
                                    print('Algo deu errado no processo...')
                                    print('Vamos tentar de novo :)...')
                                    print('Mas agora sem erro, Bora!!!')

                                    try:
                                        chrome.acessar('http://desenv.facta.com.br/sistemaNovo/login.php')
                                        usuario = self.chrome.find_element_by_css_selector('#login')
                                        senhaa = self.chrome.find_element_by_css_selector('#senha')
                                        entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                                        usuario.send_keys('600045_Beatriz')
                                        senhaa.send_keys('Dezembro@201')
                                        entrar.click()
                                        sleep(2)
                                    except Exception as e:
                                        chrome.acessar('http://desenv.facta.com.br/sistemaNovo/login.php')
                                        usuario = self.chrome.find_element_by_css_selector('#login')
                                        senhaa = self.chrome.find_element_by_css_selector('#senha')
                                        entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                                        usuario.send_keys('600045_Beatriz')
                                        senhaa.send_keys('Dezembro@202')
                                        entrar.click()
                                        sleep(2)
                                    try:
                                        print('Acessando a primeira pagina....')
                                        sleep(3)
                                        try:
                                            fechar = self.chrome.find_element_by_css_selector(
                                                '#modalMuralAlertas > div > div.modal-footer > button').click()
                                        except Exception:
                                            print('alo')
                                        operacional = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > a')
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
                                        vendadigital = self.chrome.find_element_by_css_selector(
                                            '#produto > option:nth-child(8)')
                                        vendadigital.click()
                                        pyautogui.click(x=550, y=550)
                                        sleep(2)
                                        tipo_operacao = self.chrome.find_element_by_css_selector('#tipoOperacao')
                                        tipo_operacao.click()
                                        novo = self.chrome.find_element_by_css_selector(
                                            '#tipoOperacao > option:nth-child(4)')
                                        novo.click()
                                        pyautogui.click(x=550, y=550)
                                        sleep(4)
                                        orgaa = self.chrome.find_element_by_css_selector('#averbador')
                                        orgaa.click()

                                        inss = self.chrome.find_element_by_css_selector(
                                            '#averbador > option:nth-child(27)')
                                        inss.click()
                                        pyautogui.click(x=550, y=550)
                                        sleep(2)
                                        fig = self.chrome.find_element_by_css_selector(
                                            '#divContakoWidgetJSPopUpIntegrado > img:nth-child(1)')
                                        fig.click()
                                        pyautogui.press('enter')
                                        sleep(15)
                                        try:
                                            bancoo = self.chrome.find_element_by_css_selector('#banco')
                                            bancoo.click()
                                            sleep(3)
                                            facta = self.chrome.find_element_by_css_selector(
                                                '#banco > option:nth-child(7)')
                                            facta.click()
                                            pyautogui.click(x=550, y=550)
                                        except Exception as e:
                                            print(e)
                                            print('erro ao tentar clicar no banco.... ')
                                            print('Tenatando novamente')
                                            sleep(6)
                                            bancoo = self.chrome.find_element_by_css_selector('#banco')
                                            bancoo.click()
                                            sleep(2)
                                            facta = self.chrome.find_element_by_css_selector(
                                                '#banco > option:nth-child(7)')
                                            facta.click()
                                            pyautogui.click(x=550, y=550)
                                        cpff = self.chrome.find_element_by_css_selector('#cpf')
                                        cpff.send_keys(cpf)

                                        pyautogui.click(x=550, y=550)
                                        try:
                                            dataaa = self.chrome.find_element_by_css_selector('#dataNascimento').click()
                                            dataaaa = self.chrome.find_element_by_css_selector(
                                                '#dataNascimento').send_keys(data)
                                            sleep(0.5)
                                            nomee = self.chrome.find_element_by_id('#nomeCliente').click()
                                            nomee = self.chrome.find_element_by_css_selector('#nomeCliente').send_keys(
                                                nome)
                                            pyautogui.click(x=550, y=550)
                                            sleep(3)
                                            solicitado = self.chrome.find_element_by_css_selector('#valor')
                                            solicitado.send_keys(financiaado)
                                            valor_solicitado = self.chrome.find_element_by_css_selector('#opcaoValor')
                                            valor_solicitado.click()
                                            valor_solicitado.send_keys(financiaado)
                                            sleep(1.5)
                                            selecionar = self.chrome.find_element_by_css_selector(
                                                '#opcaoValor > option:nth-child(2)')
                                            selecionar.click()
                                            prazo = self.chrome.find_element_by_css_selector('#prazo')
                                            prazo.send_keys('84')
                                            pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                                            pesquisa.click()
                                            sleep(10)
                                            if tabela == 'DESBLOQUEADOS SEM CARENCIA FACTA 2,14, 120 DIAS' or tabela == 'BLOQUEADOS SEM CARENCIA FACTA 2,14 COM 120 DIAS':
                                                In = self.chrome.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[4]')
                                                In.click()
                                            if tabela == 'DESBLOQUEADOS COM CARENCIA FACTA 120 DIA 2,14' or tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS':
                                                In1 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In1.click()
                                            if tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS - 1X A 84X':
                                                In2 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                            if tabela == 'DIG INSS - NOVO 1,30 - SEM CARENCIA E SEM SEGURO - 1X A 84X':
                                                In3 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In3.click()
                                            else:
                                                print('Tabela incompativel....')

                                            sleep(2)
                                            btnn = self.chrome.find_element_by_css_selector('#etapa1')
                                            btnn.click()

                                        # data_ = self.chrome.find_element_by_css_selector('#dataNascimento')
                                        # data_.clear()
                                        # data_.send_keys(data)
                                        except Exception as e:
                                            print('Campos nome e data preenchidos, continuando....')
                                            solicitado = self.chrome.find_element_by_css_selector('#valor')
                                            solicitado.send_keys(financiaado)
                                            valor_solicitado = self.chrome.find_element_by_css_selector('#opcaoValor')
                                            valor_solicitado.click()
                                            sleep(1.5)
                                            selecionar = self.chrome.find_element_by_css_selector(
                                                '#opcaoValor > option:nth-child(2)')
                                            selecionar.click()
                                            prazo = self.chrome.find_element_by_css_selector('#prazo')
                                            prazo.send_keys('84')
                                            pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                                            pesquisa.click()
                                            sleep(10)
                                            if tabela == 'DESBLOQUEADOS SEM CARENCIA FACTA 2,14, 120 DIAS' or tabela == 'BLOQUEADOS SEM CARENCIA FACTA 2,14 COM 120 DIAS':
                                                In = self.chrome.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[4]')
                                                In.click()
                                            if tabela == 'DESBLOQUEADOS COM CARENCIA FACTA 120 DIA 2,14' or tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS':
                                                In1 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In1.click()
                                            if tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS - 1X A 84X':
                                                In2 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                            if tabela == 'DIG INSS - NOVO 1,30 - SEM CARENCIA E SEM SEGURO - 1X A 84X':
                                                In3 = self.chrome.find_element_by_xpath(
                                                    '//*[@id="myTable"]/tbody/tr[6]')
                                                In3.click()
                                            else:
                                                print('Tabela incompativel....')

                                            sleep(2)
                                            btnn = self.chrome.find_element_by_css_selector('#etapa1')
                                            btnn.click()
                                    except Exception as e:
                                        print(e)
                                        print('Erro ao tentar conecta de primeira...')
                                        print('Tenatndo novamente....')
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
                                            senhaa.send_keys('Dezembro@201')
                                            sleep(1)
                                            entrar.click()
                                            sleep(3)
                                        except Exception:
                                            print('Erro ao tenatar reconectar b...')
                                            print('tenatando novamente...')
                                            usuario = self.chrome.find_element_by_css_selector('#login')
                                            senhaa = self.chrome.find_element_by_css_selector('#senha')
                                            entrar = self.chrome.find_element_by_css_selector('#btnLogin')
                                            sleep(1)
                                            usuario.send_keys('600045_Beatriz')
                                            sleep(1)
                                            senhaa.send_keys('Dezembro@202')
                                            sleep(1)
                                            entrar.click()
                                            sleep(3)
                                        try:
                                            sleep(3)
                                            try:
                                                fechar = self.chrome.find_element_by_css_selector(
                                                    '#modalMuralAlertas > div > div.modal-footer > button').click()
                                            except Exception:
                                                print('alo')
                                            sleep(2)
                                            operacional = self.chrome.find_element_by_css_selector(
                                                '#main-nav > div > ul > li:nth-child(2) > a')
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
                                            vendadigital = self.chrome.find_element_by_css_selector(
                                                '#produto > option:nth-child(8)')
                                            vendadigital.click()
                                            pyautogui.click(x=550, y=550)
                                            sleep(2)
                                            tipo_operacao = self.chrome.find_element_by_css_selector('#tipoOperacao')
                                            tipo_operacao.click()
                                            sleep(2)
                                            novo = self.chrome.find_element_by_css_selector(
                                                '#tipoOperacao > option:nth-child(4)')
                                            novo.click()
                                            pyautogui.click(x=550, y=550)
                                            sleep(4)
                                            orgaa = self.chrome.find_element_by_css_selector('#averbador')
                                            orgaa.click()
                                            inss = self.chrome.find_element_by_css_selector(
                                                '#averbador > option:nth-child(27)')
                                            inss.click()
                                            pyautogui.click(x=550, y=550)

                                            sleep(15)
                                            try:
                                                print('tentando conectar de primeira no banco..')
                                                bancoo = self.chrome.find_element_by_css_selector('#banco')
                                                bancoo.click()
                                                sleep(2)
                                                facta = self.chrome.find_element_by_css_selector(
                                                    '#banco > option:nth-child(7)')
                                                facta.click()
                                                pyautogui.click(x=550, y=550)
                                            except Exception:
                                                print('erro ao tentar clicar no banco.... ')
                                                print('Tentando novamente')
                                                sleep(6)
                                                bancoo = self.chrome.find_element_by_css_selector('#banco')
                                                bancoo.click()
                                                sleep(2)
                                                facta = self.chrome.find_element_by_css_selector(
                                                    '#banco > option:nth-child(7)')
                                                facta.click()
                                                pyautogui.click(x=550, y=550)
                                            sleep(2)
                                            cpff = self.chrome.find_element_by_css_selector('#cpf')
                                            cpff.send_keys(cpf)
                                            sleep(1)
                                            try:
                                                dataaa = self.chrome.find_element_by_css_selector(
                                                    '#dataNascimento').click()
                                                dataaaa = self.chrome.find_element_by_css_selector(
                                                    '#dataNascimento').send_keys(data)
                                                sleep(0.5)
                                                nomee = self.chrome.find_element_by_id('#nomeCliente').click()
                                                nomee = self.chrome.find_element_by_css_selector(
                                                    '#nomeCliente').send_keys(nome)
                                                pyautogui.click(x=550, y=550)
                                                sleep(3)
                                                solicitado = self.chrome.find_element_by_css_selector('#valor')
                                                solicitado.send_keys(financiaado)
                                                valor_solicitado = self.chrome.find_element_by_css_selector(
                                                    '#opcaoValor')
                                                valor_solicitado.click()
                                                sleep(1.5)
                                                selecionar = self.chrome.find_element_by_css_selector(
                                                    '#opcaoValor > option:nth-child(2)')
                                                selecionar.click()
                                                prazo = self.chrome.find_element_by_css_selector('#prazo')
                                                prazo.send_keys('84')
                                                pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                                                pesquisa.click()
                                                sleep(10)
                                                if tabela == 'DESBLOQUEADOS SEM CARENCIA FACTA 2,14, 120 DIAS' or tabela == 'BLOQUEADOS SEM CARENCIA FACTA 2,14 COM 120 DIAS':
                                                    In = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[4]')
                                                    In.click()
                                                if tabela == 'DESBLOQUEADOS COM CARENCIA FACTA 120 DIA 2,14' or tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS':
                                                    In1 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                    In1.click()
                                                if tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS - 1X A 84X':
                                                    In2 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                else:
                                                    print('Tabela incompativel....')

                                                sleep(2)
                                                btnn = self.chrome.find_element_by_css_selector('#etapa1')
                                                btnn.click()
                                            # data_ = self.chrome.find_element_by_css_selector('#dataNascimento')
                                            # data_.clear()
                                            # data_.send_keys(data)
                                            except Exception as e:
                                                print(e)
                                                solicitado = self.chrome.find_element_by_css_selector('#valor')
                                                solicitado.send_keys(financiaado)
                                                valor_solicitado = self.chrome.find_element_by_css_selector(
                                                    '#opcaoValor')
                                                valor_solicitado.click()
                                                sleep(1.5)
                                                selecionar = self.chrome.find_element_by_css_selector(
                                                    '#opcaoValor > option:nth-child(2)')
                                                selecionar.click()
                                                prazo = self.chrome.find_element_by_css_selector('#prazo')
                                                prazo.send_keys('84')
                                                pesquisa = self.chrome.find_element_by_css_selector('#pesquisar')
                                                pesquisa.click()
                                                sleep(8)
                                                if tabela == 'DESBLOQUEADOS SEM CARENCIA FACTA 2,14, 120 DIAS' or tabela == 'BLOQUEADOS SEM CARENCIA FACTA 2,14 COM 120 DIAS':
                                                    In = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[4]')
                                                    In.click()
                                                if tabela == 'DESBLOQUEADOS COM CARENCIA FACTA 120 DIA 2,14' or tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS':
                                                    In1 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                    In1.click()
                                                if tabela == 'BLOQUEADOS FACTA 2,14 COM CARENCIA 120 DIAS - 1X A 84X':
                                                    In2 = self.chrome.find_element_by_xpath(
                                                        '//*[@id="myTable"]/tbody/tr[6]')
                                                else:
                                                    print('Tabela incompativel....')

                                                sleep(2)
                                                btnn = self.chrome.find_element_by_css_selector('#etapa1')
                                                btnn.click()
                                        except Exception as e:
                                            print('Error Prineiro processo...', e)

                                    print('Segunda etapa...')
                                    try:
                                        sleep(2)
                                        alert = self.chrome.switch_to.alert
                                        alert.accept()
                                        sleep(1)

                                        login = self.chrome.find_element_by_css_selector(
                                            '#tab2 > fieldset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > select').click()
                                        sleep(1)
                                        Daine = self.chrome.find_element_by_css_selector(
                                            '#tab2 > fieldset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > select > option:nth-child(25)').click()

                                        pyautogui.click(x=550, y=550)

                                        sleep(2)
                                        vendedor = self.chrome.find_element_by_css_selector('#vendedor').click()
                                        vendedorB = self.chrome.find_element_by_css_selector(
                                            '#vendedor > option:nth-child(6)').click()
                                        pyautogui.click(x=550, y=550)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        btnw = self.chrome.find_element_by_css_selector('#etapa_2')
                                        btnw.click()
                                        sleep(70)
                                    except Exception as e:
                                        print(e)
                                        print('Erro no segundo processo.....')
                                        print('Tentando novamente......')
                                        pyautogui.press('f5')
                                        sleep(2)
                                        alert = self.chrome.switch_to.alert
                                        alert.accept()
                                        sleep(1)

                                        login = self.chrome.find_element_by_css_selector(
                                            '#tab2 > fieldset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > select').click()
                                        sleep(1)
                                        Daine = self.chrome.find_element_by_css_selector(
                                            '#tab2 > fieldset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > select > option:nth-child(25)').click()

                                        pyautogui.click(x=550, y=550)

                                        sleep(2)
                                        vendedor = self.chrome.find_element_by_css_selector('#vendedor').click()
                                        vendedorB = self.chrome.find_element_by_css_selector(
                                            '#vendedor > option:nth-child(6)').click()
                                        pyautogui.click(x=550, y=550)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(1.5)
                                        btnw = self.chrome.find_element_by_css_selector('#etapa_2')
                                        btnw.click()
                                        sleep(70)

                                    try:
                                        print('tereceiro processo.....')
                                        cliente = self.chrome.find_element_by_css_selector('#clienteAnalfabeto').click()
                                        nao = self.chrome.find_element_by_css_selector(
                                            '#clienteAnalfabeto > option:nth-child(3)').click()
                                        sleep(1)

                                        renda = self.chrome.find_element_by_css_selector('#valorDoBeneficio').send_keys(
                                            salario)
                                        esp = self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]').click()
                                        sleep(1)
                                        if especie == '21':
                                            B21 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[11]').click()
                                        if especie == '32':
                                            b32 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[19]').click()
                                        if especie == '41':
                                            b41 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[24]').click()
                                        if especie == '42':
                                            b42 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[25]').click()
                                        if especie == '46':
                                            b46 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[29]').click()
                                        if especie == '57':
                                            b57 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[36]').click()
                                        if especie == '92':
                                            b92 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[46]').click()
                                        if especie == '93':
                                            b93 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[47]').click()
                                        else:
                                            print('Especie vazia ou não compativel')
                                        sleep(2)
                                        UFF = self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]').click()
                                        sleep(2)
                                        if UF == 'AC':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[2]').click()
                                        if UF == 'AL':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[3]').click()
                                        if UF == 'AM':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[4]').click()
                                        if UF == 'AP':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[5]').click()
                                        if UF == 'AL':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[6]').click()
                                        if UF == 'BA':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[6]').click()
                                        if UF == 'CE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[7]').click()

                                        if UF == 'DF':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[8]').click()
                                        if UF == 'ES':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[9]').click()
                                        if UF == 'GO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[10]').click()
                                        if UF == 'MA':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[11]').click()
                                        if UF == 'MG':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[12]').click()
                                        if UF == 'MS':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[13]').click()
                                        if UF == 'MT':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[14]').click()
                                        if UF == 'PA':
                                            self.chrome.find_element_by_xpath(
                                                '#ufBeneficio > option:nth-child(15)').click()
                                        if UF == 'PB':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[16]').click()
                                        if UF == 'PE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[17]').click()
                                        if UF == 'PI':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[18]').click()
                                        if UF == 'PR':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[19]').click()
                                        if UF == 'RJ':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[20]').click()
                                        if UF == 'RN':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[21]').click()
                                        if UF == 'RO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[22]').click()
                                        if UF == 'RR':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[23]').click()
                                        if UF == 'RS':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[24]').click()
                                        if UF == 'SC':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[25]').click()
                                        if UF == 'SE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[26]').click()
                                        if UF == 'SP':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[27]').click()
                                        if UF == 'TO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[28]').click()
                                        tipo= self.chrome.find_element_by_xpath('//*[@id="mesaCreditoTipoBeneficio"]').click()
                                        tipoC= self.chrome.find_element_by_xpath('//*[@id="mesaCreditoTipoBeneficio"]/option[2]').click()
                                        sleep(1)
                                        cepp = self.chrome.find_element_by_css_selector('#cep')
                                        cepp.click()
                                        cepp.send_keys(cep)
                                        sleep(1)
                                        pesquisaa = self.chrome.find_element_by_css_selector('#pesquisar_cep').click()
                                        end = self.chrome.find_element_by_css_selector('#endereco').clear()
                                        sleep(1)
                                        sleep(3)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        en = self.chrome.find_element_by_css_selector('#endereco').send_keys(rua)
                                        sleep(2)

                                        nuber = self.chrome.find_element_by_css_selector('#numero').clear()
                                        nube = self.chrome.find_element_by_css_selector('#numero').send_keys('12')
                                        sleep(2)
                                        bairrr = self.chrome.find_element_by_css_selector('#bairro').clear()
                                        bairrrr = self.chrome.find_element_by_css_selector('#bairro').send_keys(bairro)
                                        sleep(2)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(1)
                                        cidadee = self.chrome.find_element_by_css_selector('#cidade').click()
                                        pyautogui.press('down')
                                        pyautogui.press('enter')
                                        cel = self.chrome.find_element_by_css_selector('#celular')
                                        cel.click()
                                        cel1 = self.chrome.find_element_by_css_selector('#celular')
                                        cel1.send_keys(numeroTel)
                                        sleep(2)
                                        resi = self.chrome.find_element_by_css_selector('#tipoResidencia').click()
                                        familiar = self.chrome.find_element_by_css_selector(
                                            '#tipoResidencia > option:nth-child(3)').click()
                                        sleep(2)
                                        emaill = self.chrome.find_element_by_css_selector('#email').click()
                                        sleep(1)
                                        emaii = self.chrome.find_element_by_css_selector('#email').send_keys(email)

                                        sleep(4)
                                        btn3 = self.chrome.find_element_by_css_selector('#etapa_3')
                                        btn3.click()
                                        sleep(20)
                                    except Exception as e:
                                        print(e)
                                        print('Erro no terceiro processo')
                                        print(' Tentando novamenete.....')
                                        print('tereceiro processo.....')
                                        cliente = self.chrome.find_element_by_css_selector('#clienteAnalfabeto').click()
                                        nao = self.chrome.find_element_by_css_selector(
                                            '#clienteAnalfabeto > option:nth-child(3)').click()
                                        sleep(1)

                                        renda = self.chrome.find_element_by_css_selector('#valorDoBeneficio').send_keys(
                                            salario)
                                        esp = self.chrome.find_element_by_xpath('//*[@id="tipobeneficio"]').click()
                                        sleep(1)
                                        if especie == '21':
                                            B21 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[11]').click()
                                        if especie == '32':
                                            b32 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[19]').click()
                                        if especie == '41':
                                            b41 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[24]').click()
                                        if especie == '42':
                                            b42 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[25]').click()
                                        if especie == '46':
                                            b46 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[29]').click()
                                        if especie == '57':
                                            b57 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[36]').click()
                                        if especie == '92':
                                            b92 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[46]').click()
                                        if especie == '93':
                                            b93 = self.chrome.find_element_by_xpath(
                                                '//*[@id="tipobeneficio"]/option[47]').click()
                                        else:
                                            print('Especie vazia ou não compativel')
                                        sleep(2)
                                        UFF = self.chrome.find_element_by_xpath('//*[@id="ufBeneficio"]').click()
                                        sleep(2)
                                        if UF == 'AC':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[2]').click()
                                        if UF == 'AL':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[3]').click()
                                        if UF == 'AM':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[4]').click()
                                        if UF == 'AP':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[5]').click()
                                        if UF == 'AL':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[6]').click()
                                        if UF == 'BA':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[6]').click()
                                        if UF == 'CE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[7]').click()

                                        if UF == 'DF':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[8]').click()
                                        if UF == 'ES':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[9]').click()
                                        if UF == 'GO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[10]').click()
                                        if UF == 'MA':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[11]').click()
                                        if UF == 'MG':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[12]').click()
                                        if UF == 'MS':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[13]').click()
                                        if UF == 'MT':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[14]').click()
                                        if UF == 'PA':
                                            self.chrome.find_element_by_xpath(
                                                '#ufBeneficio > option:nth-child(15)').click()
                                        if UF == 'PB':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[16]').click()
                                        if UF == 'PE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[17]').click()
                                        if UF == 'PI':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[18]').click()
                                        if UF == 'PR':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[19]').click()
                                        if UF == 'RJ':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[20]').click()
                                        if UF == 'RN':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[21]').click()
                                        if UF == 'RO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[22]').click()
                                        if UF == 'RR':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[23]').click()
                                        if UF == 'RS':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[24]').click()
                                        if UF == 'SC':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[25]').click()
                                        if UF == 'SE':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[26]').click()
                                        if UF == 'SP':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[27]').click()
                                        if UF == 'TO':
                                            self.chrome.find_element_by_xpath(
                                                '//*[@id="ufBeneficio"]/option[28]').click()

                                        sleep(1)
                                        tipo = self.chrome.find_element_by_xpath(
                                            '//*[@id="mesaCreditoTipoBeneficio"]').click()
                                        tipoC = self.chrome.find_element_by_xpath(
                                            '//*[@id="mesaCreditoTipoBeneficio"]/option[2]').click()
                                        sleep(1)
                                        cepp = self.chrome.find_element_by_css_selector('#cep')
                                        cepp.click()
                                        cepp.send_keys(cep)
                                        sleep(1)
                                        pesquisaa = self.chrome.find_element_by_css_selector('#pesquisar_cep').click()
                                        end = self.chrome.find_element_by_css_selector('#endereco').clear()
                                        sleep(1)
                                        sleep(3)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        en = self.chrome.find_element_by_css_selector('#endereco').send_keys(rua)
                                        sleep(2)

                                        nuber = self.chrome.find_element_by_css_selector('#numero').clear()
                                        nube = self.chrome.find_element_by_css_selector('#numero').send_keys('12')
                                        sleep(2)
                                        bairrr = self.chrome.find_element_by_css_selector('#bairro').clear()
                                        bairrrr = self.chrome.find_element_by_css_selector('#bairro').send_keys(bairro)
                                        sleep(2)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(1)
                                        cidadee = self.chrome.find_element_by_css_selector('#cidade').click()
                                        pyautogui.press('down')
                                        pyautogui.press('enter')
                                        cel = self.chrome.find_element_by_css_selector('#celular')
                                        cel.click()
                                        cel1 = self.chrome.find_element_by_css_selector('#celular')
                                        cel1.send_keys(numeroTel)
                                        sleep(2)
                                        resi = self.chrome.find_element_by_css_selector('#tipoResidencia').click()
                                        familiar = self.chrome.find_element_by_css_selector(
                                            '#tipoResidencia > option:nth-child(3)').click()
                                        sleep(2)
                                        emaill = self.chrome.find_element_by_css_selector('#email').click()
                                        sleep(1)
                                        emaii = self.chrome.find_element_by_css_selector('#email').send_keys(email)

                                        sleep(4)
                                        btn3 = self.chrome.find_element_by_css_selector('#etapa_3')
                                        btn3.click()
                                        sleep(20)
                                    print('Quarto  Processo...')
                                    try:
                                        sleep(2)
                                        sleep(2)
                                        bac = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]').click()
                                        if banco == '25':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[24]')
                                        if banco == '28':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[3]')
                                        if banco == '40':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[24]')
                                        if banco == '37':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[37]')
                                        if banco == '1':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[2]')
                                        if banco == '27':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[5]')
                                        if banco == '33':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[14]')
                                        if banco == '17':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[4]')
                                        if banco == '22':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[19]')
                                        # if banco == '26':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '21':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[31]')
                                        if banco == '19':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[55]')
                                        if banco == '32':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[11]')
                                        if banco == '15':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[13]')
                                        # if banco == '11':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '5':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[36]')
                                        if banco == '12':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[32]')
                                        if banco == '35':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[15]')
                                        if banco == '4':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[10]')
                                        if banco == '16':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[16]')
                                        if banco == '9':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[51]')
                                        if banco == '20':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[38]')
                                        if banco == '3':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[23]')
                                        if banco == '31':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[15]')
                                        if banco == '10':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[52]')
                                        # if banco == '36':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '6':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[39]')
                                        if banco == '34':
                                            c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '14':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[42]')
                                        if banco == '30':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[33]')
                                        if banco == '23':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[35]')
                                        # if banco == '18':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        # if banco == '29':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '8':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[49]')
                                        if banco == '7':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[46]')
                                        if banco == '2':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[9]')
                                        if banco == '24':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[55]')
                                        if banco == '13':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[54]')

                                        if banco == '38':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[20]')
                                        sleep(5)

                                        agenciacamp = self.chrome.find_element_by_xpath(
                                            '//*[@id="agenciaLiberacao"]').send_keys(agencia)
                                        sleep(1)
                                        contaa = self.chrome.find_element_by_xpath(
                                            '//*[@id="contaLiberacao"]').send_keys(numeroconta)
                                        sleep(2)
                                        Ramo = self.chrome.find_element_by_css_selector('#id_ramo_atividade_or').click()
                                        ram = self.chrome.find_element_by_css_selector(
                                            '#id_ramo_atividade_or > option:nth-child(8)').click()
                                        sleep(3)
                                        prof = self.chrome.find_element_by_css_selector('#id_tipo_profissao_or').click()
                                        prof1 = self.chrome.find_element_by_css_selector(
                                            '#id_tipo_profissao_or > option:nth-child(2)').click()
                                        sleep(3)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        btn4 = self.chrome.find_element_by_css_selector('#etapa_4').click()
                                    except Exception as e:
                                        print(e)
                                        print('Erro no quarto processo....')
                                        print('Tenatndo novamente ')
                                        sleep(2)
                                        bac = self.chrome.find_element_by_xpath('//*[@id="bancoLiberacao"]').click()
                                        if banco == '25':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[24]')
                                        if banco == '28':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[3]')
                                        if banco == '40':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[24]')
                                        if banco == '37':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[37]')
                                        if banco == '1':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[2]')
                                        if banco == '27':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[5]')
                                        if banco == '33':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[14]')
                                        if banco == '17':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[4]')
                                        if banco == '22':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[19]')
                                        # if banco == '26':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '21':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[31]')
                                        if banco == '19':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[55]')
                                        if banco == '32':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[11]')
                                        if banco == '15':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[13]')
                                        # if banco == '11':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '5':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[36]')
                                        if banco == '12':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[32]')
                                        if banco == '35':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[15]')
                                        if banco == '4':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[10]')
                                        if banco == '16':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[16]')
                                        if banco == '9':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[51]')
                                        if banco == '20':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[38]')
                                        if banco == '3':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[23]')
                                        if banco == '31':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[15]')
                                        if banco == '10':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[52]')
                                        # if banco == '36':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '6':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[39]')
                                        if banco == '34':
                                            c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '14':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[42]')
                                        if banco == '30':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[33]')
                                        if banco == '23':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[35]')
                                        # if banco == '18':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        # if banco == '29':
                                        # c1 = self.chrome.find_element_by_xpath('')
                                        if banco == '8':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[49]')
                                        if banco == '7':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[46]')
                                        if banco == '2':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[9]')
                                        if banco == '24':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[55]')
                                        if banco == '13':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[54]')

                                        if banco == '38':
                                            c1 = self.chrome.find_element_by_xpath(
                                                '//*[@id="bancoLiberacao"]/option[20]')
                                        sleep(3)
                                        sleep(15)
                                        agenciacamp = self.chrome.find_element_by_xpath(
                                            '//*[@id="agenciaLiberacao"]').send_keys(agencia)
                                        sleep(1)
                                        contaa = self.chrome.find_element_by_xpath(
                                            '//*[@id="contaLiberacao"]').send_keys(numeroconta)
                                        sleep(2)
                                        Ramo = self.chro
                                        me.find_element_by_css_selector('#id_ramo_atividade_or').click()
                                        ram = self.chrome.find_element_by_css_selector(
                                            '#id_ramo_atividade_or > option:nth-child(8)').click()
                                        sleep(1)
                                        prof = self.chrome.find_element_by_css_selector('#id_tipo_profissao_or').click()
                                        prof1 = self.chrome.find_element_by_css_selector(
                                            '#id_tipo_profissao_or > option:nth-child(2)').click()
                                        sleep(3)
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        sleep(2)
                                        btn4 = self.chrome.find_element_by_css_selector('#etapa_4').click()

                                    try:
                                        print('Quinto processo...')
                                        sleep(40)
                                        codigo = self.chrome.find_element_by_css_selector(
                                            '#content-wrapper > div > div > div > div:nth-child(2) > h3:nth-child(1)').text
                                        print(codigo)
                                        digital = self.chrome.find_element_by_css_selector(
                                            '#content-wrapper > div > div > div > div:nth-child(3) > div.span6 > div:nth-child(3) > input[type=radio]').click()
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        form = self.chrome.find_element_by_css_selector(
                                            '#btnRealizaFormalizacao').click()
                                        sleep(2)
                                        try:
                                            py = self.chrome.find_element_by_css_selector(
                                                '#corpo > div.bootbox.modal.fade.in > div.modal-footer > a').click()
                                            sleep(2)
                                        except Exception:
                                            print('mesagem não apareceu')
                                        op = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > a').click()

                                        sleep(1)
                                        consultas = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(6) > a').click()
                                        anda = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(6) > ul > li:nth-child(2) > a > span').click()
                                        sleep(2)

                                        cod = self.chrome.find_element_by_css_selector('#cpf').click()
                                        cod1 = self.chrome.find_element_by_css_selector('#cpf').send_keys(cpf)

                                        pes = self.chrome.find_element_by_css_selector('#pesquisar').click()
                                        sleep(10)
                                        self.chrome.execute_script("window.scrollTo(0, 620)")
                                        sleep(5)
                                        link = self.chrome.find_element_by_css_selector(
                                            '#tblListaProposta > tbody > tr:nth-child(1) > td:nth-child(22) > i').click()
                                        print(link)
                                        sleep(2)
                                        alert = self.chrome.switch_to.alert
                                        alert.accept()
                                        sleep(1)


                                    except Exception as e:
                                        print(e)
                                        self.chrome.refresh()
                                        print('Tentando o quinto processooo.....')
                                        sleep(40)
                                        codigo = self.chrome.find_element_by_css_selector(
                                            '#content-wrapper > div > div > div > div:nth-child(2) > h3:nth-child(1)').text
                                        print(codigo)
                                        digital = self.chrome.find_element_by_css_selector(
                                            '#content-wrapper > div > div > div > div:nth-child(3) > div.span6 > div:nth-child(3) > input[type=radio]').click()
                                        self.chrome.find_element_by_tag_name('body').send_keys(Keys.END)
                                        form = self.chrome.find_element_by_css_selector(
                                            '#btnRealizaFormalizacao').click()
                                        sleep(2)
                                        try:
                                            py = self.chrome.find_element_by_css_selector(
                                                '#corpo > div.bootbox.modal.fade.in > div.modal-footer > a').click()
                                            sleep(2)
                                        except Exception:
                                            print('mesagem não apareceu')
                                        op = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > a').click()
                                        self.chrome.execute_script("window.scrollTo(0, 55)")
                                        sleep(1)
                                        consultas = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(6) > a').click()
                                        anda = self.chrome.find_element_by_css_selector(
                                            '#main-nav > div > ul > li:nth-child(2) > ul > li:nth-child(6) > ul > li:nth-child(2) > a > span').click()
                                        sleep(2)

                                        cod = self.chrome.find_element_by_css_selector('#cpf').click()
                                        cod1 = self.chrome.find_element_by_css_selector('#cpf').send_keys(cpf)

                                        pes = self.chrome.find_element_by_css_selector('#pesquisar').click()

                                        sleep(6)
                                        self.chrome.execute_script("window.scrollTo(0, 120)")
                                        sleep(15)

                                        link = self.chrome.find_element_by_css_selector(
                                            '#tblListaProposta > tbody > tr:nth-child(1) > td:nth-child(22) > i').click()
                                        print(link)
                                        sleep(2)
                                        alert = self.chrome.switch_to.alert
                                        alert.accept()
                                        sleep(1)
                                    chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
                                    self.chrome.refresh()
                                    sleep(16)
                                    print('Sexto processo....')

                                    try:

                                        sleep(4)
                                        camp_nome = self.chrome.find_element_by_id('login')
                                        sleep(1)
                                        camp_senha = self.chrome.find_element_by_id('password')
                                        sleep(1)
                                        camp_entrar = self.chrome.find_element_by_class_name('jss10')
                                        camp_nome.send_keys('t.i')
                                        sleep(3)
                                        camp_senha.send_keys('179202*')
                                        sleep(1)
                                        camp_entrar.click()
                                        sleep(6)
                                        camp_cliente = self.chrome.find_element_by_css_selector(
                                            '#menu-100 > div > div > div > ul:nth-child(3)')
                                        sleep(5)
                                        camp_cliente.click()

                                        sleep(4)
                                        pesquisa = self.chrome.find_element_by_css_selector('#searchInput')
                                        sleep(1)
                                        pesquisa.send_keys('33478520606')
                                        sleep(1)
                                        pyautogui.press('enter')
                                        sleep(6)

                                        pontos = self.chrome.find_element_by_css_selector(
                                            '#main-content > div:nth-child(1) > div > div.jss132.jss136.jss133.jss339 > div.jss343 > table > tbody > tr:nth-child(1) > td:nth-child(25) > div > button')
                                        pontos.click()
                                        sleep(1)
                                        visualizar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss164.menu-suspenso > div.jss132.jss162.jss142.jss133.jss163 > ul > li:nth-child(2)')
                                        visualizar.click()
                                        sleep(2)
                                        colar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss164.modal.modal-minimizavel > div:nth-child(2) > div.modalBody.modal-propostas > form > fieldset:nth-child(3) > textarea')
                                        colar.click()
                                        pyautogui.hotkey('ctrl', 'v')
                                        sleep(1)
                                        salvar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss164.modal.modal-minimizavel > div:nth-child(2) > div.modalBody.modal-propostas > form > div > button.jss198.jss174.jss176.jss179.jss456.submit').click()
                                        sleep(10)
                                        status = self.chrome.find_element_by_xpath(
                                            '//*[@id="filtro-paper"]/div/div[1]/div[8]').click()
                                        sleep(2)
                                        aceite = self.chrome.find_element_by_class_name('input-busca-filtro').send_keys(
                                            'AGUARDANDO DIGITAÇÃO')
                                        sleep(1)
                                        aceite = self.chrome.find_element_by_css_selector(
                                            'body > div.jss71.jss144.jss145 > div.jss39.jss65.jss40.jss147.jss148.jss151 > div.jss321.dialog-filter > label:nth-child(5)').click()
                                        sleep(1)
                                        aplicar = self.chrome.find_element_by_css_selector(
                                            'body > div.jss71.jss144.jss145 > div.jss39.jss65.jss40.jss147.jss148.jss151 > div.jss322 > button.jss105.jss81.jss83.jss86.applyFilters.jss323 > span.jss82').click()
                                        sleep(3)

                                        banco = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(1) > div:nth-child(4)').click()
                                        sleep(1)
                                        aceite = self.chrome.find_element_by_class_name('input-busca-filtro').send_keys(
                                            'facta')
                                        sleep(1)
                                        facta1 = self.chrome.find_element_by_class_name('checkbox-description').click()
                                        sleep(1)
                                        plicar = self.chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/button[2]').click()
                                        sleep(3)
                                        data = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div > input[type=text]').click()
                                        sleep(4)
                                        seta = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()
                                        seta = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()
                                        seta = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > button.react-datepicker__navigation.react-datepicker__navigation--previous').click()

                                        data1 = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker__portal > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(1) > div.react-datepicker__day.react-datepicker__day--wed').click()
                                        sleep(1)
                                        filtro = self.chrome.find_element_by_css_selector(
                                            '#filtro-paper > div > div:nth-child(3) > div.sc-jAaTju.fVRxI').click()
                                        sleep(5)
                                        menu = self.chrome.find_element_by_css_selector(
                                            '#topo > button.jss105.jss81.jss90.jss93.hamburguer').click()
                                        print('atualizando...')
                                        sleep(5)
                                        refre = self.chrome.find_element_by_xpath(
                                            '//*[@id="filtro-paper"]/div/div[3]/div[2]').click()

                                    except Exception as a:
                                        print(a)
                                        print('erro')





                      except Exception:
                        print('Sem propostas,  atualizando...')
                        sleep(20)
                        refre = self.chrome.find_element_by_xpath('//*[@id="filtro-paper"]/div/div[3]/div[2]').click()

        except Exception as e:
            print(e)
            print('erro nos filtros')




if __name__ == '__main__':

    chrome = ChromeAuto()

    chrome.acessar('https://app.ecorban.com/grupo-digital-sf')
    chrome.login()
    sleep(6)
    chrome.proposta()
    sleep(2)



chrome.captura_de_campos()
fim=time.time()
tempo=fim  - inicio
print(tempo)