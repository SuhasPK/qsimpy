from qsimpy.circuit import QuantumCircuit

def test_measure():
    qc = QuantumCircuit(2)
    qc.hadamard(0)  # Apply H to qubit 0, creates superposition
    qc.cnot(0, 1)   # Apply CNOT, entangling qubit 0 and 1
    outcome = qc.measure()
    assert outcome in ["Measured state: |00>", "Measured state: |11>"]
