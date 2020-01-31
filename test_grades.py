
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42


def test_two_grades():
    grades = [10, 30]
    assert compute_hw_average(grades) == 20



def test_two_equal_grades():
    grades = [10, 10]
    assert compute_hw_average(grades) == 10
