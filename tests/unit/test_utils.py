import pytest
from utils.helpers import format_player_name, calculate_win_rate


def test_format_player_name_normal():
    assert format_player_name("   steve   ") == "Steve"
    assert format_player_name("roman") == "Roman"

def test_format_player_name_empty():
    assert format_player_name("") == ""

def test_format_player_name_invalid_type():
    with pytest.raises(TypeError, match="Ім'я має бути рядком"):
        format_player_name(123)


def test_calculate_win_rate_normal():
    assert calculate_win_rate(50, 100) == 50.0
    assert calculate_win_rate(3, 10) == 30.0

def test_calculate_win_rate_zero_matches():
    assert calculate_win_rate(0, 0) == 0.0

def test_calculate_win_rate_invalid_data():
    with pytest.raises(ValueError, match="Некоректні дані матчу"):
        calculate_win_rate(15, 10)
    
    with pytest.raises(ValueError):
        calculate_win_rate(-1, 5)