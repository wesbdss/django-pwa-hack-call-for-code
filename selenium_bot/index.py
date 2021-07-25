from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time

driver = None
options = Options()
options.headless = False
driver = webdriver.Firefox(options=options,executable_path=GeckoDriverManager().install())
driver.get('https://br.investing.com/commodities/carbon-emissions-streaming-chart')
time.sleep(2)
value = driver.find_element_by_id("last_last").text
variancia = driver.find_element_by_class_name('pid-8848-pc').text
types = [x.text for x in driver.find_elements_by_class_name("elp")]
response = {
    "value":value,
    "variancia":variancia,
    "unidade":types[2]
}
driver.close()