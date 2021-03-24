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

if os.getenv('PSQL_URI') is None:
    print(
        """
        WARNING no database connection found.
        Beaker37 needs MovieLense data to be store in an SQL-database.
        You need to tell Beaker37 how to access such a database.
        Provide the connection string (see sqlalchemy dokumentation)
        as the environtment variable PSQL_URI
        You can use environment file to setup this variable.
        The name of this file is 'beaker37.env' in the local directory
        or the file where the environment variable BEAKER37ENV points to
        """
    )