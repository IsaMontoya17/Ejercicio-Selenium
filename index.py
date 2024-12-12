from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ChromeDriver service configuration
service = Service("driver/chromedriver.exe")

# Initialize Chrome browser
bot = webdriver.Chrome(service=service)

# Maximize browser window
bot.maximize_window()
time.sleep(2)

# Navigate to the Exito travel page
bot.get("https://www.viajesexito.com/")
time.sleep(1)

# Select the flight-hotel button
flight_hotel = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]/a/span')
flight_hotel.click()
time.sleep(5)

# Create a WebDriverWait instance to handle dynamic elements
wait = WebDriverWait(bot, 10)

# Wait for the iframe containing the ad to load
iframe = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/iframe')))

# Switch context to the iframe to interact with its content
bot.switch_to.frame(iframe)

# Wait until the ad can be clicked and close it
ad = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]')))
ad.click()

# Exit the iframe
bot.switch_to.default_content()

# Set flight origin to MDE
origin = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
origin.click()
time.sleep(1)
origin = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
origin.send_keys("Jose Maria Cordova")
time.sleep(1)
origin.send_keys(Keys.ENTER)

# Set destination to Cancun
destination = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
destination.click()
time.sleep(1)
destination = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
destination.send_keys("Cancún, Quintana Roo (CUN-")
time.sleep(1)
wait = WebDriverWait(bot, 10)
destination_option = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li/div/div[2]/p[2]')))
destination_option.click()
time.sleep(1)

# Set flight dates
departure_date = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
departure_date.click()
time.sleep(1)
selected_departure_date = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]/div[2]/div[1]')
selected_departure_date.click()
return_date = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[3]/div[2]/div[2]/div[1]')
return_date.click()
accept_button = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/button[2]')
accept_button.click()
time.sleep(2)

# Select rooms
rooms = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p')
rooms.click()
time.sleep(2)

add_room = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
add_room.click()
time.sleep(2)
room_two =  bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/div/span[2]/button/span')
room_two.click()
room_two.click()
time.sleep(2)

apply = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
apply.click()
time.sleep(2)

# Perform the search
search = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a')
search.click()
time.sleep(18)

# These lines direct to the new page
handles = bot.window_handles
bot.switch_to.window(handles[-1])

# Wait for the container with ID divAirResults to be present
wait = WebDriverWait(bot, 15)
results_container = wait.until(EC.presence_of_element_located((By.ID, 'divAirResults')))

# Search for all cards div with row column class within the container
cards = results_container.find_elements(By.XPATH, './div[contains(@class, "row column")]')


for i, tarjeta in enumerate(cards, 1):
    try:
        # Search for all span elements with currencyText class within the card
        prices = tarjeta.find_elements(By.XPATH, './/span[contains(@class, "currencyText")]')
        
        # Access the second span with that class, as there is another one with the same name before
        if len(prices) > 1:  
            print(f"Price {i}: {prices[1].text}")
        else:
            print(f"Price {i}: No second price in this card")
    except Exception as e:
        print(f"Error in card {i}: {e}")


# Go to advanced options
advanced_options = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
advanced_options.click()
time.sleep(2)

# Select the input to write the airline
airline = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
airline.click()
time.sleep(2)
airline.send_keys("United")
time.sleep(2)
airline.send_keys(Keys.ENTER)

# Perform the search again
search = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
search.click()
time.sleep(12)

# Go to the contact us section to access WhatsApp
contact_us = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p[1]/a')
contact_us.click()
time.sleep(2)

# Close the browser window
bot.close()