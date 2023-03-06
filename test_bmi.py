import pytest
from main import calculate_bmi


def test_normal_bmi():
    """
    Test normal bmi range
    :return:
    Nothing
    """
    assert calculate_bmi(18.5) == "Normal"
    assert calculate_bmi(18.25) == "Underweight"
    assert calculate_bmi(21.75) == "Normal"
    assert calculate_bmi(25.25) == "Overweight"
    assert calculate_bmi(25) == "Overweight"


def test_overweight_bmi():
    """
    Test overweight bmi range
    :return:
    Nothing
    """
    assert calculate_bmi(25) == "Overweight"
    assert calculate_bmi(27) == "Overweight"
    assert calculate_bmi(30) == "Obese"
    assert calculate_bmi(30.25) == "Obese"
    assert calculate_bmi(24.75) == "Normal"

