from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class You():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play(self, query):
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        try:
            # Wait until the first video in the search results is clickable
            first_video = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="thumbnail-container"]'))
            )
            first_video.click()

            # Wait for the video player to be ready
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'video'))
            )

            # Keep the script running until the user closes the browser
            print("Video is playing. Close the browser window to stop.")
            while True:
                if not self.driver.window_handles:
                    break
        except Exception as e:
            print(f"An error occurred: {e}")


#auto = You()
#auto.play("ram")










