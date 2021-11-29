import time
import winsound
from colorama import Fore
from colorama import Style
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH  = "H:\chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get("https://www.cineplex.com/Movie/spiderman-no-way-home")

time.sleep(3)

frequency = 1500
duration = 500
ticketsAvailable = False

while not ticketsAvailable:
    try:
        browser.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[7]/div[1]/movie-showtimes-table')
        print("Spider-Man: No Way Home tickets now on sale!")
        winsound.Beep(frequency, duration)
    except:
        print(f'{Fore.RED}No Spidey tickets yet :(')
        winsound.Beep(500, 100)

    # time.sleep(3)
    browser.refresh()