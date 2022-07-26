from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\\Users\\itctesting22\\Downloads\\selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("C:\\Users\\itctesting22\\Desktop\\web site\\student.html")
driver.find_element(By.CLASS_NAME,"loginbtn").click()
driver.find_element(By.CLASS_NAME,"toggle-btn2").click()
driver.find_element(By.ID,"fname").send_keys("chaithra")
driver.find_element(By.ID,"laname").send_keys("mn")
driver.find_element(By.ID,"email").send_keys("chaithra@gmail.com")
driver.find_element(By.ID,"pass").send_keys("12345Cha")
driver.find_element(By.ID,"con").send_keys("12345Cha")
driver.find_element(By.ID,"gender2").click()
driver.find_element(By.ID,"check").click()
driver.find_element(By.ID,"res").click()

