from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image
import time

# Driver para chrome
browserDriver = Service("Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=browserDriver)
driver.maximize_window()
driver.get("https://zonasegura.incarail.app/itinerario/buscar")

time.sleep(2)

driver.save_screenshot('prueba1/img/prueba2.png')
# screenshot = Image.open('prueba1/img/prueba1.png')
# screenshot.show()