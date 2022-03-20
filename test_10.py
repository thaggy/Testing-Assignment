import pytest
import System
import json

#Tests if view assignment works
def test_login(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    grading_system.login(username,password)
    with open('Data/users.json') as f:
            data = json.load(f)
    if grading_system.usr.view_assignments('software_engineering')[0] == ['assignment1','1/1/20']:
        assert True
    else:
        assert False

        
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem