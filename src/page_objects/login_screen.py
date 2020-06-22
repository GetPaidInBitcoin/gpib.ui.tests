import pytest as pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from values import strings


class LoginScreen:

    def __init__(self, driver):
        self.driver = driver
        self.form = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "loginForm")))
        self.email = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Email")))
        self.password = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Password")))
        self.resetPassword = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Reset password")))
        self.loginBtn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//form[1]/div[3]/button")))

    def validate_form_is_present(self):
        assert self.form.is_displayed()

    def validate_email_input(self):
        assert self.email.is_displayed()
        assert self.email.get_attribute("type") == "email"

    def validate_password_input(self):
        assert self.password.is_displayed()
        assert self.password.get_attribute("type") == "password"

    def validate_reset_password(self):
        assert self.resetPassword.is_displayed()
        assert self.resetPassword.get_attribute(
            "href") == strings.base_url+strings.reset_password_url

    def validate_login_button(self):
        assert self.loginBtn.is_displayed()
        self.email.send_keys(strings.test_user)
        self.password.send_keys(strings.test_password)
        self.loginBtn.send_keys(Keys.ENTER)
        assert WebDriverWait(self.driver.instance, 10).until(
            EC.url_matches(strings.base_url+strings.dashboard_url))
