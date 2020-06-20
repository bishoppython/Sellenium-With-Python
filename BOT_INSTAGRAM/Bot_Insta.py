from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\ander\OneDrive\Área de Trabalho\BOT_INSTAGRAM\geckodriver.exe')

    def login(self):
        driver = self.driver
        #driver.get('https://www.instagram.com/accounts/emailsignup/')
        driver.get('https://www.instagram.com')
        time.sleep(2)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")  # referencia do botão de acesso
        #login_button.click()                    # Clica no Botão
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()                    #Limpa o campo onde vai ser digitado o usuário
        user_element.send_keys(self.username)   # Passa os paramentros para ser digitados
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtir_fotos('Empreendedorismo')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
        time.sleep(5)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            for i in range(1,2):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
            try:
                find_class = driver.find_elements_by_class_name('//button[@class="wpO6b ]"').click()
                time.sleep(19)
            except Exception as e:
                time.sleep(5)

BishopXBot = InstagramBot('bishopxti', 'Abaporojucaiba')
BishopXBot.login()