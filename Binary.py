"""1.	Реалізуйте клас BinaryNumber, який представляє двійкове число. Додайте методи для виконання двійкових операцій: AND (__and__), OR (__or__), XOR (__xor__) та NOT (__invert__).
2.	Напишіть тест для цих операцій."""


class BinaryNumber:
    """A class to represent a binary number."""

    def __init__(self, value):
        """Initialize binary number with an integer value."""
        self.value = value

    def __and__(self, other):
        """Perform binary AND operation."""
        return BinaryNumber(self.value & other.value)

    def __or__(self, other):
        """Perform binary OR operation."""
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other):
        """Perform binary XOR operation."""
        return BinaryNumber(self.value ^ other.value)

    def __invert__(self):
        """Perform binary NOT operation."""
        return BinaryNumber(~self.value)

    def __repr__(self):
        """Return string representation of the binary number."""
        return f"Бінарне число({bin(self.value)[2:]})"


if __name__ == "__main__":
    b1 = BinaryNumber(0b1111)
    b2 = BinaryNumber(0b1100)
    print(b1 & b2)
    print(b1 | b2)
    print(b1 ^ b2)
    print(~b1)