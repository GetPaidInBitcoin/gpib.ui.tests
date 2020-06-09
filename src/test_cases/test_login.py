import unittest
from webdriver import Driver
from values import strings
from page_objects import LoginScreen

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_login_screen_components(self):
        pass
    
    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()