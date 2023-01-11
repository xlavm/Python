from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Levanta el navegador de chrome y accede a Google.com y obten el VALOR del pais que aparece en la pagina principal

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com/")

paisObtenido = driver.find_element(By.CLASS_NAME, 'uU7dJb').text

time.sleep(10)

print('El Pais que aparece en la pagina principal es: '+ paisObtenido)

driver.quit()

# APRENDIZAJE:
# find_element()
# By
# CLASS_NAME
# .text