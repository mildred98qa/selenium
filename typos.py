import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Typos(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Typos").click()

    def test_find_typo(self):
        driver = self.driver
        correct_text = "Sometimes you'll see a typo, other times you won't."
        tries = 1

        while True:
            text_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)').text
            if text_to_check == correct_text:
                break
            driver.refresh()
            tries += 1

        print(f'It took {tries} tries to find the correct text.')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
