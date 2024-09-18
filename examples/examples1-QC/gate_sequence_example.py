# gate_sequence_example.py

from qsimpy import QuantumCircuit

def gate_sequence_example():
    qc = QuantumCircuit(1)
    qc.x(0)         # Apply X gate to flip qubit 0
    qc.hadamard(0)  # Apply Hadamard to create superposition
    qc.z(0)         # Apply Z gate to introduce phase flip
    result = qc.measure()  # Measure qubit 0
    print("Gate Sequence measurement result:", result)

if __name__ == "__main__":
    gate_sequence_example()
