from src.general_python.decorators.static_methods import MathUtils


def test_math_utils():
    ans = MathUtils.sum(1, 2)
    assert ans == 3