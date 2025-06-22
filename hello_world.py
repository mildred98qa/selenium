import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(r'C:\Users\USER\Desktop\selenium\chromedriver-win64\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)

    def test_hello_World(self):
        self.driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://es.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))
