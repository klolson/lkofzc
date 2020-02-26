import pytest
import json
import Student
import System

#Verifies that the correct grades are returned to the correct user.
def test_check_grades(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')
    assert grading_system.usr.check_grades('software_engineering') == [['assignment2', 22], ['assignment1',43]], "Grades should be 22 and 43"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
