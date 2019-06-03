import urllib
import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# params = urllib.parse.quote_plus(
#    "Driver={ODBC Driver 13 for SQL Server};Server=tcp:topicossoftware.database.windows.net,1433;Database=Software;Uid=softwareadmin@topicossoftware;Pwd=pass123*;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
SQLALCHEMY_DATABASE_URI = 'sqlite:///../../students.sqlite3'
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
