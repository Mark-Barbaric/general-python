class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self._day = day
        self._month = month
        self._year = year

    @classmethod
    def from_string(cls, date_as_string: str) -> object:
        day, month, year = map(int, date_as_string.split('-'))
        date = cls(day, month, year)
        return date

    @staticmethod
    def is_date_valid(date_as_string: str) -> bool:
        day, month, year = map(int, date_as_string.split('-'))

        if day < 0 or day > 31:
            return False

        if month < 0 or month > 12:
            return False

        if year > 3999:
            return False

        return True

    def __str__(self):
        return f"{self._day}-{self._month}-{self._year}"
