"""1.	Реалізуйте клас User з атрибутами first_name, last_name, email. Додайте методи для отримання та встановлення цих атрибутів через декоратор @property.
2.	Додайте методи для перевірки формату email-адреси."""


import re


class User():
    """A class to represent a user."""

    def __init__(self, first_name, last_name, email):
        """Initialize user with first_name, last_name, email."""
        self._first_name = first_name
        self._last_name = last_name
        self._email = self._validate_email(email)


    def _validate_email(self, email):
        """Validate email."""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, email):
            raise ValueError('Invalid email address')
        return email

    @property
    def first_name(self):
        """Get first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Set first name."""
        self._first_name = value

    @property
    def last_name(self):
        """Get last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Set last name."""
        self._last_name = value

    @property
    def email(self):
        """Get email."""
        return self._email

    @email.setter
    def email(self, value):
        """Set email with validation."""
        self._email = self._validate_email(value)

if __name__ == '__main__':
    user = User("Данило", "Сергієнко", "serdaniil88@gmail.com")
    print(user.first_name, user.last_name, user.email)
    user.email = "newemail@gmail.com"
    print(user.email)


