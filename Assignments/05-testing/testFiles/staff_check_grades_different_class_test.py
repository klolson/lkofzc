import pytest
import json
import Staff
import System

#Tests if a staff member can view grades of students in other courses. A staff member shouldn't be able to do this.
def test_staff_check_grades_different_class(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    gradeList = []
    gradeList = grading_system.usr.check_grades('hdjsr7', 'databases')
    assert 'databases' in grading_system.users['cmhbf5']['courses'], "databases not in cmhbf5, this TA can't access grades from this course"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
