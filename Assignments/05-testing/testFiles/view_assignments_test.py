import pytest
import json
import Student
import System

#Verifies that the correct assignments for the correct course are returned
def test_view_assignments(grading_system):
    grading_system.login('yted91', 'imoutofpasswordnames')
    assert grading_system.usr.view_assignments('cloud_computing') == [['assignment2', '2/3/20'], ['assignment1', '1/3/20']], "Due dates hould be 2/3/20 and 1/3/20"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
