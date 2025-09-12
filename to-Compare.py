"""1.	Реалізуйте клас Vector, що підтримує операції додавання, віднімання, множення на число та порівняння за довжиною. Використовуйте відповідні dunder-методи (__add__, __sub__, __mul__, __lt__, __eq__).
2.	Додайте до класу метод для отримання довжини вектора."""


class Person:
    """A class to represent a person with name and age."""

    def __init__(self, name, age):
        """Initialize person with name and age."""
        self.name = name
        self.age = age

    def __lt__(self, other):
        """Compare persons by age (less than)."""
        return self.age < other.age

    def __eq__(self, other):
        """Check if two persons have the same age."""
        return self.age == other.age

    def __gt__(self, other):
        """Compare persons by age (greater than)."""
        return self.age > other.age

    def __repr__(self):
        """Return string representation of the person."""
        return f"Person({self.name}, {self.age})"


if __name__ == "__main__":
    people = [Person("Данило", 22), Person("Вероніка", 19), Person("Тетяна", 49)]
    sorted_people = sorted(people)
    print(sorted_people)