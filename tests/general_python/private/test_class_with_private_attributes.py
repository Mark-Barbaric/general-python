import pytest
from src.general_python.private.private_attributes import ClassWithPrivateAttributes


@pytest.fixture
def test_private_class() -> ClassWithPrivateAttributes:
    return ClassWithPrivateAttributes(
        public_attribute="public",
        semi_private_attribute="semi_private",
        private_attribute="private"
    )


def test_private_attributes(test_private_class):
    test_private_class._semi_private_method()
    test_private_class.public_method()
    with pytest.raises(AttributeError) as exc:
        test_private_class.__private_attribute == ""

        assert str(exc.value) == "AttributeError: 'ClassWithPrivateAttributes' object has no attribute '__private_attribute'"

    with pytest.raises(AttributeError) as exc:
        test_private_class.__private_method()

        assert str(exc.value) == "AttributeError: 'ClassWithPrivateAttributes' object has no attribute '__private_method'"
