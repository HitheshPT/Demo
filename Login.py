from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver_path = ChromeDriverManager().install()

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')



driver = webdriver.Chrome(executable_path=driver_path,  chrome_options=chrome_options)

class mouseHover:
    def mouse(self):
        driver.get('https://demo.actitime.com/login.do')

mH = mouseHover()
mH.mouse()

