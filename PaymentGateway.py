"""1.	Реалізуйте клас Price, що представляє ціну товару з можливістю заокруглення до двох десяткових знаків. Додайте методи для додавання, віднімання та порівняння цін.
2.	Поміркуйте, як клас Price може бути використаний в майбутньому класі PaymentGateway для обробки фінансових транзакцій."""


class Price:
    """A class to represent a price with rounding to two decimal places."""

    def __init__(self, amount):
        """Initialize price with an amount."""
        self.amount = round(amount, 2)

    def __add__(self, other):
        """Add two prices."""
        return Price(self.amount + other.amount)

    def __sub__(self, other):
        """Subtract one price from another."""
        return Price(self.amount - other.amount)

    def __lt__(self, other):
        """Compare prices (less than)."""
        return self.amount < other.amount

    def __eq__(self, other):
        """Check if two prices are equal."""
        return self.amount == other.amount

    def __repr__(self):
        """Return string representation of the price."""
        return f"Price({self.amount})"


if __name__ == "__main__":
    p1 = Price(10.555)
    p2 = Price(5.333)
    print(p1)
    print(p1 + p2)
    print(p1 - p2)
    print(p1 < p2)
    print(p1 == p2)