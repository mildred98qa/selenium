import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Tables(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')  # Ejecuta sin abrir ventana
        options.add_argument('--disable-gpu')
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')  # Ajusta la ruta si es necesario
        self.driver = webdriver.Chrome(service=service, options=options)

    def tearDown(self):  # Corrección del nombre
        self.driver.quit()

    def test_sort_tables(self):
        driver = self.driver
        table_data = []

        try:
            driver.get('https://the-internet.herokuapp.com/')
            driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()

            # Obtener encabezados
            header_cells = driver.find_elements(By.CSS_SELECTOR, '#table1 thead tr th')
            headers = [cell.text.strip() for cell in header_cells]

            # Obtener filas del cuerpo
            rows = driver.find_elements(By.CSS_SELECTOR, '#table1 tbody tr')

            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                data = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
                table_data.append(data)

            # Mostrar resultado
            for row_data in table_data:
                print(row_data)

        except NoSuchElementException as ex:
            self.fail(f"Elemento no encontrado: {ex.msg}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
