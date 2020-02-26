import pytest
import json
import System

#Tests if the passwords return correctly if the passwords are the same
def test_check_password(grading_system):
    username = 'cmhbf5'
    assert grading_system.check_password(username, 'bestTA') == True, "Should be true"
    assert grading_system.check_password(username, 'BestTA') == False, "Should be false"
    assert grading_system.check_password(username, 'Be$TTA') == False, "Should be false"
    assert grading_system.check_password(username, 'asdjfkh;l') == False, "Should be false"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
