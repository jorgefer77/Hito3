#se ocupo selenium
from selenium import webdriver 
from time import sleep
#datos a ingresar      
correo = "kmurphyp_t328i@hxsni.com"  #nombre de usuario que corresponde al correo
password = "Cokefer777" #contraseña, se va ir probando y realizando el ataque 
contra_nueva = "Coke.s.7777"
#pagina
link = "https://www.alamy.es/myalamycustomer.aspx"
url = "https://www.alamy.es/log-in/"
#Automatizacion de inicio de sesion (nombre de usuario y contraseña) para luego modif. contraseña
driver = webdriver.Chrome("/home/coke/Documentos/Hito2/chromedriver")
driver.get(url)
sleep(1)
driver.find_element_by_name("email").send_keys(correo)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("btnIniciarsesión").click()

sleep(5)
driver.get(link)
sleep(2)
#driver.find_element_by_xpath('//*[@id="__next"]/div/header/nav/ul/li[4]/a/div/span[1]/svg').click()
#driver.find_element_by_xpath('//*[@id="account"]/div/div[2]/div/ul/li[1]/a/span/span').click()
driver.find_element_by_id("ChangePasswodChange").click()
sleep(1)

driver.find_element_by_id("CurrentPassword").send_keys(password)
sleep(1)
driver.find_element_by_id("Changepassword").send_keys(contra_nueva)
sleep(1)
driver.find_element_by_id("SavePasswodChange").click()
sleep(1)
driver.close()
