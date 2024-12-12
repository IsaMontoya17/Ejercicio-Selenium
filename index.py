from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
time.sleep(2)

bot.get("https://www.viajesexito.com/")
time.sleep(1)

#seleccionar el boton vuelo-hotel
vuelo_hotel = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]/a/span')
vuelo_hotel.click()
time.sleep(5)

#cerrar anuncio
wait = WebDriverWait(bot, 10)


iframe = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/iframe')))
bot.switch_to.frame(iframe)
anuncio = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]')))
anuncio.click()
bot.switch_to.default_content()

#poner vuelo desde mde
origen = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
origen.click()
time.sleep(1)
origen = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
origen.send_keys("Jose Maria Cordova")
time.sleep(1)
origen.send_keys(Keys.ENTER)

#poner destio a cancun
destino = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
destino.click()
time.sleep(1)
destino = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
destino.send_keys("Cancún, Quintana Roo (CUN-")
time.sleep(1)
wait = WebDriverWait(bot, 10)
opcion_destino = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li/div/div[2]/p[2]')))
opcion_destino.click()
time.sleep(1)

#poner fechas de vuelos
fecha_salida = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
fecha_salida.click()
time.sleep(1)
fecha_salida_seleccionada = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]/div[2]/div[1]')
fecha_salida_seleccionada.click()
fecha_regreso = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[3]/div[2]/div[2]/div[1]')
fecha_regreso.click()
boton_aceptar = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/button[2]')
boton_aceptar.click()
time.sleep(5)

#seleccionar habitaciones
habitaciones = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p')
habitaciones.click()
time.sleep(2)

anadir_habitacion = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
anadir_habitacion.click()
time.sleep(2)
habitacion_dos =  bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/div/span[2]/button/span')
habitacion_dos.click()
habitacion_dos.click()
time.sleep(2)

aplicar = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
aplicar.click()
time.sleep(2)