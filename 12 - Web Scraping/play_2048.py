# Using selenium and stuff to play the game 2048
# Automate the Boring Stuff Chapter 12, page 516
# https://2048game.com/

import random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')


restartButton = browser.find_element_by_class_name('restart-button')
time.sleep(4)
browser.find_element_by_class_name('notice-close-button').click()

time.sleep(4)

gameGrid = browser.find_element_by_tag_name('body')

moves = {0: Keys.UP, 1: Keys.DOWN, 2: Keys.LEFT, 3: Keys.RIGHT}

for i in range(5):
    for x in range(1, 300):
        r = random.randint(0, 3)
        gameGrid.send_keys(moves[r])
        #time.sleep(.25)
    restartButton.click()

