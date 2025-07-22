import numpy as np
from typing import Union

G = 6.67430e-11

def get_mass(*, density: float, volume: float) -> float:
    """Calculate mass from density and volume.
    
    Args:
        density: Material density (kg/m³)
        volume: Object volume (m³)
        
    Returns:
        Mass in kg
    """
    if density < 0 or volume < 0:
        raise ValueError("Density and volume must be non-negative")
    return density * volume


def get_force(*, mass: float, acceleration: float) -> float:
    """Calculate force from mass and acceleration using Newton's second law.
    
    Args:
        mass: Object mass (kg)
        acceleration: Acceleration (m/s²)
        
    Returns:
        Force in Newtons
    """
    if mass < 0:
        raise ValueError("Mass must be non-negative")
    return mass * acceleration


def get_mass_vectorized(densities: np.ndarray, volumes: np.ndarray) -> np.ndarray:
    """Calculate masses for multiple objects using vectorized operations.
    
    Args:
        densities: Array of material densities (kg/m³)
        volumes: Array of object volumes (m³)
        
    Returns:
        Array of masses in kg
    """
    densities = np.asarray(densities)
    volumes = np.asarray(volumes)
    
    if np.any(densities < 0) or np.any(volumes < 0):
        raise ValueError("Densities and volumes must be non-negative")
    
    return densities * volumes


def get_force_vectorized(masses: np.ndarray, accelerations: np.ndarray) -> np.ndarray:
    """Calculate forces for multiple objects using vectorized operations.
    
    Args:
        masses: Array of object masses (kg)
        accelerations: Array of accelerations (m/s²)
        
    Returns:
        Array of forces in Newtons
    """
    masses = np.asarray(masses)
    accelerations = np.asarray(accelerations)
    
    if np.any(masses < 0):
        raise ValueError("Masses must be non-negative")
    
    return masses * accelerations


def calculate_gravitational_forces(positions: np.ndarray, masses: np.ndarray) -> np.ndarray:
    """Calculate gravitational forces between all pairs of objects.
    
    Args:
        positions: Array of shape (n, 2) containing x,y positions
        masses: Array of shape (n,) containing object masses
        
    Returns:
        Array of shape (n, 2) containing net gravitational forces on each object
    """
    positions = np.asarray(positions)
    masses = np.asarray(masses)
    
    if positions.shape[0] != masses.shape[0]:
        raise ValueError("Number of positions must match number of masses")
    
    if positions.ndim != 2 or positions.shape[1] != 2:
        raise ValueError("Positions must be a 2D array with shape (n, 2)")
    
    n = len(masses)
    forces = np.zeros_like(positions, dtype=np.float64)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                r_vec = positions[j] - positions[i]
                r_mag = np.linalg.norm(r_vec)
                
                if r_mag > 0:
                    force_magnitude = G * masses[i] * masses[j] / (r_mag ** 2)
                    force_direction = r_vec / r_mag
                    forces[i] += force_magnitude * force_direction
    
    return forces


def simulate_particle_system(positions: np.ndarray, velocities: np.ndarray, 
                           masses: np.ndarray, dt: float, steps: int) -> tuple:
    """Simulate a particle system under gravitational forces.
    
    Args:
        positions: Initial positions array of shape (n, 2)
        velocities: Initial velocities array of shape (n, 2)
        masses: Masses array of shape (n,)
        dt: Time step size
        steps: Number of simulation steps
        
    Returns:
        Tuple of (final_positions, final_velocities)
    """
    positions = np.copy(positions)
    velocities = np.copy(velocities)
    
    for _ in range(steps):
        forces = calculate_gravitational_forces(positions, masses)
        accelerations = forces / masses.reshape(-1, 1)
        
        velocities += accelerations * dt
        positions += velocities * dt
    
    return positions, velocities
