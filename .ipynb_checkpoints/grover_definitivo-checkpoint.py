from qiskit import QuantumCircuit, Aer, execute

import numpy as np

from qiskit import IBMQ, Aer, assemble, transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer import QasmSimulator

import qiskit
from qiskit import IBMQ
from qiskit.providers.aer import AerSimulator
from qiskit import transpile
from qiskit import execute
from qiskit.circuit.library import QuantumVolume

import qiskit
from qiskit import IBMQ
from qiskit.providers.aer import AerSimulator
from qiskit import transpile
from qiskit import execute
from qiskit.circuit.library import QuantumVolume

from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import QasmSimulator
import qiskit.quantum_info as qi

qc = QuantumCircuit(7)

qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
qc.h(4)
qc.h(5)

qc.x(0)
qc.x(2)
qc.x(3)

qc.mct([0,1,2,3,4,5],6)
qc.z(6)
qc.mct([0,1,2,3,4,5],6)

qc.x(0)
qc.x(2)
qc.x(3)

qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
qc.h(4)
qc.h(5)

qc.x(0)
qc.x(1)
qc.x(2)
qc.x(3)
qc.x(4)
qc.x(5)

qc.h(5)

qc.mct([0,1,2,3,4],5)

qc.h(5)

qc.x(0)
qc.x(1)
qc.x(2)
qc.x(3)
qc.x(4)
qc.x(5)

qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
qc.h(4)
qc.h(5)

grover=transpile(qc)
grover.measure_all()

sim = QasmSimulator(method='density_matrix')

result = execute(grover, sim, shots=1, blocking_enable=True, blocking_qubits=2).result()


print(result)
print('\n --------------------------------------------------------------------------------------------- \n')