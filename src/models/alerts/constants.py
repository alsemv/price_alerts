import os

# URL = "https://api.mailgun.net/v3/sandbox7c385542316d4401a85306288ddef4b5.mailgun.org"
# API_KEY = "key-820002984cfef4521a91dfcaf8e34a17"
# FROM = "Mailgun Sandbox <postmaster@sandbox7c385542316d4401a85306288ddef4b5.mailgun.org>"


URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"
