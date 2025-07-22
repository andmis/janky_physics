import timeit
import numpy as np
import mechanics

def benchmark_scalar_functions():
    """Benchmark the current scalar physics functions."""
    print("Benchmarking scalar functions...")
    print("=" * 50)
    
    mass_time = timeit.timeit(
        lambda: mechanics.get_mass(density=2.5, volume=10.0), 
        number=100000
    )
    print(f"get_mass (scalar): {mass_time:.6f}s for 100k calls")
    print(f"get_mass (scalar): {mass_time * 10:.1f}ns per call")
    
    force_time = timeit.timeit(
        lambda: mechanics.get_force(mass=5.0, acceleration=9.8), 
        number=100000
    )
    print(f"get_force (scalar): {force_time:.6f}s for 100k calls")
    print(f"get_force (scalar): {force_time * 10:.1f}ns per call")
    
    return mass_time, force_time

def benchmark_vectorized_functions():
    """Benchmark the new vectorized physics functions."""
    print("\nBenchmarking vectorized functions...")
    print("=" * 50)
    
    densities = np.random.uniform(1.0, 10.0, 1000)
    volumes = np.random.uniform(1.0, 10.0, 1000)
    masses = np.random.uniform(1.0, 100.0, 1000)
    accelerations = np.random.uniform(1.0, 20.0, 1000)
    
    mass_time = timeit.timeit(
        lambda: mechanics.get_mass_vectorized(densities, volumes), 
        number=1000
    )
    print(f"get_mass_vectorized: {mass_time:.6f}s for 1k calls (1000 objects each)")
    print(f"get_mass_vectorized: {mass_time:.1f}ns per object")
    
    force_time = timeit.timeit(
        lambda: mechanics.get_force_vectorized(masses, accelerations), 
        number=1000
    )
    print(f"get_force_vectorized: {force_time:.6f}s for 1k calls (1000 objects each)")
    print(f"get_force_vectorized: {force_time:.1f}ns per object")
    
    return mass_time, force_time

def benchmark_gravitational_forces():
    """Benchmark gravitational force calculations."""
    print("\nBenchmarking gravitational force calculations...")
    print("=" * 50)
    
    positions = np.random.uniform(-100, 100, (100, 2))
    masses = np.random.uniform(1.0, 1000.0, 100)
    
    grav_time = timeit.timeit(
        lambda: mechanics.calculate_gravitational_forces(positions, masses), 
        number=100
    )
    print(f"gravitational_forces: {grav_time:.6f}s for 100 calls (100 objects each)")
    print(f"gravitational_forces: {grav_time * 10:.1f}ms per calculation")
    
    return grav_time

def run_all_benchmarks():
    """Run all performance benchmarks."""
    print("Physics Library Performance Benchmarks")
    print("=" * 60)
    
    scalar_times = benchmark_scalar_functions()
    
    try:
        vectorized_times = benchmark_vectorized_functions()
        grav_time = benchmark_gravitational_forces()
        
        print("\nPerformance Comparison:")
        print("=" * 50)
        speedup_mass = (scalar_times[0] * 1000) / vectorized_times[0]
        speedup_force = (scalar_times[1] * 1000) / vectorized_times[1]
        print(f"Mass calculation speedup: {speedup_mass:.1f}x")
        print(f"Force calculation speedup: {speedup_force:.1f}x")
        
    except AttributeError:
        print("\nVectorized functions not yet implemented.")
        print("Run benchmarks again after implementing optimizations.")

if __name__ == "__main__":
    run_all_benchmarks()
