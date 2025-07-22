import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mechanics
import numpy as np


def test_get_mass() -> None:
    assert mechanics.get_mass(density=1, volume=1) == 1
    assert mechanics.get_mass(density=2, volume=3) == 6


def test_get_force() -> None:
    assert mechanics.get_force(mass=1, acceleration=1) == 1
    assert mechanics.get_force(mass=2, acceleration=3) == 6


def test_get_mass_vectorized() -> None:
    densities = np.array([1, 2, 3])
    volumes = np.array([1, 3, 2])
    expected = np.array([1, 6, 6])
    result = mechanics.get_mass_vectorized(densities, volumes)
    np.testing.assert_array_equal(result, expected)


def test_get_force_vectorized() -> None:
    masses = np.array([1, 2, 3])
    accelerations = np.array([1, 3, 2])
    expected = np.array([1, 6, 6])
    result = mechanics.get_force_vectorized(masses, accelerations)
    np.testing.assert_array_equal(result, expected)


def test_gravitational_forces() -> None:
    positions = np.array([[0, 0], [1, 0]])
    masses = np.array([1.0, 1.0])
    forces = mechanics.calculate_gravitational_forces(positions, masses)
    
    assert forces.shape == (2, 2)
    
    force_magnitude = np.linalg.norm(forces[0])
    expected_magnitude = mechanics.G * masses[0] * masses[1] / 1.0
    np.testing.assert_almost_equal(force_magnitude, expected_magnitude)


def test_input_validation() -> None:
    try:
        mechanics.get_mass(density=-1, volume=1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        mechanics.get_force(mass=-1, acceleration=1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


if __name__ == "__main__":
    test_get_mass()
    test_get_force()
    test_get_mass_vectorized()
    test_get_force_vectorized()
    test_gravitational_forces()
    test_input_validation()
    print("All tests passed!")
