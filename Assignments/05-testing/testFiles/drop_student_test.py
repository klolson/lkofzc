import pytest
import json
import Professor
import System

#Verifies that the student is added and dropped from the correct course in the database
def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('yted91', 'software_engineering')
    grading_system.reload_data()
    assert 'software_engineering' not in grading_system.users['yted91']['courses'], "software_engineering should be removed"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
