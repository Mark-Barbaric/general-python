from src.algos.general.decode import decode
import pytest
import os

@pytest.fixture
def create_word_file():
    dir_name = os.path.dirname(os.path.realpath(__file__))
    return f"{dir_name}/coding_qual_input.txt"


@pytest.fixture
def create_word_file2():
    dir_name = os.path.dirname(os.path.realpath(__file__))
    return f"{dir_name}/test.txt"


def test_decode(create_word_file):
    assert decode(create_word_file) == "young system present student lot experiment strong crease sun company hurry remember milk us repeat clothe against meant history indicate pitch print bread would"
    

def test_decode2(create_word_file2):
    assert decode(create_word_file2) == "I love computers"