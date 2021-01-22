import pytest


@pytest.mark.usefixtures("test_demo")
class TestFixtureTest:
    def test_method1(self):
        print("in Method 1")


    def test_method2(self):
        print("in Method q")
