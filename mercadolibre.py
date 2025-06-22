import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Typos(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get('https://www.mercadolibre.com')

    def test_search_ps4(self):
        driver = self.driver

        # Esperar que el botón de Colombia esté visible y hacer clic
        country = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='colombia']"))
        )
        country.click()

        # Esperar a que cargue la caja de búsqueda
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "as_word"))
        )
        search_field.clear()
        search_field.send_keys("playstation 4")
        search_field.submit()

        sleep(3)
        # Filtrar por ubicación: Bogotá
        try:
            location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')
            driver.execute_script("arguments[0].click();", location)
            sleep(3)
        except:
            print("No se encontró la opción de ubicación Bogotá D.C.")

        # Filtrar por condición: Nuevo
        try:
            condition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
            driver.execute_script("arguments[0].click();", condition)
            sleep(3)
        except:
            print("No se encontró la opción de condición Nuevo.")

        # Ordenar por Mayor precio
        try:
            order_menu = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Ordenar']")
            order_menu.click()
            value = driver.find_element(By.PARTIAL_LINK_TEXT, 'Mayor precio')
            driver.execute_script("arguments[0].click();", value)
            sleep(3)
        except:
            print("No se pudo cambiar el orden por Mayor precio.")

        # Capturar los primeros 5 artículos
        articles = []
        prices = []

        for i in range(1, 6):
            try:
                article_name = driver.find_element(By.XPATH, f'(//h2[@class="ui-search-item__title"])[{i}]').text
                article_price = driver.find_element(By.XPATH, f'(//span[@class="andes-money-amount__fraction"])[{i}]').text
                articles.append(article_name)
                prices.append(article_price)
            except:
                print(f"No se pudo capturar el artículo #{i}")

        print("ARTÍCULOS:", articles)
        print("PRECIOS:", prices)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
