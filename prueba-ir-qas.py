from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import date, timedelta, datetime
import os
import time

# Se crea el directorio para guardar las imagenes
nomDirectorio = datetime.today().strftime('%d%m%Y%H%M%S')
dirImagen = nomDirectorio + "/img"

try:
    os.mkdir(nomDirectorio)
    os.mkdir(dirImagen)
except OSError:
    print("La creación del directorio %s falló" % dirImagen)
else:
    print("Se ha creado el directorio: %s " % dirImagen)

# Obtenemos la fecha actual y le sumamos días para la busqueda de itinerarios.
fecActual = date.today()
fecViajeIda = (fecActual + timedelta(5)).strftime('%d/%m/%Y')
idFecViajeIda = (fecActual + timedelta(5)).strftime('%d%m%Y')

fecViajeRegreso = (fecActual + timedelta(5)).strftime('%d/%m/%Y')
idFecViajeRegreso = (fecActual + timedelta(5)).strftime('%d%m%Y')

# Driver para chrome
browserDriver = Service("Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=browserDriver)
time.sleep(1)

driver.maximize_window()
driver.get("https://zonasegura.incarail.app/itinerario/buscar")

# paso 1
WebDriverWait(driver, 1).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section[4]/div/div/div/section/form/div/div[1]/div/label[1]'))).click()
driver.execute_script('document.getElementById("fecViajeIda").removeAttribute("readonly")')
WebDriverWait(driver, 1).until(ec.element_to_be_clickable((By.ID, 'fecViajeIda'))).clear()
WebDriverWait(driver, 1).until(ec.element_to_be_clickable((By.ID, 'fecViajeIda'))).send_keys(fecViajeIda)
WebDriverWait(driver, 1).until(ec.element_to_be_clickable((By.ID, 'fecViajeRegreso'))).click()
time.sleep(1)
driver.execute_script('document.getElementById("fecViajeRegreso").removeAttribute("readonly")')
WebDriverWait(driver, 1).until(ec.element_to_be_clickable((By.ID, 'fecViajeRegreso'))).clear()
WebDriverWait(driver, 1).until(ec.element_to_be_clickable((By.ID, 'fecViajeRegreso'))).send_keys(fecViajeRegreso)
time.sleep(3)
driver.save_screenshot(dirImagen + '/paso1.png')
WebDriverWait(driver, 1).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input#botonBuscar'))).click()

# paso 2
WebDriverWait(driver, 25).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section[4]/div/div/div[1]/div/div/div[1]/div[2]/label[1]'))).click()
WebDriverWait(driver, 16).until(ec.element_to_be_clickable((By.ID, 'frecuencia5420'))).click()

time.sleep(2)

WebDriverWait(driver, 18).until(ec.element_to_be_clickable((By.ID, 'r1s2f1fec' + idFecViajeIda + '11'))).click()
driver.save_screenshot(dirImagen + '/paso2-ida.png')
WebDriverWait(driver, 19).until(ec.element_to_be_clickable((By.ID, 'continuar15420'))).click()
time.sleep(1)

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section[4]/div/div/div[1]/div/div/div[2]/div[2]/label[1]'))).click()
WebDriverWait(driver, 21).until(ec.element_to_be_clickable((By.ID, 'frecuencia61612'))).click()
time.sleep(2)

WebDriverWait(driver, 22).until(ec.element_to_be_clickable((By.ID, 'r2s7f14fec' + idFecViajeRegreso + '11'))).click()
driver.save_screenshot(dirImagen + '/paso2-retorno.png')
WebDriverWait(driver, 23).until(ec.element_to_be_clickable((By.ID, 'continuar261612'))).click()
time.sleep(2)

driver.save_screenshot(dirImagen + '/paso2-total.png')
WebDriverWait(driver, 24).until(ec.element_to_be_clickable((By.ID, 'botonPasajerosAbt'))).click()

# paso 3
# pasajero 1
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, 'formPasajero1-nomPasajero'))).send_keys('JUNA DOMINGO')
WebDriverWait(driver, 11).until(ec.element_to_be_clickable((By.ID, 'formPasajero1-apePasajero'))).send_keys('WONG CHUQUIZUTA')
Select(WebDriverWait(driver, 12).until(ec.element_to_be_clickable((By.ID, 'formPasajero1-idPais')))).select_by_visible_text('PERÚ')
WebDriverWait(driver, 14).until(ec.element_to_be_clickable((By.ID, 'formPasajero1-numDocumentoIdentidad'))).send_keys('45233736')
driver.execute_script('document.getElementById("formPasajero1-fecNacimiento").removeAttribute("readonly")')
time.sleep(1)
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'formPasajero1-fecNacimiento'))).send_keys('11/07/1988')

# pasajero 2
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, 'formPasajero2-nomPasajero'))).send_keys('ANDRY')
WebDriverWait(driver, 11).until(ec.element_to_be_clickable((By.ID, 'formPasajero2-apePasajero'))).send_keys('MIRANDA SAAVEDRA')
Select(WebDriverWait(driver, 12).until(ec.element_to_be_clickable((By.ID, 'formPasajero2-idPais')))).select_by_visible_text('PERÚ')
WebDriverWait(driver, 14).until(ec.element_to_be_clickable((By.ID, 'formPasajero2-numDocumentoIdentidad'))).send_keys('46289926')
driver.execute_script('document.getElementById("formPasajero2-fecNacimiento").removeAttribute("readonly")')
time.sleep(1)
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'formPasajero2-fecNacimiento'))).send_keys('27/08/1988')
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'formPasajero2-idGenero-2'))).click()

driver.save_screenshot(dirImagen + '/paso3.png')
# Datos de contacto
Select(WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'codLadaPais')))).select_by_visible_text('PERÚ +51')
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'numTelefono'))).send_keys('959538652')

time.sleep(1)
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'btnFormularioPasajero'))).click()

# paso 4
driver.execute_script("window.open('');")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://zonasegura.incarail.app/pago/forma/idVista/5")

driver.save_screenshot(dirImagen + '/paso4-1-resumen-compra.png')
time.sleep(1)

driver.execute_script("window.scrollTo(0, 800)")
time.sleep(1)
driver.save_screenshot(dirImagen + '/paso4-2-importe-total.png')

WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'idTarjetaCredito-0'))).click()
Select(WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'listaPax')))).select_by_value('0')
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'desEmail'))).send_keys('jwong@incarail.com')
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'confdesEmail'))).send_keys('jwong@incarail.com')
time.sleep(1)
driver.save_screenshot(dirImagen + '/paso4-3-pagador.png')
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'botonPagar'))).click()

# paso 4 pasarela de pago
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, 'numTarjetaCreditoWp'))).send_keys('4444333322221111')
Select(WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'selectMesWp')))).select_by_value('01')
Select(WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'selectAnoWp')))).select_by_value('2025')
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, 'numCVCWp'))).send_keys('111')
driver.save_screenshot(dirImagen + '/paso4-4-pasarela-pago.png')

time.sleep(1)
WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.ID, 'btnContinuar'))).click()

# mensaje de compra y voucher
time.sleep(15)
el = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, 'body')))
el.screenshot(dirImagen + '/paso5.png')

idCarrito = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/div[1]/div/div/p[2]/strong")
idCarrito = idCarrito.text

os.rename(nomDirectorio, idCarrito)

time.sleep(30)

driver.close()