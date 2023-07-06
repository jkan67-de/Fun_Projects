from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller as chromedriver
from playsound import playsound
from Info import *

path = chromedriver.install()
driver = webdriver.Chrome(path)

driver.get(website)
dropped = False

while not dropped:
    
    driver.refresh()
    
    try:
        price = driver.find_element("xpath",f'/html/body/div[5]/div[5]/div[1]/div/div[1]/div[3]/div/div[1]/span[2]/span').text
        fprice = float(price[1:])
        
    except:
        fprice=100
    
    if fprice<5:
        dropped=True
        break

    sleep(3600)
    
while True:
    playsound(soundfile)
