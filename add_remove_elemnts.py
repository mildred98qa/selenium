import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

class AddRemoveElementsReto(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver
        elements_to_add = 3
        elements_to_remove = 2

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        for _ in range(elements_to_add):
            add_button.click()

        delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')

        self.assertGreaterEqual(len(delete_buttons), elements_to_remove, 
            "No puedes eliminar más elementos de los que agregaste")

        for i in range(elements_to_remove):
            delete_buttons[i].click()

        remaining_elements = driver.find_elements(By.CLASS_NAME, 'added-manually')
        total_remaining = len(remaining_elements)

        print(f"Agregaste {elements_to_add}, eliminaste {elements_to_remove}, quedan {total_remaining}.")

        self.assertEqual(total_remaining, elements_to_add - elements_to_remove)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
