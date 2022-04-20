from selenium import webdriver

email="margie11i_j620w@hxsni.com"
password="123456"
url="https://www.serviceshop.cl/customer/login" 

driver= webdriver.Chrome("/Users/Desktop/chromedriver")
driver.get(url)

driver.find_element_by_name("mail").send_keys(mail)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()

print("efectuo correctamente")