from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_Info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org/")

        # Wait until the search input is present
        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]'))
        )
        search.click()
        search.send_keys(query)

        # Wait until the search button is present
        enter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="search-form"]/fieldset/button'))
        )
        enter.click()

        # Optionally, wait for some results to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mw-search-result-heading"]'))
        )
#inst = infow()
#inst.get_Info("hello")



