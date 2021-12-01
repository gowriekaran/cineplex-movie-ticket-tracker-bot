import time
import winsound
import variables
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(variables.CHROME_DRIVER_PATH)

browser.get(variables.MOVIE_URL)

time.sleep(variables.INITIAL_LOAD_DELAY)

isTicketsAvailable = False

while not isTicketsAvailable:
    try:
        browser.find_element(By.XPATH, variables.TARGET_ELEMENT_XPATH)
        print(variables.MOVIE_TICKETS_ON_SALE_MESSAGE)
        winsound.Beep(variables.POSITIVE_SOUND_NOTIFICATION_FREQUENCY, variables.POSITIVE_SOUND_NOTIFICATION_DURATION)
        isTicketsAvailable = True
    except:
        print(f'{Fore.RED}{variables.MOVIE_TICKETS_NOT_ON_SALE_MESSAGE}')
        winsound.Beep(variables.NEGATIVE_SOUND_NOTIFICATION_FREQUENCY, variables.NEGATIVE_SOUND_NOTIFICATION_DURATION)

    time.sleep(variables.LOOP_REPEAT_DELAY)
    browser.refresh()
browser.close()