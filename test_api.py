import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use the loaded environment variables
CACHE_DIR = Path(os.getenv('DIGIKEY_STORAGE_PATH'))

# Set the other environment variables (no need to use os.environ)
DIGIKEY_CLIENT_ID = os.getenv('DIGIKEY_CLIENT_ID')
DIGIKEY_CLIENT_SECRET = os.getenv('DIGIKEY_CLIENT_SECRET')
DIGIKEY_CLIENT_SANDBOX = os.getenv('DIGIKEY_CLIENT_SANDBOX')

import digikey
from digikey.v3.productinformation import KeywordSearchRequest
from digikey.v3.batchproductdetails import BatchProductDetailsRequest

# Query product number
dkpn = '296-6501-1-ND'
part = digikey.product_details(dkpn)

# Search for parts
search_request = KeywordSearchRequest(keywords='CRCW080510K0FKEA', record_count=10)
result = digikey.keyword_search(body=search_request)

# Only if BatchProductDetails endpoint is explicitly enabled
# Search for Batch of Parts/Product
mpn_list = ["0ZCK0050FF2E", "LR1F1K0"] #Length upto 50
batch_request = BatchProductDetailsRequest(products=mpn_list)
part_results = digikey.batch_product_details(body=batch_request)