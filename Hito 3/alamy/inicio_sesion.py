
#se ocupo selenium
from selenium import webdriver 
from time import sleep
#datos a ingresar      
correo = "kmurphyp_t328i@hxsni.com"  #nombre de usuario que corresponde al correo
password = "Cokefer777" #contraseña, se va ir probando y realizando el ataque 
#pagina
link = "https://www.alamy.es/log-in/"

#Automatizacion de inicio de sesion (nombre de usuario y contraseña)
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")

driver.get(link)
sleep(2)
driver.find_element_by_name("email").send_keys(correo)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("btnIniciarsesión").click()
driver.close()


