import os
from pathlib import Path
from dotenv import load_dotenv
import digikey
from digikey.v3.productinformation import KeywordSearchRequest

# Load environment variables from .env file
load_dotenv()

# Get environment variables
CLIENT_ID = os.getenv('DIGIKEY_CLIENT_ID')
CLIENT_SECRET = os.getenv('DIGIKEY_CLIENT_SECRET')
CLIENT_SANDBOX = os.getenv('DIGIKEY_CLIENT_SANDBOX')
CACHE_DIR = Path(os.getenv('DIGIKEY_STORAGE_PATH'))

# Set environment variables
os.environ['DIGIKEY_CLIENT_ID'] = CLIENT_ID
os.environ['DIGIKEY_CLIENT_SECRET'] = CLIENT_SECRET
os.environ['DIGIKEY_CLIENT_SANDBOX'] = CLIENT_SANDBOX
os.environ['DIGIKEY_STORAGE_PATH'] = str(CACHE_DIR)

# Query product number
dkpn = '296-6501-1-ND'
part = digikey.product_details(dkpn)

# Search for parts
search_request = KeywordSearchRequest(keywords='CRCW080510K0FKEA', record_count=10)
result = digikey.keyword_search(body=search_request)
