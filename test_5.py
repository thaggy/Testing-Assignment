import json
import pytest
import System

#Tests if add student works
def test_login(grading_system):
    username = 'goggins'
    password =  'augurrox'
    student_name = 'cmhbf5'
    course = 'software_engineering'
    with open('Data/users.json') as f:
            data = json.load(f)
    grading_system.login(username,password)
    grading_system.usr.add_student(student_name, course)
    if  course in data[student_name]['courses']:
        assert True
    else:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem