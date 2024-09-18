import numpy as np
from qsimpy.gates import (pauli_x_gate, pauli_z_gate, 
pauli_y_gate, cnot_gate, cz_gate, swap_gate, s_gate, t_gate, 
rx_gate, ry_gate, rz_gate, t_dagger_gate, s_dagger_gate)

from qsimpy.utils import apply_gate  # Import from utils.py


class QuantumCircuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros((2**num_qubits, 1), dtype=complex)  # Initialize in |0> state
        self.state[0] = 1

    def apply_gate(self, gate, qubits):
        """Apply a gate to the circuit's state."""
        self.state = apply_gate(self.state, gate, qubits, self.num_qubits)
        self.clean_state()  # Clean the state after applying the gate
    
    def clean_state(self, threshold=1e-10):
        """Clean small floating point errors from the quantum state."""
        self.state[np.abs(self.state) < threshold] = 0
        self.state = np.round(self.state, decimals=10)  # Optional: Rounds to avoid further artifacts

    def expand_gate(self, gate, qubits):
        """Expand a gate to the full Hilbert space."""
        identity = np.eye(2)
        full_gate = np.eye(1)
        if len(qubits) == 2:
            full_gate = gate
            for i in range(self.num_qubits - len(qubits)):
                full_gate = np.kron(identity, full_gate)
            return full_gate

        for i in range(self.num_qubits):
            if i in qubits:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, identity)
        return full_gate

    def measure_all(self):
        """Measure the quantum state, collapsing to one of the basis states."""
        probabilities = np.abs(self.state)**2
        outcome = np.random.choice(2**self.num_qubits, p=probabilities.flatten())
        self.state = np.zeros((2**self.num_qubits, 1))
        self.state[outcome] = 1
        return f"Measured state: |{bin(outcome)[2:].zfill(self.num_qubits)}>"
    
    def measure(self, measure_qubits):
        """Measure the specified qubits, collapsing to one of the basis states."""
        total_qubits = self.num_qubits
        measured_states = []
        for q in measure_qubits:
            measured_states.append(q)
        all_states = np.arange(2**total_qubits)
        probabilities = np.abs(self.state)**2
        outcome = np.random.choice(all_states, p=probabilities.flatten())
        outcome_bin = bin(outcome)[2:].zfill(total_qubits)
        measured_outcome = ''.join(outcome_bin[q] for q in measure_qubits)
        return f"Measured state: |{measured_outcome}>"

    # Methods to apply gates
    def x(self, qubit):
        """Apply Pauli-X (NOT) gate to a qubit."""
        self.apply_gate(pauli_x_gate(), [qubit])

    def y(self,qubit):
        """Apply Pauli-Y gate to a qubit."""
        self.apply_gate(pauli_y_gate(), [qubit])

    def z(self, qubit):
        """Apply Pauli-Z gate to a qubit."""
        self.apply_gate(pauli_z_gate(), [qubit])

    def y(self, qubit):
        """Apply Pauli-Y gate to a qubit."""
        self.apply_gate(pauli_y_gate(), [qubit])



    def hadamard(self, qubits):
        """Apply Hadamard gate to specified qubits."""
        if isinstance(qubits, int):
            qubits = [qubits]  # Convert single qubit to a list
        for qubit in qubits:
            # Apply Hadamard gate to the specified qubit
            # Assuming Hadamard matrix is already defined and gate application is correct
            H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
            self.apply_gate(H, [qubit])

    def s(self, qubit):
        """Apply the S-gate (Phase gate) to a qubit."""
        self.apply_gate(s_gate(), [qubit])
    
    def s_dagger(self, qubit):
        """Apply the S-gate (Phase gate) to a qubit."""
        self.apply_gate(s_dagger_gate, [qubit])
    

    def t(self, qubit):
        """Apply the T-gate (π/8 gate) to a qubit."""
        self.apply_gate(t_gate(), [qubit])

    def t_dagger(self, qubit):
        """Apply the S-gate (Phase gate) to a qubit."""
        self.apply_gate(t_dagger_gate, [qubit])

    

    def cnot(self, control, target):
        """Apply CNOT gate to the control and target qubits."""
        self.apply_gate(cnot_gate(), [control, target])

    def cz(self, control, target):
        """Apply CZ gate to the control and target qubits."""
        self.apply_gate(cz_gate(), [control, target])

    def swap(self, qubit1, qubit2):
        """Apply SWAP gate to the qubits."""
        self.apply_gate(swap_gate(), [qubit1, qubit2])

    # Rotation gates
    def rx(self, qubit, theta):
        """Apply the rotation gate around the X-axis."""
        self.apply_gate(rx_gate(theta), [qubit])

    def ry(self, qubit, theta):
        """Apply the rotation gate around the Y-axis."""
        self.apply_gate(ry_gate(theta), [qubit])

    def rz(self, qubit, theta):
        """Apply the rotation gate around the Z-axis."""
        self.apply_gate(rz_gate(theta), [qubit])


    def print_state(self):
        """Print the current quantum state."""
        print(f"State:\n{self.state.flatten()}")


    def __repr__(self):
        return f"QuantumCircuit({self.num_qubits} qubits):\nState:\n{self.state}"