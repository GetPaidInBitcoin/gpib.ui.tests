import unittest
from webdriver import Driver
from values import strings
from page_objects.reset_password_screen import ResetPasswordScreen


class TestResetPassword(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url+strings.reset_password_url)

    def test_reset_password_screen_components(self):
        reset_screen = ResetPasswordScreen(self.driver)
        reset_screen.validate_form_is_present()
        reset_screen.validate_email_input()
        reset_screen.validate_email_link_button()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
