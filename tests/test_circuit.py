import numpy as np
from qsimpy.circuit import QuantumCircuit

def test_pauli_x_gate():
    qc = QuantumCircuit(1)
    qc.x(0)
    assert np.allclose(qc.state, np.array([[0], [1]]))  # Should be |1>

def test_pauli_y_gate():
    qc = QuantumCircuit(1)
    qc.y(0)
    assert np.allclose(qc.state, np.array([[0], [1j]]))  # Should be |i> since Y applied to |0> gives i|1>

def test_pauli_z_gate():
    qc = QuantumCircuit(1)
    qc.z(0)
    assert np.allclose(qc.state, np.array([[1], [0]]))  # Should remain |0>

def test_hadamard_gate():
    qc = QuantumCircuit(1)
    qc.hadamard(0)
    assert np.allclose(qc.state, np.array([[1], [1]]) / np.sqrt(2))  # Superposition
