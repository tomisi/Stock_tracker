# Function to save alerts to a file or database
def save_alerts(alerts):
    try:
        with open("alerts.txt", "w") as file:
            for alert in alerts:
                file.write(f"{alert.symbol}, {alert.threshold}\n")
        print("Alerts saved successfully.")
    except Exception as e:
        print(f"Error saving alerts: {str(e)}")

# Function to retrieve saved alerts from a file or database
def get_alerts():
    try:
        alerts = []
        with open("alerts.txt", "r") as file:
            for line in file:
                symbol, threshold = line.strip().split(", ")
                alerts.append((symbol, float(threshold)))
        return alerts
    except Exception as e:
        print(f"Error retrieving alerts: {str(e)}")
        return []