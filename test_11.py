import pytest
import System
import json

#Tests if professor can drop a student in a course not taught by professor
def test_login(grading_system):
    username = 'goggins'
    password =  'augurrox'
    grading_system.login(username,password)
    grading_system.usr.drop_student('akend3', 'comp_sci')
    with open('Data/users.json') as f:
            data = json.load(f)
    if 'comp_sci' in data['akend3']['courses']:
        assert True
    else:
        assert False
        
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem