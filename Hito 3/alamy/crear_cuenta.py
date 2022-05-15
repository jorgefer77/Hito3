#se ocupo selenium
from selenium import webdriver 
from time import sleep
#datos a ingresar
sexo = 1      
correo = "kmurphyp_t328i@hxsni.com"  #nombre de usuario que corresponde al correo
password = "Cokefer777" #contraseña, se va ir probando y creando la cuenta

link = "https://www.alamy.es/create-customer-account/"

driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")
driver.get(link)
driver.find_element_by_name("email").send_keys(correo)
driver.find_element_by_name("password").send_keys(password)

driver.find_element_by_id("btnCreesucuentaahora").click()

driver.close()