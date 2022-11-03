import unittest
from selenium import webdriver
import pytest
import pytest_html

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver =webdriver.Chrome(executable_path="chromedriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10)

    def test1_hello_world(self):
        driver = self.driver
        driver.get("https://www.google.com")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
 unittest.main(verbosity=2)