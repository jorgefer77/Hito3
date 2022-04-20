from selenium import webdriver

email="margie11i_j620w@hxsni.com"
tel="95456431"
password="123456"
url="https://www.serviceshop.cl/customer/registration" 

driver= webdriver.Chrome("/Users/Desktop/chromedriver")
driver.get(url)

driver.find_element_by_name("mail").send_keys(mail)
driver.find_element_by_name("tel").send_keys(tel)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()

print("efectuo correctamente")

