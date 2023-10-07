"""Testing get_gradus()."""


import pytest

from main import get_gradus

test_cases = (
    (2.0, 10.0, 1.0, 0, 1432.8),
    (20.0, 3.0, 0.5, 1.0, 14.4),
    (6.0, 15.0, 0.01, 2.0, 298.8),
    (100.0, 1000.0, 0, 0, 0),
)


@pytest.mark.parametrize('radius, time, acl, speed, expected', test_cases)
def test_get_gradus(radius: float, time: float, acl: float, speed: float, expected: float):
    """Start testing of get_radius().

    Args:
        radius: float - radius of sphere
        time: float - time of rotation
        acl: float - acceleration of moving
        speed: float - speed before measurement
        expected: float - result of measurment
    """
    assert get_gradus(radius, time, acl, speed) == expected
