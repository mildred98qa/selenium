import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class AssertionsTests(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
