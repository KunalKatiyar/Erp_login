from selenium import webdriver
import time

from selenium .webdriver.common.keys import Keys
driver= webdriver.Chrome(r"(CHROMEDRIVER PATH LOCATION HERE!)")
driver.get("https://erp.iitkgp.ac.in/SSOAdministration/login.htm?sessionToken=D04CA8D2D3D39CC55C7C301AC6E2C48C.worker2&requestedUrl=https://erp.iitkgp.ac.in/IIT_ERP3/home.htm")
elem = driver.find_element_by_name("user_id")
elem.clear()
elem.send_keys("(id here)")
elem2 = driver.find_element_by_name("password")
elem2.clear()
elem2.send_keys("(password here)")
time.sleep(1)
elem3 = driver.find_element_by_name("answer")
elem3.clear()
elem4 =driver.find_element_by_class_name("control-label").text
if elem4 == "Question1":
    elem3.send_keys("Answer1")
elif elem4 == "Question2":
    elem3.send_keys("Answer2")
else:
    elem3.send_keys("Answer3")

elem.send_keys(Keys.RETURN)
