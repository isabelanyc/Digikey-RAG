# Digikey-RAG
_Under Development_

## Overview
The Digikey RAG project interacts with the Digikey API to search for electronic components, retrieve datasheets, and manage electronic components.

## RAG Overview
<p align="center">
  <img src="./img/rag.png"  width="850" height="300">
</p>
Diagram taken from [LlamaIndex webinar](https://www.youtube.com/watch?v=njzB6fm0U8g&t=904s)

## Features
- **Search Components**: Search for specific parts using the Digikey API (`test_api.py`).
- **Retrieve Datasheets**: Download datasheets for various components (`get_datasheets.py`).
- **Indexing**: Load and index PDFs for efficient search (`indexing.py`).
- **Querying**: Placeholder for future querying functionality (`querying.py`).
- **Demo**: A comment hinting at a potential future feature (`demo.py`).

## Installation
1. Install the required packages listed in `requirements.txt`.
2. Set up environment variables for Digikey API credentials.

## Usage
- **Testing API**: Run `test_api.py` to test the Digikey API.
- **Get Datasheets**: Run `get_datasheets.py` to download datasheets.
- **Indexing**: Run `indexing.py` to load and index PDFs.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).
