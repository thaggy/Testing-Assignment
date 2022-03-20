import pytest
import System
import json

#Tests if check grade works
def test_login(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    course = 'databases'
    grading_system.login(username,password)
    with open('Data/users.json') as f:
            data = json.load(f)
    grades = grading_system.usr.check_grades(course)
    if grades[0] == ['assignment1',100]:
        assert True
    else:
        assert False
        
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem