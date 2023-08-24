import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
import digikey
import requests
from digikey.v3.productinformation import KeywordSearchRequest

def download_pdf(url, destination_path):
    try:
        response = requests.get(url, timeout=(5, 10))
        with open(destination_path, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to download {url}")
    except requests.exceptions.Timeout:
        print(f"Timed out while downloading {url}")


def ensure_pdf_extension(destination_path):
    # Check if the file exists
    if os.path.exists(destination_path):
        if not destination_path.lower().endswith('.pdf'):
            new_destination_path = destination_path + '.pdf'
            shutil.move(destination_path, new_destination_path)
            print(f"Renamed {destination_path} to {new_destination_path}")
            return new_destination_path
    else:
        print(f"File {destination_path} does not exist. Cannot rename.")
    return destination_path


def getDatasheetURLs(keywordSearchResult):
    numberOfproducts = len(keywordSearchResult._products)

    urls = []
    for i in range(numberOfproducts):
        urls.append(keywordSearchResult._products[i].primary_datasheet)
        digi_key_part_number = keywordSearchResult._products[i].digi_key_part_number
        print(f'Obtained datasheet for {digi_key_part_number}')
    return urls


def getDatasheets(datasheetUrls):
    for url in datasheetUrls:
        if url and url.startswith(('http://', 'https://')):
            destination_path = 'data/' + url.split('/')[-1]
            download_pdf(url, destination_path)
            destination_path = ensure_pdf_extension(destination_path)
        else:
            print(f"Skipping invalid URL: {url}")


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
        search_request = KeywordSearchRequest(keywords=keyword, record_count=50)
        keywordSearchResult = digikey.keyword_search(body=search_request)

        # add to running list of datasheet urls
        keywordUrls = getDatasheetURLs(keywordSearchResult=keywordSearchResult)
        datasheetUrls = datasheetUrls + keywordUrls

    # Download the datasheets
    getDatasheets(datasheetUrls)
