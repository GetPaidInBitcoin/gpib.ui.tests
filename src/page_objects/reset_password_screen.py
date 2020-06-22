import pytest as pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from values import strings


class ResetPasswordScreen:

    def __init__(self, driver):
        self.driver = driver
        self.form = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//form[1]")))
        self.email = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Email")))
        self.resetBtn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//form[1]/div[3]/div[1]/input")))

    def validate_form_is_present(self):
        assert self.form.is_displayed()

    def validate_email_input(self):
        assert self.email.is_displayed()
        assert self.email.get_attribute("type") == "email"

    def validate_email_link_button(self):
        assert self.resetBtn.is_displayed()
        self.email.send_keys(strings.test_user)
        self.resetBtn.send_keys(Keys.ENTER)
        assert WebDriverWait(self.driver.instance, 10).until(
            EC.url_matches(strings.base_url+strings.reset_confirmation_url))
