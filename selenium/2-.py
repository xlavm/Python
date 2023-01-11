from selenium import webdriver
import time

# Levanta el navegador de chrome y accede a Google.com

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com/")

time.sleep(500)

driver.quit()

# APRENDIZAJE:
# get()