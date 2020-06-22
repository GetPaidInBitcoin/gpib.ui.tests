import unittest
from webdriver import Driver
from values import strings
from page_objects.login_screen import LoginScreen


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url+strings.login_url)

    def test_login_screen_components(self):
        login_screen = LoginScreen(self.driver)
        login_screen.validate_form_is_present()
        login_screen.validate_email_input()
        login_screen.validate_password_input()
        login_screen.validate_login_button()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
