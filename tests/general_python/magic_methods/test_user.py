from src.general_python.magic_methods import User


def test_equal_user():
    user1 = User(name="mark", age=22)
    user2 = User(name="mark", age=22)
    assert user1 == user2


def test_not_equal_user():
    user1 = User(name="mark", age=22)
    user2 = User(name="marc", age=22)
    assert user1 != user2
