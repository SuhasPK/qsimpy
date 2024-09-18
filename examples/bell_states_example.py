# bell_state_example.py

from qsimpy.circuit import QuantumCircuit

def bell_state_example():
    qc = QuantumCircuit(2)
    qc.hadamard(0)  # Create superposition on qubit 0
    qc.cnot(0, 1)   # Entangle qubit 0 with qubit 1
    # result = qc.measure()  # Measure both qubits
    print("Bell State :", qc)

if __name__ == "__main__":
    bell_state_example()
