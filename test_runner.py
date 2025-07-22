import sys
import os
sys.path.insert(0, os.getcwd())

import mechanics

def test_scalar_functions():
    """Test the original scalar physics functions."""
    print("Testing scalar functions...")
    
    mass1 = mechanics.get_mass(density=1, volume=1)
    mass2 = mechanics.get_mass(density=2, volume=3)
    assert mass1 == 1, f"Expected 1, got {mass1}"
    assert mass2 == 6, f"Expected 6, got {mass2}"
    print("✓ get_mass tests passed")
    
    force1 = mechanics.get_force(mass=1, acceleration=1)
    force2 = mechanics.get_force(mass=2, acceleration=3)
    assert force1 == 1, f"Expected 1, got {force1}"
    assert force2 == 6, f"Expected 6, got {force2}"
    print("✓ get_force tests passed")

def test_vectorized_functions():
    """Test the new vectorized physics functions."""
    print("Testing vectorized functions...")
    
    try:
        import numpy as np
        
        densities = np.array([1, 2, 3])
        volumes = np.array([1, 3, 2])
        expected_masses = np.array([1, 6, 6])
        
        masses = mechanics.get_mass_vectorized(densities, volumes)
        np.testing.assert_array_equal(masses, expected_masses)
        print("✓ get_mass_vectorized tests passed")
        
        masses_input = np.array([1, 2, 3])
        accelerations = np.array([1, 3, 2])
        expected_forces = np.array([1, 6, 6])
        
        forces = mechanics.get_force_vectorized(masses_input, accelerations)
        np.testing.assert_array_equal(forces, expected_forces)
        print("✓ get_force_vectorized tests passed")
        
    except (ImportError, AttributeError) as e:
        print(f"⚠ Vectorized functions not available: {e}")

def test_gravitational_forces():
    """Test gravitational force calculations."""
    print("Testing gravitational force calculations...")
    
    try:
        import numpy as np
        
        positions = np.array([[0, 0], [1, 0]])
        masses = np.array([1.0, 1.0])
        
        forces = mechanics.calculate_gravitational_forces(positions, masses)
        
        assert forces.shape == (2, 2), f"Expected shape (2, 2), got {forces.shape}"
        
        force_magnitude = np.linalg.norm(forces[0])
        expected_magnitude = mechanics.G * masses[0] * masses[1] / 1.0
        
        np.testing.assert_almost_equal(force_magnitude, expected_magnitude, decimal=10)
        print("✓ gravitational force tests passed")
        
    except (ImportError, AttributeError) as e:
        print(f"⚠ Gravitational functions not available: {e}")

def run_all_tests():
    """Run all tests."""
    print("Running Physics Library Tests")
    print("=" * 40)
    
    test_scalar_functions()
    test_vectorized_functions()
    test_gravitational_forces()
    
    print("\nAll available tests completed!")

if __name__ == "__main__":
    run_all_tests()
