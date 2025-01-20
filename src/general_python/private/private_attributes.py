class ClassWithPrivateAttributes:
    def __init__(self,
                 public_attribute: str,
                 semi_private_attribute: str,
                 private_attribute: str):
        self.public_attribute = public_attribute
        self._semi_private_attribute = semi_private_attribute
        self.__private_attribute = private_attribute

    def public_method(self) -> None:
        print("this is a public method")
        self.__private_method()

    def _semi_private_method(self) -> None:
        print("this is a private method")

    def __private_method(self) -> None:
        print("this is a private method")
