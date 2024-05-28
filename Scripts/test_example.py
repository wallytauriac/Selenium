import pytest
import pytest_html

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

@pytest.mark.parametrize("num", [1, 2, 3])
def test_example(num):
    assert num % 2 == 0


if __name__ == "__main__":
    pytest.main(["test_example.py", "-s", "--html=report.html", "--self-contained-html"])
