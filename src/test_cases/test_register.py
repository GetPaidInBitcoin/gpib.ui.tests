import unittest
from webdriver import Driver
from values import strings
from page_objects.register_screen import RegisterScreen


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url+strings.register_url)

    def test_register_screen_components(self):
        register_screen = RegisterScreen(self.driver)
        register_screen.validate_form_is_present()
        register_screen.validate_register_new_user()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
