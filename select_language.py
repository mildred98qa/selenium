import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class LanguageOptions(unittest.TestCase):
    def setUp(self):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_select_language(self):
        # Opciones visibles esperadas en el dropdown
        exposed_options = ['English', 'French', 'German']
        active_options = []

        # Obtener el elemento select correctamente
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))

        # Verificar que haya 3 opciones
        self.assertEqual(3, len(select_language.options))

        # Guardar los textos de cada opción
        for option in select_language.options:
            active_options.append(option.text)

        # Verificar que las opciones coinciden
        self.assertListEqual(exposed_options, active_options)

        # Verificar que 'English' es la opción seleccionada por defecto
        self.assertEqual('English', select_language.first_selected_option.text)

        # Seleccionar 'German'
        select_language.select_by_visible_text('German')

        # Verificar que la URL cambió correctamente
        self.assertIn('store=german', self.driver.current_url)

        # Volver a seleccionar 'English' por índice (opcional)
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
