import pytest
import json
import Student
import System

#Verifies that the database is updated with the correct assignment, submission, submission date and in the correct course
def test_submit_assignment(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')
    grading_system.usr.submit_assignment('software_engineering', 'assignment2', 'Dooby-Doo', '4/1/20')
    assert 'assignment2' in grading_system.users['yted91']['courses']['software_engineering'], "assignment2 should be in software_engineering"
    assert grading_system.users['yted91']['courses']['software_engineering']['assignment2']['submission'] == 'Dooby-Doo', "submission should equal Dooby-Doo"
    assert grading_system.users['yted91']['courses']['software_engineering']['assignment2']['submission_date'] == '4/1/20', "Submission Date should equal 04/01/20"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
