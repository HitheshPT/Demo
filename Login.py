  GNU nano 4.8                                                                      Login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opts)

class mouseHover:
    def mouse(self):
        driver.get('https://demo.actitime.com/login.do')

mH = mouseHover()
mH.mouse()

