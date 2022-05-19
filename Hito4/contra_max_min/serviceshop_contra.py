import random as rd
#se ocupo selenium
from selenium import webdriver 
letras= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros= '0123456789'
simbolos= '!@#$%^&><'
superscript = '₁ⁱₕ₉ₘ₊⁼⁽ₔ⁰'
emojis = '🌝💓😢🙉'
simbolos= '!@#$%^&><'
arabic = 'ڜ ﭗ ﺹ ﻇ ﻨ ﻩ ﻲ'
intentos=6
tamaño= 1 #Tamaño para determinar el largo permitido minimo/maximo
unidos= f'{letras}{numeros}{arabic}{emojis}{superscript}{simbolos}'  #Se va probando con cada
l=1  #Largo de contraseña (se va modificando)
#Automatizacion de inicio de sesion (nombre de usuario y contraseña)
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")
#contra= ''.join(rd.sample(unidos,N))
#datos a ingresar      
correo = "cokeffere@mozej.com"  #nombre de usuario que corresponde al correo
telefono= "+56966666666" #Telefono
#password = "" contraseña, se va ir probando y realizando el ataque 
#pagina
link = "https://www.serviceshop.cl/customer/registration"
for i in range(intentos):
    driver.get(link)
    tamaño=rd.randint(1,l)
    contra= ''.join(rd.sample(unidos,tamaño))
    driver.find_element_by_name("customer[email]").send_keys(correo)
    driver.find_element_by_name("customer[phone]").send_keys(telefono)
    driver.find_element_by_name("customer[password]").send_keys(contra)
    driver.find_element_by_name("customer[password_confirmation]").send_keys(contra)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    l=l+1 

driver.close()
