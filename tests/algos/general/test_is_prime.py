from src.algos.general.is_prime import is_prime


def test_is_prime():
    assert is_prime(1)
    assert not is_prime(16)
    assert is_prime(17)
    assert not is_prime(21)
    assert is_prime(31)
    assert is_prime(101)
    assert not is_prime(121)
    assert not is_prime(64)