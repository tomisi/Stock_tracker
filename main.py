from api.stock_data import fetch_stock_data
from alerts.price_alerts import PriceAlert
from data.data_storage import save_alerts, get_alerts

def main_menu():
    while True:
        print("\nStock Tracker Menu:")
        print("1. Track Stock")
        print("2. Set Price Alert")
        print("3. Check Alerts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter a stock symbol (e.g., AAPL): ")
            current_price = fetch_stock_data(symbol)
            if current_price is not None:
                print(f"The current price of {symbol} is ${current_price}")
        elif choice == '2':
            symbol = input("Enter a stock symbol (e.g., AAPL): ")
            threshold = float(input("Enter the alert threshold price: "))
            alert = PriceAlert(symbol, threshold)
            alerts = get_alerts() or []  # Retrieve existing alerts or initialize as an empty list
            alerts.append(alert)
            save_alerts(alerts)
        elif choice == '3':
            alerts = get_alerts() or []
            for alert in alerts:
                current_price = fetch_stock_data(alert.symbol)
                if current_price is not None:
                    alert_message = alert.check_price(current_price)
                    if alert_message:
                        print(alert_message)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()