import pytest
from main import calculate_bmi
from main import categorize_bmi
from main import int_value

"""
For my tests I split the normal and overweight categories and tested the boundaries on both of them
"""


def test_normal_lower():
    """
    Test the inclusive lower bound of normal range
    """
    assert categorize_bmi(18.5) == "Normal"
    assert categorize_bmi(18.4) == "Underweight"
    assert categorize_bmi(18.6) == "Normal"


def test_normal_upper():
    """
    Test the exclusive upper bound of normal range
    """
    assert categorize_bmi(25) == "Overweight"
    assert categorize_bmi(25.1) == "Overweight"
    assert categorize_bmi(24.9) == "Normal"


def test_overweight_lower():
    """
    Test the exclusive lower bound of overweight range
    """
    assert categorize_bmi(25) == "Overweight"
    assert categorize_bmi(24.9) == "Normal"
    assert categorize_bmi(25.1) == "Overweight"


def test_overweight_upper():
    """
    Test the inclusive upper bound of overweight range
    """
    assert categorize_bmi(30) == "Obese"
    assert categorize_bmi(29.9) == "Overweight"
    assert categorize_bmi(30.1) == "Obese"


def test_bmi_calculation():
    """
    Use 2-D Data Space to Test BMI_CALCULATIONS
    """
    assert calculate_bmi(67, 115) == 18.45
    assert calculate_bmi(67, 116) == 18.61
    assert calculate_bmi(67, 155) == 24.86
    assert calculate_bmi(67, 157) == 25.18


def test_passed_value():
    """
    Tests the value passed through int_value
    """
    assert int_value("5") == True
    assert int_value("7") == True
    assert int_value("-10") == False
    assert int_value("a") == False