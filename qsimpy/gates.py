import numpy as np


# Pauli-X (NOT) gate
def pauli_x_gate():
    return np.array([[0, 1],
                     [1, 0]])

# Pauli-Y gate
def pauli_y_gate():
    return np.array([[0, -1j], 
                     [1j, 0]])

# Pauli-Z gate
def pauli_z_gate():
    return np.array([[1, 0],
                     [0, -1]])

# Hadamard gate
def hadamard_gate():
    return np.array([[1, 1],
                     [1, -1]]) / np.sqrt(2)

def cnot_gate():
    """Creates the CNOT gate using Pauli gates."""
    I = np.eye(2)  # Identity matrix
    X = pauli_x_gate()  # Pauli-X gate

    # Construct the CNOT gate matrix
    cnot = np.kron(I, I)  # Start with identity matrix for a 2-qubit system
    cnot[2:, 2:] = X  # Apply X gate to the last 2x2 part (target qubit flip)
    # cnot = np.array([
    #     [1, 0, 0, 0],
    #     [0, 1, 0, 0],
    #     [0, 0, 1, 0],
    #     [0, 0, 0, -1]
    # ])

    return cnot

def cz_gate():
    """Creates the CZ gate using Pauli-Z."""
    I = np.eye(2)  # Identity matrix
    Z = pauli_z_gate()  # Pauli-Z gate
    
    # Construct the CZ gate matrix
    cz = np.kron(I, I)  # Start with identity matrix for a 2-qubit system
    cz[3, 3] = -1  # Apply phase flip for the |11> state
    return cz

def swap_gate():
    """Creates the SWAP gate using Pauli matrices.""" 
    # SWAP gate sequence: 3 CNOTs equivalent, which can be represented with Pauli-X
    # First, the full 4x4 SWAP matrix for 2 qubits
    swap = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ])
    return swap

def s_gate():
    """Return the matrix for the S-gate (Phase gate)."""
    return np.array([[1, 0], 
                     [0, 1j]])  # 1j represents the imaginary unit

def t_gate():
    """Return the matrix for the T-gate (π/8 gate)."""
    return np.array([[1, 0], 
                     [0, np.exp(1j * np.pi / 4)]])  # e^(iπ/4)

def rx_gate(theta):
    """Return the rotation matrix around the X-axis."""
    return np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                     [-1j * np.sin(theta / 2), np.cos(theta / 2)]])

def ry_gate(theta):
    """Return the rotation matrix around the Y-axis."""
    return np.array([[np.cos(theta / 2), -np.sin(theta / 2)],
                     [np.sin(theta / 2), np.cos(theta / 2)]])

def rz_gate(theta):
    """Return the rotation matrix around the Z-axis."""
    return np.array([[np.exp(-1j * theta / 2), 0],
                     [0, np.exp(1j * theta / 2)]])

def t_dagger_gate():
    """Return the T-dagger (π/8 inverse) gate matrix."""
    return np.array([[1, 0],
                     [0, np.exp(-1j * np.pi / 4)]])

def s_dagger_gate():
    """Return the S-dagger (Phase inverse) gate matrix."""
    return np.array([[1, 0],
                     [0, -1j]])
