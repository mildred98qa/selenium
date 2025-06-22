import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Función para leer datos del archivo CSV
def get_data(file_name):
    rows = []
    with open(file_name, 'r', newline='', encoding='utf-8') as data_file:
        reader = csv.reader(data_file)
        next(reader, None)  # Omitir encabezado
        for row in reader:
            rows.append(row)
    return rows

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://demowebshop.tricentis.com/')

    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        expected_count = int(expected_count)
        products = driver.find_elements(By.XPATH, '//h2[@class="product-title"]/a')

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element(By.CLASS_NAME, 'no-result')
            self.assertEqual('No products were found that matched your criteria.', message.text)

        print(f'Searched for "{search_value}" - Expected: {expected_count}, Found: {len(products)}')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
