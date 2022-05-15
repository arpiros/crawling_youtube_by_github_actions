import os
import time
from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from discord_webhook import DiscordWebhook

WEBHOOK_URL = os.getenv('DISCORD_KIRINUKI_WEBHOOK_URL')
YOUTUBE_URL = os.getenv('YOUTUBE_URL')

get_driver = GetChromeDriver()
get_driver.install()

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

driver = driver_init()
driver.get(YOUTUBE_URL)

driver.implicitly_wait(10)

box_list = driver.find_elements(by=By.CSS_SELECTOR, value="#contents > ytd-video-renderer")
for box in box_list:
    title = box.find_element(by=By.CSS_SELECTOR, value='#video-title')
    link = title.get_attribute("href")
    webhook = DiscordWebhook(url=WEBHOOK_URL, content=link)
    response = webhook.execute()

driver.quit()
