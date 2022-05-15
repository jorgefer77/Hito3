#se ocupo selenium
from selenium import webdriver 
#datos a ingresar      
correo = "kmurphyp_t328i@hxsni.com"  #nombre de usuario que corresponde al correo
#pagina
link = "https://www.alamy.es/log-in/"

#Automatizacion de restablecimiento contraseña
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")

driver.get(link)

driver.find_element_by_id("linkIdforgotPwd").click()

driver.find_element_by_name("email").send_keys(correo)

driver.find_element_by_id("btnEnviaremailderestablecimiento").click()

driver.close()
