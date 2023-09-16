import requests

def fetch_stock_data(symbol):
    api_key = "YOUR_API_KEY"  # Replace with your API key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        time_series = data.get("Time Series (1min)")
        if time_series:
            latest_time = next(iter(time_series))
            price = time_series[latest_time]["1. open"]
            return float(price)
        else:
            return None
    else:
        return None