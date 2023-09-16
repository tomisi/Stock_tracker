# Stock Tracker

The Stock Tracker is a Python-based command-line application designed to track stock prices, set price alerts, and monitor alerts for specific stocks.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Features](#features)
  - [Tracking Stocks](#tracking-stocks)
  - [Setting Price Alerts](#setting-price-alerts)
  - [Checking Alerts](#checking-alerts)
- [Customization](#customization)
  - [Data Storage](#data-storage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The Stock Tracker project is organized into the following folders and files:

- `api/`: Contains functions for fetching stock data from an API.
- `alerts/`: Contains functions for setting, checking, and managing price alerts.
- `data/`: Contains functions for data storage and retrieval (e.g., saving and retrieving user alerts).
- `main.py`: The main script serving as the entry point for the application.
- `README.md`: Documentation file (this document).

## Setup

### Prerequisites

Before running the Stock Tracker application, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- An Alpha Vantage API key (replace `"YOUR_ALPHA_VANTAGE_API_KEY"` in the code with your actual API key).
  Main Menu
  
## Features

### Track Stock

- Fetch and display the current stock price for a specific symbol.

### Set Price Alert

- Set a price alert for a stock symbol, specifying a threshold price.

### Check Alerts

- Check for price alerts you've set. If any threshold is crossed, the application notifies you.

### Exit

- Exit the application.

## Customization

### Data Storage

- The `data_storage.py` script contains example functions for saving and retrieving alerts. You can customize this script to use your preferred data storage method, such as a file or a database.

## Contributing

Contributions to this project are welcome! You can fork the repository, make improvements, and create a pull request.
