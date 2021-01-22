import pytest


@pytest.fixture(scope="class")
def test_demo():
    print("before test...")
    yield
    print("after test...")


@pytest.fixture()
def data_load():
    return ["Ayaan", "Mir", "Rash"]


@pytest.fixture(params=["chrome", "ie", ("firefox", "Mir")])
def cross_browser(request):
    return request.param
