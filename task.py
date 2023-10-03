import math


def task(radius: float, time: float, acceleration: float, start_velocity: float = 0) -> float:
    """Rotation of the ball.
    Args:
        radius (float|int): ball radius (in metres)
        time (float|int): time (in seconds)
        acceleration (float|int): ball acceleration (metres per second squared)
        start_velocity (float|int): ball start velocity (metres per second)

    Returns:
        float - rotation of the ball in degrees
    """
    c = 2 * math.pi * radius
    s = start_velocity * time + (acceleration * (time**2)) / 2
    return round(((s % c) / c * 360), 2)
