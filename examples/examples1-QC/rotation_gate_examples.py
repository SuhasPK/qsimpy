import numpy as np
from qsimpy.circuit import QuantumCircuit

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply Rx gate to qubit 0 with a rotation of pi/2
qc.rx(0, np.pi/2)
print(f"After applying Rx(pi/2) to |0>: {qc.state.flatten()}")

# Reset state to |0>
qc.state = np.array([[1], [0]])

# Apply Ry gate to qubit 0 with a rotation of pi/2
qc.ry(0, np.pi/2)
print(f"After applying Ry(pi/2) to |0>: {qc.state.flatten()}")

# Reset state to |0>
qc.state = np.array([[1], [0]])

# Apply Rz gate to qubit 0 with a rotation of pi/2
qc.rz(0, np.pi/2)
print(f"After applying Rz(pi/2) to |0>: {qc.state.flatten()}")
