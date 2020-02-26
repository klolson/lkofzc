import pytest
import json
import Student
import System

#Verifies if an assignment was turned in on time or not
def test_check_ontime(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')
    assert grading_system.usr.check_ontime('2/5/20', '2/1/20') == False, "Should return false"
    assert grading_system.usr.check_ontime('1/13/20', '2/1/20') == True, "Should return true"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
