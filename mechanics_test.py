from . import mechanics


def test_get_mass() -> None:
    assert mechanics.get_mass(density=1, volume=1) == 1
    assert mechanics.get_mass(density=2, volume=3) == 6


def test_get_force() -> None:
    assert mechanics.get_force(mass=1, acceleration=1) == 1
    assert mechanics.get_force(mass=2, acceleration=3) == 6
