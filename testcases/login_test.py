import pytest



@pytest.mark.sanity
def testLogin(setUp):
    print("Login Successful")

@pytest.mark.regression
def testLogout2():
    print("Logout Successful2")

@pytest.mark.skip
def testLogout():
    print("Logout Successful")


#steps to Fixture testing
#Arrange
#Act - test
#Assert - verify
#Clenup - finish rest the application state