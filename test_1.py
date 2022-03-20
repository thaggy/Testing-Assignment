import pytest
import System

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'calyam'
    password =  '#yeet'
    grading_system.login(username,password)
    if grading_system.usr.name == username:
        assert True
    else:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem