#se ocupo selenium
from selenium import webdriver 
#datos a ingresar      
correo = "yetone7093@eoscast.com"  #nombre de usuario que corresponde al correo
#pagina
link = "https://www.serviceshop.cl/customer/login"

#Automatizacion de inicio de sesion (nombre de usuario y contraseña)
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")

driver.get(link)

driver.find_element_by_id("reset_password").click()

driver.find_element_by_name("customer[email]").send_keys(correo)

driver.find_element_by_css_selector("input[type=\"submit\" i]").click()

driver.close()
