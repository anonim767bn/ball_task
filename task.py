"""Return degrees the point of contact will rotate after rotation."""


from math import pi


def get_gradus(radius: float, time: float, acl: float, speed: float) -> float:
    """Get gradus.

    Args:
        radius: float - radius of sphere
        time: float - time of rotation
        acl: float - acceleration of moving
        speed: float - speed before measurement

    Returns:
        float - gradus, result of measurment
    """
    full_rotation = 360
    circle_length = 2 * round(pi, 2) * radius
    route = time * speed + (acl * time ** 2) / 2

    amount_of_rotations = round(route / circle_length, 2)
    return amount_of_rotations * full_rotation
