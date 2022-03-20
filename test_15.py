import pytest
import System
import json

#Tests if a student can create an assignment
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    course = 'software_engineering'
    assignment_name = 'assignment1'
    due_date = '2/1/20'
    grading_system.login(username,password)
    grading_system.usr.create_assignment(assignment_name,due_date,course)

        
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem