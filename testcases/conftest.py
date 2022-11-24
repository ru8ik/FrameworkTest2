import pytest

@pytest.fixture
def setUp():
    print("Hi")
    print("My name is")
    yield
    print("SlimShady")