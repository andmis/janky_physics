def get_mass(*, density: float, volume: float) -> float:
    return density * volume


def get_force(*, mass: float, acceleration: float) -> float:
    return mass * acceleration
