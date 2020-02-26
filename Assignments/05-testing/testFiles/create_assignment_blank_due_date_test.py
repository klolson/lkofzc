import pytest
import json
import Staff
import System

#Tests if an assignment can be made without a due date, this is not allowed
def test_create_assignment_blank_due_date(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('assignment3', '', 'comp_sci')
    grading_system.reload_data()
    assert len(grading_system.courses['comp_sci']['assignments']['assignment3']['due_date']) != 0, "There should be a string for due_date"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
