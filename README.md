# Stock Tracker

## Introduction

The Stock Tracker is a command-line application written in Python that empowers users to track stock prices, establish price alerts, and monitor those alerts for specific stocks. This documentation serves as a comprehensive guide, outlining the project's structure, functionalities, and usage instructions.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Main Menu](#main-menu)
  - [Features](#features)
    - [Tracking Stocks](#tracking-stocks)
    - [Setting Price Alerts](#setting-price-alerts)
    - [Checking Alerts](#checking-alerts)
  - [Customization](#customization)
  - [Data Storage](#data-storage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The Stock Tracker project is meticulously organized using a modular directory structure:

- **api/**: This directory houses functions dedicated to retrieving stock data from an external API.
- **alerts/**: This directory contains functions for managing price alerts, including setting, checking, and handling them.
- **data/**: This directory contains functions for data storage and retrieval, such as saving and retrieving user-defined alerts.
- **main.py**: This script serves as the application's entry point, orchestrating the overall functionality.
- **README.md**: This file serves as the project's primary documentation, providing a clear understanding of its purpose and usage.

## Setup

### Prerequisites

Before embarking on using the Stock Tracker, ensure your system meets the following requirements:

- **Python 3.x**: A functional installation of Python 3.x is mandatory. To verify this, open your terminal and execute the command `python --version` (or `python3 --version` on some systems). If Python 3.x is not installed, download and install it from the [official website](https://www.python.org/downloads/).
- **Alpha Vantage API Key**: To fetch live stock data, you'll necessitate an API key from Alpha Vantage. You can obtain a free API key by creating an account on their website: [Alpha Vantage](https://www.alphavantage.co/).

### Installation

There are two primary methods for installing the Stock Tracker:

#### Manual Installation (Project Download):

1. Download the project's source code https://github.com/tomisi/Stock_tracker.git.
2. Navigate to the downloaded directory using your terminal's `cd` command.
3. Assuming the project utilizes a `requirements.txt` file to list dependencies, install them using the following command:
    ```bash
    pip install -r requirements.txt
    ```

#### Git Clone (For Developers):

If you intend to contribute to the project's development, clone it from a version control system like Git using the following command:
```bash
git clone https://github.com/tomisi/Stock_tracker.git
