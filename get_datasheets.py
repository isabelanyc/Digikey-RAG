import os
from pathlib import Path
from dotenv import load_dotenv
import digikey
import requests
from digikey.v3.productinformation import KeywordSearchRequest

def download_pdf(url, destination_path):
    response = requests.get(url)
    with open(destination_path, 'wb') as file:
        file.write(response.content)

def getDatasheetURLs(keywordSearchResult):
    numberOfproducts = len(keywordSearchResult._products)

    urls = []
    for i in range(numberOfproducts):
        urls.append(keywordSearchResult._products[i].primary_datasheet)
    return urls

def getDatasheets(datasheetUrls):
    # Destination folder
    destination_folder = 'data'

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Download and save each PDF
    for url in datasheetUrls:
        # Determine the destination path
        filename = url.split('/')[-1]
        destination_path = os.path.join(destination_folder, filename)

        # Download and save the PDF
        download_pdf(url, destination_path)

        print(f'Downloaded {filename} from {url}')

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Get environment variables
    CLIENT_ID = os.getenv('DIGIKEY_CLIENT_ID')
    CLIENT_SECRET = os.getenv('DIGIKEY_CLIENT_SECRET')
    CLIENT_SANDBOX = os.getenv('DIGIKEY_CLIENT_SANDBOX')
    CACHE_DIR = Path(os.getenv('DIGIKEY_STORAGE_PATH'))

    # Define list of keywords
    keywords = ["resistor", "capacitor", "RF Amplifier"]
    
    datasheetUrls = []
    # Do a keyword search and grab all the urls for the datasheets
    for keyword in keywords:
        search_request = KeywordSearchRequest(keywords=keyword, record_count=30)
        keywordSearchResult = digikey.keyword_search(body=search_request)

        # add to running list of datasheet urls
        keywordUrls = getDatasheetURLs(keywordSearchResult=keywordSearchResult)
        datasheetUrls = datasheetUrls + keywordUrls

    # Download the datasheets
    getDatasheets(datasheetUrls)
