import pytest
import json
import Staff
import System

#Tests that the correct grade is changed on the correct student in the database
def test_change_grade(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', 50)
    grading_system.reload_data()
    assert grading_system.users['yted91']['courses']['software_engineering']['assignment1']['grade'] == 50, "Should be 50"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
