import pytest
import System
import json

#Tests if change grade works
def test_login(grading_system):
    username = 'goggins'
    password =  'augurrox'
    student = 'yted91'
    course = 'software_engineering'
    grade = 100
    assignment = 'assignment1'
    grading_system.login(username,password)
    grading_system.usr.change_grade(student,course,assignment,grade)
    with open('Data/users.json') as f:
            data = json.load(f)
    if data[student]['courses'][course][assignment]['grade'] == grade:
        assert True
    else:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem