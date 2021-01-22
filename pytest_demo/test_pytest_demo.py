import pytest


def test_demo_print():
    print("Testing")


def test_greet():
    print("Hello")


@pytest.mark.smoke
@pytest.mark.skip
def test_card():
    print("Card...")
