import json
import pytest
import System

#Tests if create assignment works
def test_login(grading_system):
    username = 'goggins'
    password =  'augurrox'
    assignment_name = 'newAssignment'
    course = 'software_engineering'
    due_date = '2/2/2022'
    
    grading_system.login(username,password)
    grading_system.usr.create_assignment(assignment_name, due_date, course)
    with open('Data/courses.json') as f:
            data = json.load(f)
    if data[course]['assignments'][assignment_name]['due_date'] == due_date:
        assert True
    else:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem