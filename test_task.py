import pytest

from task import task

# r, t, a, v
test_data = (
    (1, 5, 5, 1, (267.47)),
    (1, 1, 1, 1, (85.94)),
    (2, 5, 10, 0, (340.99))
)


@pytest.mark.parametrize('r, t, a, v, expected', test_data)
def test(r: float, t: float, a: float, v: float, expected):
    assert task(radius=r, time=t, acceleration=a, start_velocity=v) == expected
