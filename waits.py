import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

class ExplicitWaitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        s = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=s)

        driver = cls.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        driver.implicitly_wait(3)
    
    def test_account_link(self):
        # Esperar a que el select tenga 3 opciones
        WebDriverWait(self.driver, 10).until(
            lambda d: len(Select(d.find_element(By.ID, 'select-language')).options) == 3
        )
        
        account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT'))
        )
        account.click()

    def test_create_new_customer(self):
        account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT'))
        )
        account.click()
        
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'My Account'))
        )
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT'))
        )
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains('Create New Customer Account')
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
