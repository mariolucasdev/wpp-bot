from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas
import urllib
import time

# List Contacts
contacts = pandas.read_excel("contacts.xlsx")

# Browser Generate and Open
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://web.whatsapp.com/")
time.sleep(3)

# Function to Check WhatsApp Auth
def auth(browser):
    while len(browser.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)

# Function to Send Message
def send_message(browser):
    
    # =====================================================================================================
    # CHECK BUG FOR TEMP MESSAGES ACTIVES TO CHAT
    # =====================================================================================================

    # xpath_btn_hide_temp_messages = '//*[@id="app"]/div/div/div[5]/span/div/div/header/div/div[1]/div/span'
    # if(len(browser.find_elements(By.XPATH, xpath_btn_hide_temp_messages)) > 0):
    #     WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_btn_hide_temp_messages))).click()

    # Click in Button to Send Message
    xpath_btn_send_messages = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_btn_send_messages))).click()

# Check is Loggin
auth(browser=browser)

# Gerenate Link
def generate_link(i, contacts):
    name = contacts.loc[i, "Pessoa"]
    contact = contacts.loc[i, "Número"]
    message = urllib.parse.quote(f"Oi {name}! {mensagem}")
    return f"https://web.whatsapp.com/send?phone={contact}&text={message}"

# Send Mensages to Persons
for i, mensagem in enumerate(contacts['Mensagem']):
    browser.get(generate_link(i=i, contacts=contacts))
    auth(browser=browser)
    time.sleep(5)
    send_message(browser=browser)
    time.sleep(10)