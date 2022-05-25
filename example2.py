import qiskit
from qiskit import IBMQ
from qiskit.providers.aer import AerSimulator
from qiskit import transpile
from qiskit import execute
from qiskit.circuit.library import QuantumVolume

qubit=28
sim = AerSimulator(method='statevector')
circ = transpile(QuantumVolume(qubit, 8, seed = 0))
circ.measure_all()
result = execute(circ, sim, shots=1, blocking_enable=True, blocking_qubits=23).result()

print(result)
print('----------------------------------------------------- \n')
