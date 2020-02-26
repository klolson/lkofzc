import pytest
import json
import Student
import System

#Verifies that a student can't submit an assignment if it doesn't contain a submission
def test_submit_assignment_not_exist(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')
    grading_system.usr.submit_assignment('software_engineering', 'assignment2', '', '4/1/20')
    assert len(grading_system.users['yted91']['courses']['software_engineering']['assignment2']['submission']) != 0, "There should be somethin within the submission"
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
