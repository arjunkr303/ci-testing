import pytest
from calculator import calculate_tip

def test_basic_tip():
    result = calculate_tip(100, 15)
    assert result["tip"] == 15.0
    assert result["total"] == 115.0

def test_split_between_people():
    result = calculate_tip(100, 20, people=4)
    assert result["per_person"] == 30.0

def test_negative_bill_raises():
    with pytest.raises(ValueError):
        calculate_tip(-50, 10)

def test_zero_people_raises():
    with pytest.raises(ValueError):
        calculate_tip(100, 10, people=0)