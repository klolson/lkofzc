import pytest
import json
import Staff
import System

#Tests if an assignment can be created with a duplicate name. This shouldn't be allowed every assignment should have a unique name
def test_create_duplicate_assignment(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    newAssignment = 'assignment2'
    assert newAssignment not in grading_system.courses['comp_sci']['assignments'], "New assignment must not have a name already being used"
    grading_system.usr.create_assignment('assignment2', '04/01/20', 'comp_sci')
    grading_system.reload_data()

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
