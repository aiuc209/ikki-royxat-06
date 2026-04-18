import pytest

def calculate_cubes(a, b):
    return [x**3 + y**3 for x, y in zip(a, b)]

def test_calculate_cubes():
    a = [1, 2, 3]
    b = [4, 5, 6]
    expected_result = [65, 133, 225]
    assert calculate_cubes(a, b) == expected_result

def test_calculate_cubes_empty_lists():
    a = []
    b = []
    expected_result = []
    assert calculate_cubes(a, b) == expected_result

def test_calculate_cubes_lists_of_different_lengths():
    a = [1, 2, 3]
    b = [4, 5]
    with pytest.raises(ValueError):
        calculate_cubes(a, b)

def test_calculate_cubes_non_numeric_values():
    a = [1, 2, '3']
    b = [4, 5, 6]
    with pytest.raises(TypeError):
        calculate_cubes(a, b)
