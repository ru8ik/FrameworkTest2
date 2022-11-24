import pytest

@pytest.mark.sanity
def usersStatus():
    print("User Ok")


def usersStatusnone():
    print("User bad")