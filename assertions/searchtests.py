import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_search_simple_computer(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('simple computer')
        search_field.submit()

        # Buscar productos en los resultados
        products = driver.find_elements(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div[1]/a/img')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
