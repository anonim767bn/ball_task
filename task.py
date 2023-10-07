"""Module for calculating the rotation of a ball."""
from math import pi


def task(rad: float, time: float, accel: float, velocity: float = 0) -> float:
    """Rotation of the ball.

    Args:
        rad (float) : ball radius (in metres).
        time (float) : time (in seconds).
        accel (float) : The ball acceleration (metres per second squared).
        velocity (float) : The ball start velocity (metres per second).

    Returns:
        float - rotation of the ball in degrees.
    """
    degrees_full_circle = 360
    circumference = 2 * pi * rad
    spatium = velocity * time + (accel * (time**2)) / 2
    return round(((spatium % circumference) / circumference * degrees_full_circle), 2)
