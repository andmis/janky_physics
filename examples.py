import numpy as np
import mechanics

def example_basic_usage():
    """Demonstrate basic scalar function usage."""
    print("Basic Physics Calculations")
    print("=" * 30)
    
    mass = mechanics.get_mass(density=7.8, volume=0.001)
    print(f"Steel cube mass: {mass:.3f} kg")
    
    force = mechanics.get_force(mass=mass, acceleration=9.81)
    print(f"Weight force: {force:.3f} N")

def example_vectorized_operations():
    """Demonstrate vectorized operations for multiple objects."""
    print("\nVectorized Operations")
    print("=" * 30)
    
    densities = np.array([7.8, 2.7, 1.0])
    volumes = np.array([0.001, 0.002, 0.005])
    materials = ["Steel", "Aluminum", "Water"]
    
    masses = mechanics.get_mass_vectorized(densities, volumes)
    
    for material, mass in zip(materials, masses):
        print(f"{material}: {mass:.4f} kg")
    
    accelerations = np.array([9.81, 5.0, 2.0])
    forces = mechanics.get_force_vectorized(masses, accelerations)
    
    print("\nForces under different accelerations:")
    for material, force, accel in zip(materials, forces, accelerations):
        print(f"{material} at {accel} m/s²: {force:.4f} N")

def example_gravitational_simulation():
    """Demonstrate gravitational force calculations."""
    print("\nGravitational Force Simulation")
    print("=" * 30)
    
    positions = np.array([
        [0, 0],
        [1, 0],
        [0.5, 0.866]
    ])
    
    masses = np.array([1e12, 1e12, 1e12])
    
    forces = mechanics.calculate_gravitational_forces(positions, masses)
    
    print("Net gravitational forces:")
    for i, force in enumerate(forces):
        magnitude = np.linalg.norm(force)
        print(f"Object {i}: {magnitude:.2e} N")

def example_particle_system():
    """Demonstrate particle system simulation."""
    print("\nParticle System Simulation")
    print("=" * 30)
    
    initial_positions = np.array([
        [0, 0],
        [2, 0],
        [1, 1.732]
    ])
    
    initial_velocities = np.array([
        [0, 0.1],
        [0, -0.05],
        [-0.1, 0]
    ])
    
    masses = np.array([1e12, 1e12, 1e12])
    
    final_pos, final_vel = mechanics.simulate_particle_system(
        initial_positions, initial_velocities, masses, dt=0.1, steps=10
    )
    
    print("Position changes after simulation:")
    for i, (initial, final) in enumerate(zip(initial_positions, final_pos)):
        displacement = np.linalg.norm(final - initial)
        print(f"Object {i}: moved {displacement:.4f} units")

if __name__ == "__main__":
    example_basic_usage()
    example_vectorized_operations()
    example_gravitational_simulation()
    example_particle_system()
