import numpy as np
from qsimpy.circuit import QuantumCircuit

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply S-gate to qubit 0 (initial state is |0>)
qc.s(0)
print(f"After applying S-gate to |0>: {qc.state.flatten()}")

# Reset state to |1>
qc.state = np.array([[0], [1]])

# Apply S-gate to qubit 0 (initial state is |1>)
qc.s(0)
print(f"After applying S-gate to |1>: {qc.state.flatten()}")

# Reset state to |0>
qc.state = np.array([[1], [0]])

# Apply T-gate to qubit 0 (initial state is |0>)
qc.t(0)
print(f"After applying T-gate to |0>: {qc.state.flatten()}")

# Reset state to |1>
qc.state = np.array([[0], [1]])

# Apply T-gate to qubit 0 (initial state is |1>)
qc.t(0)
print(f"After applying T-gate to |1>: {qc.state.flatten()}")
