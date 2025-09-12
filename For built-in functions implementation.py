"""1.	Реалізуйте власну версію функцій len(), sum(), та min(). Використовуйте спеціальні методи __len__, __iter__, __getitem__, якщо необхідно.
2.	Напишіть тест для кожної з реалізованих функцій."""


class CustomList:
    """A class to support len, sum, and min operations."""

    def __init__(self, items):
        """Initialize list with items."""
        self.items = items

    def __len__(self):
        """Return the length of the list."""
        return len(self.items)

    def __iter__(self):
        """Return an iterator for the list."""
        return iter(self.items)

    def __getitem__(self, index):
        """Return item at the given index."""
        return self.items[index]


if __name__ == "__main__":
    cl = CustomList([1, 2, 3, 4, 5])
    print(len(cl))
    print(sum(cl))
    print(min(cl))