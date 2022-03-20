import pytest
import System
import json

#Tests if submit_assignment works
def test_login(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    course = 'software_engineering'
    assignment_name = 'assignment1'
    submission = 'why'
    submission_date = '2/2/20'
    due_date = '2/1/20'
    grading_system.login(username,password)
    grading_system.usr.submit_assignment(course,assignment_name,submission,submission_date)
    with open('Data/users.json') as f:
            data = json.load(f)
    if assignment_name in data[username]['courses'][course] and data[username]['courses'][course][assignment_name]['submission'] == submission and data[username]['courses'][course][assignment_name]['submission_date'] == submission_date and not data[username]['courses'][course][assignment_name]['ontime'] == grading_system.usr.view_assignments(submission_date,due_date):
        assert True
    else: 
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem