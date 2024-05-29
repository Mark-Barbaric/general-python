from src.algos.helpers.timer import timer


@timer
def print_nums():
    for i in range(2000):
        print(i)


def test_timer(capsys):
    print_nums()
    out, err = capsys.readouterr()  # noqa: E731
    assert 'Finished print_nums()' in out
