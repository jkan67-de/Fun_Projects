from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller as chromedriver

#all variables are defined in Info
from Info import *

path = chromedriver.install()
driver = webdriver.Chrome(path)

driver.get(website)
booked = False

while not booked:
    
    driver.refresh()
    sleep(4)
    amts=[]
    
    # get times
    for i in range(2,14,2):
        amts.append(driver.find_element("xpath",f'//*[@id="nav_menu2"]/li['+str(i)+']/a'))
    
    for amt in amts:
        month=int(amt.text[6:8])
        day= int(amt.text[3:5])

        cond1= (month==12 and (day==22 or (day>=28 and day<=31)))
        cond2= month==1 and (day!=2 and day<=18)
    
        if cond1 or cond2:
          amt.click()
          driver.find_element("id",'nachname').send_keys(lname)
          driver.find_element("id",'vorname').send_keys(fname)
          driver.find_element("id",'email').send_keys(email)
          driver.find_element("id",'email2').send_keys(email)
          driver.find_element("id",'mobilnummer').send_keys(number)
          sleep(0.5)
          driver.find_element("name",'submit').click()
          sleep(20)
          booked = True
          break

    sleep(30)
