import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

class DynamicElement(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()

    def test_gallery_element_appears(self):
        driver = self.driver
        intentos = 1
        max_intentos = 10

        elements = driver.find_elements(By.TAG_NAME, 'li')

        while len(elements) < 5 and intentos <= max_intentos:
            print(f'Intento {intentos}: {len(elements)} elementos visibles.')
            driver.refresh()
            sleep(1)
            elements = driver.find_elements(By.TAG_NAME, 'li')
            intentos += 1

        print(f'Total intentos: {intentos}')

        # Validar que al menos en algún intento apareció Gallery (5 elementos)
        self.assertEqual(len(elements), 5, 'No se encontró el quinto elemento "Gallery" tras varios intentos.')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
