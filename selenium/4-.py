from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

# Realizar una consulta en Google y validar el valor del primer resultado, al final debe mostrar si el valor es correcto o no de acuerdo al resultado esperado

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com/")

#wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

driver.find_element(By.NAME, 'q').send_keys('Luis Angel Vanegas Martinez')
driver.find_element(By.NAME,'btnK').click() 
#wait.until(EC.element_to_be_clickable((By.NAME,'btnK'))).click()
resultadoObtenido = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3').text

resultadoEsperado = 'Luis Angel Vanegas Martinez - Senior QA Automation ...'

time.sleep(10)

print('Valor del primer resultado: '+ resultadoObtenido)

if (resultadoObtenido == resultadoEsperado):
    print('Prueba Exitosa! El valor es correcto')
else:
    print('Prueba Fallida, el valor es INCORRECTO')

driver.quit()

# APRENDIZAJE:
# send_keys()
# click()
# Keys
# webDriverWait (FluentWait)
# expected_conditions