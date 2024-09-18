# superposition_example.py

from qsimpy.circuit import QuantumCircuit

def superposition_example():
    qc = QuantumCircuit(2)
    qc.hadamard(0)  # Create superposition on qubit 0
    # result = qc.measure_all()  # Measure qubit 0
    print("Superposition state:", qc)

if __name__ == "__main__":
    superposition_example()
