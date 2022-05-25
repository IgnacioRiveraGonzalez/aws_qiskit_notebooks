import qiskit
from qiskit import IBMQ
from qiskit.providers.aer import AerSimulator
from qiskit import transpile
from qiskit import execute
from qiskit.circuit.library import QuantumVolume

qubit=20
sim = AerSimulator(method='unitary')
circ = transpile(QuantumVolume(qubit, 8, seed = 0))
#circ.measure_all()
circ.measure(19,1)
result = execute(circ, sim, shots=1, blocking_enable=True, blocking_qubits=18).result()

print(result)
print('----------------------------------------------------- \n')
