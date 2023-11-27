# Crypto and Precious Metal Price Tracker

This Django website provides real-time(every 23 minutes) updates on cryptocurrency prices, precious metal prices, and the latest cryptocurrency news. It utilizes external APIs to fetch current data and presents it in a user-friendly interface.

## Features

- **Live Crypto Prices:** Displays the latest prices of various cryptocurrencies.
- **Precious Metal Prices:** Shows the current rates of precious metals such as gold, silver, platinum, etc.
- **Crypto News:** Fetches and displays the latest news related to cryptocurrencies.

## Setup and Installation

### Docker Setup

1. Ensure you have Docker installed on your machine.
2. Build the Docker image using the provided Dockerfile:

   ```bash
   docker build -t crypto-website .
   ```
   
1. Run the Docker container:

```bash
   docker run -p 8000:8000 crypto-website
```

2. Access the website in your browser at http://localhost:8000.

Dependencies

•	Python 3.9
•	Django
•	External APIs for crypto and precious metal prices (configured in the Django app)

Configuration

1.	Clone this repository:
```bash

git clone <repository_url> 
```

2.	Navigate to the project directory:
```bash

cd crypto-website
```
3.	Install required Python packages:

```bash
pip install -r requirements.txt
```

4.	Set up API keys for fetching cryptocurrency and precious metal prices. Add these keys in a .env file:
plaintextCopy code
CRYPTO_API_KEY=your_crypto_api_key_here METAL_API_KEY=your_precious_metal_api_key_here

5.	Run the Django server:

```bash
python manage.py runserver 
```

6.	Access the website in your browser at http://localhost:8000.
Folder Structure

•	/app: Django application files.

•	/static: Static files (CSS, JavaScript, etc.).

•	/templates: HTML templates for the website


