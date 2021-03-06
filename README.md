# gpib.ui.tests

Selenium tests for www.getpaidinbitcoin.com.au

## Tutorial and example on this structure

https://github.com/mikearias3/QABoy/tree/master/QABoyAutomation-Final/QABoyAutomationFramework
https://qaboy.com/2018/01/15/automated-framework-using-selenium-with-python/
https://www.selenium.dev/documentation/en/guidelines_and_recommendations/page_object_models/

### Todo

- add pytest to setup
- add python-dotenv for env vars?

## Setup

### Install the web driver

Drivers are available for chrome, firefox, edge, and safari.
To install the chrome driver on OSX and Linux (when brew is installed):

```bash
brew cask install chromedriver
```

Alternatively, the driver can be downloaded from the links available here: [Selenium web drivers](https://selenium-python.readthedocs.io/installation.html) and added manually:

```bash
sudo cp chromedriver /usr/bin/chromedriver
```

### Setup python and dependancies

NB: Needs a better package management solution

```bash
git clone git@github.com:GetPaidInBitcoin/gpib.ui.tests.git
cd gpib.ui.tests

# Create a virtual env, so system upgrades don't break the test suite
python3 -m ./venv

# Start the virtual env
source ./venv/bin/activate

# Install dependencies
pip3 install selenium pytest
```

## Usage

### Activate/Deactivate the virtual environment

To activate the virtual env so you can run the test suite:

```bash
source ./venv/bin/activate
```

When you're finished with the test suite:

```bash
deactivate
```

### Running the tests

#### Execute all tests

```bash
cd src
python3 -m pytest test_cases/
```

#### Execute Login screen tests

```bash
cd src
python3 -m pytest test_cases/test_login.py

```
