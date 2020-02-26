import pytest
import json
import System

#Tests if the correct user is made given a username and password
def test_userLogin(grading_system):
    username = 'calyam'
    password = '#yeet'
    grading_system.login(username,password)
    assert grading_system.users[username]['role'] == 'professor', "Should be professor"
    assert grading_system.users[username]['courses'][0] == 'cloud_computing', "Should be cloud_computing"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
