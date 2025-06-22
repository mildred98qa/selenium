import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class HomePageTests(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID, "small-searchterms")
        self.assertTrue(search_field.is_displayed())

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(By.NAME, "q")
        self.assertTrue(search_field.is_displayed())

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element(By.CSS_SELECTOR, ".search-box-text.ui-autocomplete-input")
        self.assertTrue(search_field.is_displayed())

    def test_search_button_enabled(self):
        button = self.driver.find_element(By.CLASS_NAME, "button-1")
        self.assertTrue(button.is_displayed())
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
