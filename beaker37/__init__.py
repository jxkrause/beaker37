"""
Beaker37 is a Python library for recommending for movies.
project for Spiced Academy / Discrete Dill
"""

import os
from dotenv import load_dotenv

library_path = os.path.dirname(__file__)

BEAKER37ENV = os.getenv('BEAKER37ENV')
if BEAKER37ENV is None:
    load_dotenv('beaker37.env')
else:
    load_dotenv(BEAKER37ENV)
