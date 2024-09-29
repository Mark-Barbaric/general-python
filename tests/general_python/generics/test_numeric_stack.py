from src.general_python.generics.numeric_stack import Stack, NumericStack


def test_str_stack():
    stack = Stack[str]()
    stack.push("hello")
    assert not stack.is_empty()
    top = stack.top()
    assert top == "hello"
    stack.push("my")
    stack.push("name")
    top = stack.top()
    assert top == "name"
    popped = stack.pop()
    assert popped == "name"
    top = stack.top()
    assert top == "my"


def test_int_stack():
    stack = NumericStack[int]()
    word: str = "hello"
    stack.push(word)
    stack.push(1)
    assert not stack.is_empty()
    assert stack.top() == 1
    popped = stack.pop()
    assert popped == 1
    assert not stack.is_empty()
