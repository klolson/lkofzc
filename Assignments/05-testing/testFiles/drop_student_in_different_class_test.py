import pytest
import json
import Professor
import System

#Custom Test 1
#Tests if professor's can remove students from classes that they don't teach. Professors shouldn't be able to do this.
def test_drop_student_other_class(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('yted91', 'cloud_computing')
    grading_system.reload_data()
    if 'cloud_computing' not in grading_system.users['goggins']['courses']:
        assert 'cloud_computing' in grading_system.users['yted91']['courses'], "cloud_computing shouldn't be removed, the professor doesn't teach the class"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
