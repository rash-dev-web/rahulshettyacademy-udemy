import pytest


def test_method1():
    print("method 1")


@pytest.mark.smoke
@pytest.mark.xfail
def test_method2():
    print("method 2")
    assert False
