import math


def task(radius: float|int, time: float|int, acceleration: float|int, start_velocity: float|int = 0) -> float:
    """Rotation of the ball.
    Args:
        radius: float|int - ball radius (in metres)
        time: float|int - time (in seconds)
        acceleration: float|int - ball acceleration (metres per second squared)
        start_velocity: float|int - ball start velocity (metres per second)

    Returns:
        float - rotation of the ball in degrees
    """
    degress_full_circle = 360
    circumference = 2 * math.pi * radius
    spatium = start_velocity * time + (acceleration * (time**2)) / 2
    return round(((spatium % circumference) / circumference * degress_full_circle), 2)
