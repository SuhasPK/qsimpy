import numpy as np

def apply_gate(circuit_state, gate, qubits, num_qubits):
    """Apply a gate to the quantum state."""
    # Check if the gate is callable (i.e., a function that returns a matrix)
    if callable(gate):
        gate = gate()  # Call the function to get the gate matrix
    gate_expanded = expand_gate(gate, qubits, num_qubits)
    return np.dot(gate_expanded, circuit_state)

def expand_gate(gate, qubits, num_qubits):
    """Expand a gate to the full Hilbert space for multiple qubits."""
    identity = np.eye(2)
    full_gate = np.eye(1)
    
    if len(qubits) == 2:
        full_gate = gate
        for i in range(num_qubits - len(qubits)):
            full_gate = np.kron(identity, full_gate)
        return full_gate

    for i in range(num_qubits):
        if i in qubits:
            full_gate = np.kron(full_gate, gate)
        else:
            full_gate = np.kron(full_gate, identity)
    return full_gate


