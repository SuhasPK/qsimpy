import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from qsimpy import QuantumSimulator

# Create a simulator for a 2-qubit system
sim = QuantumSimulator(2, noise_strength=0.01)

# Function to simulate Bell state creation and measurement
def run_bell_state_simulation(num_runs):
    results = []
    for _ in range(num_runs):
        # Reset simulator
        sim.__init__(2, noise_strength=0.01)  # Reinitialize to reset state
        
        # Apply gates to create Bell state
        sim.hadamard(0)      # Apply Hadamard gate to qubit 0
        sim.cnot(0, 1)       # Apply CNOT gate with qubit 0 as control and qubit 1 as target
        
        # Measure the state and record the result
        result = sim.measure()
        results.append(result)

    return results

# Run the simulation 1000 times
num_runs = 1000
results = run_bell_state_simulation(num_runs)

# Count occurrences of each measured state
state_counts = Counter(results)

# Get all possible states (|00>, |01>, |10>, |11>)
states = ['|00>', '|01>', '|10>', '|11>']
counts = [state_counts[f'Measured state: {state}'] for state in states]

# Calculate probabilities and percentages
probabilities = np.array(counts) / num_runs
percentages = probabilities * 100  # Convert to percentage

# Plotting
fig, ax = plt.subplots()
bars = ax.bar(states, probabilities, color='skyblue')

# Add percentage values on top of bars
for bar, percentage in zip(bars, percentages):
    height = bar.get_height()
    ax.annotate(f'{percentage:.2f}%', 
                xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3),  # Offset label position slightly above the bar
                textcoords="offset points", 
                ha='center', va='bottom')

# Labels and title
ax.set_title("Bell State Measurement Probabilities")
ax.set_ylabel("Probability")
ax.set_xlabel("Measured State")
plt.grid()
ax.set_ylim(0, 1)

# Show plot
plt.show()
