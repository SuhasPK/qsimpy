from qsimpy import QuantumCircuit

def toffoli():
    qc = QuantumCircuit(3)
    
    # Initialize to |111>
    qc.x(0)
    qc.x(1)
    qc.x(2)
    
    # Apply Hadamard to qubit 2
    qc.hadamard(2)
    
    # Apply CNOT gate with control qubit 1 and target qubit 2
    qc.cnot(1, 2)
    
    # Apply T-dagger to qubit 2
    qc.t_dagger(2)
    
    # Apply CNOT gate with control qubit 0 and target qubit 2
    qc.cnot(0, 2)
    
    # Apply T gate to qubit 2
    qc.t(2)
    
    # Apply CNOT gate with control qubit 1 and target qubit 2
    qc.cnot(1, 2)
    
    # Apply T-dagger to qubit 2
    qc.t_dagger(2)
    
    # Apply CNOT gate with control qubit 0 and target qubit 2
    qc.cnot(0, 2)
    
    # Apply T gate to qubits 1 and 2
    qc.t(1)
    qc.t(2)
    
    # Apply CNOT gate with control qubit 0 and target qubit 1
    qc.cnot(0, 1)
    
    # Apply Hadamard to qubit 2
    qc.hadamard(2)
    
    # Apply T and T-dagger gates
    qc.t(0)
    qc.t_dagger(2)
    
    # Print the final state of the quantum circuit
    print(qc)

if __name__ == "__main__":
    toffoli()
