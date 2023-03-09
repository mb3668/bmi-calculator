import pytest
from main import calculate_bmi
from main import categorize_bmi


def test_normal_lower():
    """
    Test the inclusive lower bound
    """
    assert categorize_bmi(18.5) == "Normal"
    assert categorize_bmi(18) == "Underweight"
    assert categorize_bmi(19) == "Normal"


def test_normal_upper():
    """
    Test the exclusive upper bound
    """
    assert categorize_bmi(25) == "Overweight"
    assert categorize_bmi(25.5) == "Overweight"
    assert categorize_bmi(24.5) == "Normal"


def test_overweight_lower():
    """
    Test the exclusive lower bound
    """
    assert categorize_bmi(25) == "Overweight"
    assert categorize_bmi(24.5) == "Normal"
    assert categorize_bmi(25.5) == "Overweight"


def test_overweight_upper():
    """
    Test the inclusive upper bound
    """
    assert categorize_bmi(30) == "Obese"
    assert categorize_bmi(29.5) == "Overweight"
    assert categorize_bmi(30.5) == "Obese"


def test_bmi_calculation():
    assert calculate_bmi(63, 125) == 22.68
    assert calculate_bmi(72, 135) == 18.75
    assert calculate_bmi(72, 180) == 25
    assert calculate_bmi(67, 157) == 25.18
