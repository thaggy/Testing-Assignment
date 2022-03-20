import pytest
import System
import json

#Tests if a student can check grades for a class that they are not in
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    course = 'software_engineering'
    assignment_name = 'assignment1'
    submission = 'why'
    submission_date = '2/2/20'
    due_date = '2/1/20'
    grading_system.login(username,password)
    grading_system.usr.check_grades(course)

        
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem