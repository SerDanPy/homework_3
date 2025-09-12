"""1.	Реалізуйте клас Vector, що підтримує операції додавання, віднімання, множення на число та порівняння за довжиною. Використовуйте відповідні dunder-методи (__add__, __sub__, __mul__, __lt__, __eq__).
2.	Додайте до класу метод для отримання довжини вектора."""

import math


class Vector:
    """A class to represent a vector in n-dimensional space."""

    def __init__(self, components):
        """Initialize vector with a list of components."""
        self.components = components

    def __add__(self, other):
        """Add two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        """Subtract one vector from another."""
        if len(self.components) != len(other.components):
            raise ValueError("Вектори повинні мати однакову довжину")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        """Multiply vector by a scalar."""
        return Vector([c * scalar for c in self.components])

    def __lt__(self, other):
        """Compare vectors by their length."""
        return self.length() < other.length()

    def __eq__(self, other):
        """Check if two vectors have the same length."""
        return self.length() == other.length()

    def length(self):
        """Calculate the length (magnitude) of the vector."""
        return math.sqrt(sum(c ** 2 for c in self.components))

    def __repr__(self):
        """Return string representation of the vector."""
        return f"Vector({self.components})"


if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * 2)
    print(round(v1.length(),2))
    print(v1 < v2)
    print(v1 == v2)