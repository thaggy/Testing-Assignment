import pytest
import System
import json

#Tests if a professor can add a student to a class that is not taught by the professor
def test_login(grading_system):
    username = 'goggins'
    password =  'augurrox'
    grading_system.login(username,password)
    grading_system.usr.add_student('hdjsr7', 'comp_sci')
    with open('Data/users.json') as f:
            data = json.load(f)
    if 'comp_sci' in data['hddjsr7']['courses']:
        assert False
    else:
        assert True
        
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem