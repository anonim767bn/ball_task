import math


def task(radius: float, time: float, acceleration: float, start_velocity: float = 0) -> float:
    c = 2 * math.pi * radius
    s = start_velocity * time + (acceleration * (time**2))/2
    return round(((s % c) / c * 360), 2)
