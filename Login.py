from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(ChromeDriverManager().install())
class mouseHover:
    def mouse(self):
        driver.get('https://demo.actitime.com/login.do')

mH = mouseHover()
mH.mouse()
