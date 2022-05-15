#se ocupo selenium
from selenium import webdriver 
#datos a ingresar      
correo = "yetone7093@eoscast.com"  #nombre de usuario que corresponde al correo
telefono= "+56966666666"
password = "LA37gl85xp2f" #contraseña
#pagina
link = "https://www.serviceshop.cl/customer/registration"

#Automatizacion de registro (con el nombre de usuario y contraseña)
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")

driver.get(link)

driver.find_element_by_name("customer[email]").send_keys(correo)

driver.find_element_by_name("customer[phone]").send_keys(telefono)
driver.find_element_by_name("customer[password]").send_keys(password)
driver.find_element_by_name("customer[password_confirmation]").send_keys(password)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()

driver.close()
