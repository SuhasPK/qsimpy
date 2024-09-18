# tests/test_gates.py

import numpy as np
from qsimpy.gates import (hadamard_gate, pauli_x_gate, pauli_y_gate,
                          pauli_z_gate, s_gate, t_gate, cnot_gate)

def test_hadamard_gate():
    H = hadamard_gate()
    expected_H = (1 / np.sqrt(2)) * np.array([[1, 1],
                                              [1, -1]])
    assert np.allclose(H, expected_H), "Hadamard gate matrix is incorrect"

def test_pauli_x_gate():
    X = pauli_x_gate()
    expected_X = np.array([[0, 1],
                           [1, 0]])
    assert np.allclose(X, expected_X), "Pauli-X gate matrix is incorrect"

def test_pauli_y_gate():
    Y = pauli_y_gate()
    expected_Y = np.array([[0, -1j],
                           [1j, 0]])
    assert np.allclose(Y, expected_Y), "Pauli-Y gate matrix is incorrect"

def test_pauli_z_gate():
    Z = pauli_z_gate()
    expected_Z = np.array([[1, 0],
                           [0, -1]])
    assert np.allclose(Z, expected_Z), "Pauli-Z gate matrix is incorrect"

def test_phase_gate():
    S = s_gate()
    expected_S = np.array([[1, 0],
                           [0, 1j]])
    assert np.allclose(S, expected_S), "Phase gate matrix is incorrect"

def test_t_gate():
    T = t_gate()
    expected_T = np.array([[1, 0],
                           [0, (1 + 1j) / np.sqrt(2)]])
    assert np.allclose(T, expected_T), "T gate matrix is incorrect"

def test_cnot_gate():
    CNOT = cnot_gate()
    expected_CNOT = np.array([[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 0, 1],
                              [0, 0, 1, 0]])
    assert np.allclose(CNOT, expected_CNOT), "CNOT gate matrix is incorrect"
