# Crypto and Precious Metal Price Tracker

This Django-based website offers real-time(every 23 minutes) updates on various financial data, including cryptocurrency prices, precious metal values, and the latest cryptocurrency news. It relies significantly on external APIs to fetch current data and delivers it through a user-friendly interface. One of the critical components powering this platform is the integration of the Coinmarketcap API. This API serves as a primary source for obtaining accurate and up-to-date cryptocurrency prices.


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
   docker run -e SECRET_KEY=abc -e DEBUG=true -p 8000:8000 crypto-website
```
### What is secret key:

In Django, the secret key is a cryptographic key used for securing and validating the integrity of sessions, CSRF tokens, and other security-related functionalities within the framework. It serves as a crucial security measure to encrypt and sign data, preventing tampering and unauthorized access to sensitive information. Keeping the secret key confidential is essential to ensure the overall security and integrity of a Django application.







2. Access the website in your browser at http://localhost:8000/coin_app/home/
   

### Python setup

#### Dependencies
•	Python 3.9
•	Django
•	External APIs for crypto and precious metal prices (configured in the Django app)

#### Configuration

1.	Clone this repository:
```bash

git clone <repository_url> 
```

2.	Navigate to the project directory:
```bash

cd django-crypto-api
```
and then

```bash

cd clone
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

6.	Access the website in your browser at http://localhost:8000/coin_app/home/
   
Folder Structure

•	/app: Django application files.

•	/static: Static files (CSS, JavaScript, etc.).

•	/templates: HTML templates for the website


