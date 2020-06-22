#!/bin/bash
# Create a virtual env, so system upgrades don't break the test suite
python3 -m ./venv
source ./venv/bin/activate

# Install dependencies
pip3 install selenium pytest

#Need to work on this pip3 install python-dotenv
