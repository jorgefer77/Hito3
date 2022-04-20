from selenium import webdriver

email="margie11i_j620w@hxsni.com"

url="https://www.serviceshop.cl/customer/login"

driver= webdriver.Chrome("/Users/Desktop/chromedriver")
driver.get(url)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
driver.find_element_by_name("mail").send_keys(mail)


print("efectuo correctamente")