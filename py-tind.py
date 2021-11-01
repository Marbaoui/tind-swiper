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


def RunFrontApp():
    global Instance
    global wait
    Instance.get(url)
    time.sleep(2)

    input('press any key to run the script')
    # Locate like btn and click on it
    locate_like_btn = Instance.find_elements(By.XPATH, '//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)"]/button')
    print (len(locate_like_btn))

    for btn in locate_like_btn:
        print(btn.text)

        while(1):
            randomint = randint(2,6)
            time.sleep(randomint)
            btn.send_keys(Keys.ENTER)


    


Initialize()
RunFrontApp()