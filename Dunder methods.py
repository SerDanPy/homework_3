"""1. Dunder methods
1.	Реалізуйте клас Fraction (дробові числа), який має методи для додавання, віднімання, множення та ділення двох об'єктів цього класу. Використайте спеціальні методи __add__, __sub__, __mul__, __truediv__.
2.	Реалізуйте метод __repr__, щоб можна було коректно виводити об'єкти цього класу у форматі "numerator/denominator"."""


class Fraction:
    """A class to represent a fraction with numerator and denominator."""

    def __init__(self, numerator, denominator):
        """Initialize fraction with numerator and denominator."""
        if denominator == 0:
            raise ValueError("Знаменник не може бути 0")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """Add two fractions."""
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Subtract one fraction from another."""
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Multiply two fractions."""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Divide one fraction by another."""
        if other.numerator == 0:
            raise ValueError("Division by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __repr__(self):
        """Return string representation of the fraction."""
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    #f3 = Fraction(5, 0)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
    #print(f1 / f3)