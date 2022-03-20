import pytest
import System
import json

#Tests if view_assignments works
def test_login(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    course = 'software_engineering'
    assignment_name = 'assignment2'
    submission_date = '2/1/20'
    due_date = '2/1/20'
    grading_system.login(username,password)
    with open('Data/users.json') as f:
            data = json.load(f)
    if not data[username]['courses'][course][assignment_name]['ontime'] == grading_system.usr.view_assignments(submission_date,due_date):
        assert True
    else:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem