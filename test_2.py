import pytest
import System

#Tests if check password works
def test_login(grading_system):
    username = 'calyam'
    password =  '#yeet'
    incorrectPassword = 'badYeet'
    TAusername = 'cmhbf5'
    TApassword = 'bestTA'
    STUusername = 'yted91'
    STUpassword = 'imoutofpasswordnames'

    if grading_system.check_password(username,password) and not grading_system.check_password(username,incorrectPassword) and grading_system.check_password(STUusername, STUpassword) and not grading_system.check_password(STUusername,incorrectPassword) and grading_system.check_password(TAusername,TApassword) and not grading_system.check_password(TAusername,incorrectPassword):
        assert True
    else:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem