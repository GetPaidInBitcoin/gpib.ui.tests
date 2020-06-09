from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## should not be able to resgister without a firstname
driver = webdriver.Chrome()
driver.get("https://portal.getpaidinbitcoin.com.au/account/register")
assert "Get Paid in Bitcoin - Register" in driver.title
elem = driver.find_element_by_id("Email")
elem.clear()
elem.send_keys("alice@bitcoinbrisbane.com.au")

elem = driver.find_element_by_id("Password")
elem.clear()
elem.send_keys("Test1234")

elem = driver.find_element_by_id("ConfirmPassword")
elem.clear()
elem.send_keys("Test1234")

elem = driver.find_element_by_id("Firstname")
elem.clear()
elem.send_keys("Alice")

elem = driver.find_element_by_id("Lastname")
elem.clear()
elem.send_keys("BB")

elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()