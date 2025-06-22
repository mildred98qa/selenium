import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service  # <-- Importar esto

class DynamicControls(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')  # <-- Ruta al ejecutable
        self.driver = webdriver.Chrome(service=service)  # <-- Usar `service=service`
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver

        # Paso 1: click en el checkbox
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
        checkbox.click()

        # Paso 2: click en botón remove
        remove_add_button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
        remove_add_button.click()

        # Esperar que desaparezca el checkbox
        WebDriverWait(driver, 15).until(
            EC.invisibility_of_element_located((By.ID, "checkbox"))
        )

        # Paso 3: volver a agregar el checkbox
        remove_add_button.click()

        # Esperar a que reaparezca el checkbox
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "checkbox"))
        )

        # Paso 4: habilitar input
        enable_disable_button = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
        enable_disable_button.click()

        # Esperar a que se habilite el input
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > input"))
        )

        text_area = driver.find_element(By.CSS_SELECTOR, "#input-example > input")
        text_area.send_keys('Platzi')

        # Paso 5: deshabilitar input otra vez
        enable_disable_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
