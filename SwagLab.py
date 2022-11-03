from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

username = "standard_user"
password = "secret_sauce"

url = "https://www.saucedemo.com/"

driver = webdriver.Chrome("C:/Users/EQUIPO/Desktop/Nueva carpeta (5)/TQA/Proyectos/a1/chromedriver")

driver.get(url)
driver.maximize_window()
sleep(3)
driver.find_element(By.ID,"user-name").send_keys(username)
sleep(3)
driver.find_element(By.NAME,"password").send_keys(password)
sleep(3)
driver.find_element(By.ID, "login-button").click()

print("Inicio de sesión correcto")

driver.quit()
