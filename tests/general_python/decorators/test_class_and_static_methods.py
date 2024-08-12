from src.general_python.decorators.class_and_static_methods import Date


def test_valid_date():
    date = Date.from_string('31-10-1999')
    date_string = str(date)
    assert Date.is_date_valid(date_string)


def test_invalid_date():
    date = Date.from_string('31-13-2024')
    date_string = str(date)
    assert not Date.is_date_valid(date_string)
