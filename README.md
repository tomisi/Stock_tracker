Stock Tracker

Introduction
The Stock Tracker is a Python-based command-line application designed to track stock prices, set price alerts, and monitor alerts for specific stocks. This documentation provides an overview of the project's structure, functionality, and usage.

Table of Contents
Project Structure
Setup
Prerequisites
Installation
Usage
Running the Application
Main Menu
Features
Tracking Stocks
Setting Price Alerts
Checking Alerts
Customization
Data Storage
Contributing
License
Project Structure
The Stock Tracker project is organized into the following folders and files:

api/: Contains functions for fetching stock data from an API.
alerts/: Contains functions for setting, checking, and managing price alerts.
data/: Contains functions for data storage and retrieval (e.g., saving and retrieving user alerts).
main.py: The main script serving as the entry point for the application.
README.md: Documentation file (this document).
Setup
Prerequisites
Before running the Stock Tracker application, ensure you have the following:

Python 3.x installed on your system.
An Alpha Vantage API key (replace "YOUR_ALPHA_VANTAGE_API_KEY" in the code with your actual API key).
Installation
Clone the project repository from GitHub:

The application's main menu provides the following options:

Track Stock: Fetch and display the current stock price for a specific symbol.
Set Price Alert: Set a price alert for a stock symbol, specifying a threshold price.
Check Alerts: Check for price alerts and notify if a threshold is crossed.
Exit: Exit the application.
Features
Tracking Stocks
The "Track Stock" option allows you to enter a stock symbol and fetch its current price using the Alpha Vantage API.
Setting Price Alerts
The "Set Price Alert" option lets you set a price alert for a specific stock symbol. You can specify a threshold price that, when crossed, triggers an alert.
Checking Alerts
The "Check Alerts" option checks for price alerts you've set. If any threshold is crossed, the application notifies you.
Customization
Data Storage
The data_storage.py script contains example functions for saving and retrieving alerts. You can customize this script to use your preferred data storage method, such as a file or a database.


Contributions to this project are welcome! You can fork the repository, make improvements, and create a pull request.

For Modular imports: from api.stock_data import fetch_stock_data