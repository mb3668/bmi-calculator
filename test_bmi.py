import pytest
from main import calculate_bmi
from main import categorize_bmi

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
    assert calculate_bmi(63, 125) == 22.68
    assert calculate_bmi(72, 135) == 18.75
    assert calculate_bmi(72, 180) == 25
    assert calculate_bmi(67, 157) == 25.18
