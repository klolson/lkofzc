import pytest
import json
import Staff
import System

#Verifies that an assignment is created with the correct due date in the correct course in the database
def test_create_assignment(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('assignment3', '04/01/20', 'comp_sci')
    grading_system.reload_data()
    assert grading_system.courses['comp_sci']['assignments']['assignment3']['due_date'] == '04/01/20', "Due date should be 04/01/20"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
