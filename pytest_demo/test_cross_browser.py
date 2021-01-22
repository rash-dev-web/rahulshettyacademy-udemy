import pytest


@pytest.mark.usefixtures("cross_browser")
class TestParameterization:

    def test_cross_brow(self, cross_browser):
        print(cross_browser)