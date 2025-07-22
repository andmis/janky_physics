from . import mechanics


def test_get_mass() -> None:
    assert mechanics.get_mass(density=1, volume=1) == 1
    assert mechanics.get_mass(density=2, volume=3) == 6
