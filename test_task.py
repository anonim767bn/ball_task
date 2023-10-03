"""Module for testing test function."""
import pytest

from task import task

# r, t, a, v
test_data = (
    (1, 5, 5, 1, (267.47)),
    (1, 1, 1, 1, (85.94)),
    (2, 5, 10, 0, (340.99)),
)


@pytest.mark.parametrize('rad, time, acc, velo, expected', test_data)
def test(rad: float, time: float, acc: float, velo: float, expected: tuple):
    """Testing task() function.

    Args:
        rad (float): The radius.
        time (float): The time.
        acc (float): The acceleration.
        velo (float): The start velocity.
        expected (tuple): expected result of calling the task() function.
    """
    assert task(radius=rad, time=time, acceleration=acc, start_velocity=velo) == expected
