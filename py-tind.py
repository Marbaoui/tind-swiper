from selenium import webdriver
# import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import randint

import time

Instance = None
wait = None

url = "https://tinder.com/app/recs"

def Initialize():
    global Instance
    global wait
    Instance = webdriver.Chrome("./chromedriver.exe")
    wait = WebDriverWait(Instance , 10)
    time.sleep(1)
    Instance.get(url)
    input('press any key to run the script')

count = 0
like_number = 0

def RunFrontApp():
    global Instance
    global wait
    global count
    global like_number
    time.sleep(2)

    # Locate like btn and click on it
    
    while(1):
        locate_like_btn = Instance.find_elements(By.XPATH, '//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)"]/button')
        print (like_number)
        btn = locate_like_btn[0]
        randomint = randint(2,5)
        time.sleep(randomint)
        try:
            btn.send_keys(Keys.ENTER)
            like_number = like_number + 1
        except:
            count = count +1
            input("press any keys to reload browser")
            Instance.get(url)
            input("press any keys to start")
            time.sleep(2)
                

