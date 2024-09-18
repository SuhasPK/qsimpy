from qsimpy import QuantumSimulator
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def apply_oracle_with_cnot(qc, secret_string):
    """Apply the Bernstein-Vazirani oracle using CNOT gates."""
    num_qubits = len(secret_string)
    # Add CNOT gates based on the secret string
    for i, bit in enumerate(secret_string):
        if bit == '1':
            qc.cnot(i,num_qubits)  # Apply CNOT with control qubit i and target qubit num_qubits - 1

def run_bv_algo_with_cnot(secret_string, runs):
    results = []
    num_qubits = len(secret_string) + 1  # Add one extra qubit for the target

    for _ in range(runs):
        qc = QuantumSimulator(num_qubits, noise_strength=0.01)  # Create a quantum circuit with num_qubits

        # Apply X gate to the last qubit to set it to |1>
        qc.x(num_qubits-1)

        # Apply Hadamard to all qubits
        qc.hadamard(range(num_qubits))

        # Apply the oracle
        apply_oracle_with_cnot(qc, secret_string)

        # Apply Hadamard gates again to all qubits except the last one
        qc.hadamard(range(num_qubits - 1))

        # Measure all qubits except the last one
        result = qc.measure(measure_qubits=range(num_qubits - 1)) # Measurement result
        results.append(result.replace("Measured state: ", ""))  # Remove the prefix

    return results
# Parameters
secret_string = '001'  # Secret string for Bernstein-Vazirani algorithm
runs = 100

# Run the algorithm
results = run_bv_algo_with_cnot(secret_string, runs)

# Count occurrences of each measured state
state_counts = Counter(results)

# Calculate the percentage of occurrence of each state
percentages = {state: count / runs * 100 for state, count in state_counts.items()}

# Plot the percentages
plt.bar(percentages.keys(), percentages.values())
plt.xlabel('State')
plt.ylabel('Percentage of Occurrence')
plt.title('Bernstein-Vazirani Algorithm Results')
plt.show()

print("State counts:", state_counts)
print("Percentages:", percentages)