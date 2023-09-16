class PriceAlert:
    def __init__(self, symbol, threshold):
        self.symbol = symbol
        self.threshold = threshold

    def check_price(self, current_price):
        if current_price >= self.threshold:
            return f"Alert: {self.symbol} has crossed the threshold of ${self.threshold}. Current price: ${current_price}"
        else:
            return None