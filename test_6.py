import pytest
import System
import json
#Tests if drop student works
def test_login(grading_system):
    username = 'goggins'
    password =  'augurrox'
    course = 'software_engineering'
    student = 'yted91'
    grading_system.login(username,password)
    grading_system.usr.drop_student(student,course)
    with open('Data/users.json') as f:
            data = json.load(f)
    if course in data[student]['courses']:
        assert False
    else:
        assert True
    



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem