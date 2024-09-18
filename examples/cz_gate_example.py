import numpy as np
from qsimpy import QuantumCircuit

# Define the initial states
initial_states = [
    np.array([1, 0, 0, 0]),  # |00>
    np.array([0, 1, 0, 0]),  # |01>
    np.array([0, 0, 1, 0]),  # |10>
    np.array([0, 0, 0, 1])   # |11>
]

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

for state in initial_states:
    qc.state = state.reshape(-1, 1)  # Set the initial state
    qc.cz(0, 1)  # Apply the CZ gate
    print(f"Input state: {state} -> CZ gate output: {qc.state.flatten()}")

