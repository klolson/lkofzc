import pytest
import json
import Professor
import System

#Verifies that a student will be added to the correct course in the database
def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('akend3', 'cloud_computing')
    grading_system.reload_data()
    assert 'cloud_computing' in grading_system.users['akend3']['courses'], "cloud_computing should be in akend3 dictionary"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
