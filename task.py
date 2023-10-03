"""Module for calculating the rotation of a ball."""
import math


def task(radius: float, time: float, acceleration: float, start_velocity: float = 0) -> float:
    """Rotation of the ball.

    Args:
        radius (float) : ball radius (in metres).
        time (float) : time (in seconds).
        acceleration (float) : The ball acceleration (metres per second squared).
        start_velocity (float) : The ball start velocity (metres per second).

    Returns:
        float - rotation of the ball in degrees.
    """
    degrees_full_circle = 360
    circumference = 2 * math.pi * radius
    spatium = start_velocity * time + (acceleration * (time**2)) / 2
    return round(((spatium % circumference) / circumference * degrees_full_circle), 2)
