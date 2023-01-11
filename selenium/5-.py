from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

# Realizar una consulta en Google y validar el valor del primer resultado, al final debe mostrar si el valor es correcto o no de acuerdo al resultado esperado

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com/")
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

wait.until(EC.element_to_be_clickable((By.NAME,'q'))).send_keys('Luis Angel Vanegas Martinez')
wait.until(EC.element_to_be_clickable((By.NAME,'btnK'))).click()

class ClasePrincipal(unittest.TestCase):
    def CasoPositivo(self):
        resultadoObtenido = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3'))).text
        resultadoEsperado = "Luis Angel Vanegas Martinez - Senior QA Automation ..."
        mensajeDeError = "ERROR: Los valores no son iguales!"
        self.assertEqual(resultadoObtenido, resultadoEsperado, mensajeDeError)
  
unittest.main()

driver.quit()

# APRENDIZAJE:
# unittest
# asserts
