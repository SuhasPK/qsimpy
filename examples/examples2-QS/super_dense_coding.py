# superdense_coding_example.py

import numpy as np
from qsimpy import QuantumSimulator

def create_entangled_pair():
    """Create an entangled Bell state between Alice and Bob."""
    qc = QuantumSimulator(2, noise_strength=0.01)
    qc.hadamard(0)  # Apply Hadamard gate to qubit 0
    qc.cnot(0, 1)   # Apply CNOT gate with qubit 0 as control and qubit 1 as target
    return qc

def encode_classical_bits(qc, bits):
    """Encode two classical bits into Alice's qubit."""
    if bits[0] == 1:
        qc.x(0)  # Apply X gate if the first bit is 1
    if bits[1] == 1:
        qc.z(0)  # Apply Z gate if the second bit is 1

def decode_classical_bits(qc):
    """Decode the classical bits on Bob's side."""
    # Apply CNOT gate with qubit 0 as control and qubit 1 as target
    qc.cnot(0, 1)
    # Apply Hadamard gate to qubit 0
    qc.hadamard(0)
    # Measure the qubits
    return qc.measure_all()

def superdense_coding(bits):
    """Perform superdense coding protocol."""
    # Create an entangled Bell state
    qc = create_entangled_pair()
    
    # Encode the classical bits into Alice's qubit
    encode_classical_bits(qc, bits)
    
    # Simulate sending Alice's qubit to Bob
    # Now Bob performs decoding on the combined qubits
    result = decode_classical_bits(qc)
    
    print("Encoded bits:", bits)
    print("Measurement result:", result)

if __name__ == "__main__":
    # Example: Encode bits (1, 0) and perform superdense coding
    superdense_coding(bits=(1, 1))
