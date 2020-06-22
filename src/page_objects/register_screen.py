import pytest as pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from values import strings


class RegisterScreen:

    def __init__(self, driver):
        self.driver = driver
        self.form = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//form[1]")))
        self.email = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Email")))
        self.password = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Password")))
        self.confirmPassword = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
        self.firstName = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Firstname")))
        self.lastName = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Lastname")))
        self.referredBy = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "ReferredBy")))
        self.btcAddress = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "BitcoinAddress")))
        self.registerBtn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Join")))
        self.facebookRegister = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.ID, "Facebook")))

    def validate_form_is_present(self):
        assert self.form.is_displayed()
        assert self.email.is_displayed()
        # assert self.email.get_attribute("type") == "email"
        assert self.password.is_displayed()
        assert self.password.get_attribute("type") == "password"
        assert self.confirmPassword.is_displayed()
        assert self.confirmPassword.get_attribute("type") == "password"
        assert self.firstName.is_displayed()
        assert self.lastName.is_displayed()
        assert self.referredBy.is_displayed()
        assert self.btcAddress.is_displayed()
        assert self.registerBtn.is_displayed()
        assert self.facebookRegister.is_displayed()

    def validate_register_new_user(self):
        self.email.send_keys(str(random.randint(100, 1000)) +
                             strings.test_register_user)
        self.password.send_keys(strings.test_password)
        self.confirmPassword.send_keys(strings.test_password)
        self.firstName.send_keys(strings.test_firstname)
        self.lastName.send_keys(strings.test_lastname)
        self.registerBtn.send_keys(Keys.ENTER)
        assert WebDriverWait(self.driver.instance, 10).until(
            EC.url_matches(strings.base_url+strings.dashboard_url))
