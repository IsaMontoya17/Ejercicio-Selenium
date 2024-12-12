from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# configuración del servicio de ChromeDriver
service = Service("driver/chromedriver.exe")

# Inicializar del navegador Chrome
bot = webdriver.Chrome(service=service)

# Maximizar la ventana del navegador
bot.maximize_window()
time.sleep(2)

# Navegar a la pagina de viajes exito
bot.get("https://www.viajesexito.com/")
time.sleep(1)

#seleccionar el boton vuelo-hotel
vuelo_hotel = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]/a/span')
vuelo_hotel.click()
time.sleep(5)

# se crea una instancia de WebDriverWait para manejar elementos dinamicos
wait = WebDriverWait(bot, 10)

# esperar a que se cargue el iframe que contiene el anuncio
iframe = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/iframe')))

# se cambia el contexto al iframe para interactuar con el contenido interno
bot.switch_to.frame(iframe)

# esperar a que se le pueda hacer click al anuncio y cerrarlo
anuncio = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]')))
anuncio.click()

# salir del iframe
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
time.sleep(2)

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

#realizar la busqueda
buscar = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a')
buscar.click()
time.sleep(18)

# estas lineas son para dirigirnos a la nueva pagina
handles = bot.window_handles
bot.switch_to.window(handles[-1])

# espera a que el contenedor con id divAirResults este presente
wait = WebDriverWait(bot, 15)
contenedor_resultados = wait.until(EC.presence_of_element_located((By.ID, 'divAirResults')))

# busca todas las cards div con clase row column dentro del contenedor
tarjetas = contenedor_resultados.find_elements(By.XPATH, './div[contains(@class, "row column")]')


for i, tarjeta in enumerate(tarjetas, 1):
    try:
        # busca todos los span con clase currencyText dentro de la tarjeta
        precios = tarjeta.find_elements(By.XPATH, './/span[contains(@class, "currencyText")]')
        
        # accede al segundo span con esa clase, ya que anteiormente hay otro con ese mismo nombre
        if len(precios) > 1:  
            print(f"Precio {i}: {precios[1].text}")
        else:
            print(f"Precio {i}: No hay un segundo precio en esta tarjeta")
    except Exception as e:
        print(f"Error en tarjeta {i}: {e}")


# ir a opciones avanzadas
opciones_avanzadas = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
opciones_avanzadas.click()
time.sleep(2)

#seleccionamos el input para escribir la aerolinea
aerolinea = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
aerolinea.click()
time.sleep(2)
aerolinea.send_keys("United")
time.sleep(2)
aerolinea.send_keys(Keys.ENTER)

#realizamos la busqueda otra vexz
buscar = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
buscar.click()
time.sleep(12)

# ir a contactanos para ir a wpp
contactanos = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p[1]/a')
contactanos.click()
time.sleep(2)

# Cerrar la ventana del navegador
bot.close()