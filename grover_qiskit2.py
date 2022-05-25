from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import GroverOperator
from qiskit.providers.aer import AerSimulator
from qiskit import transpile
from qiskit import execute

qubits = 10
oracle = QuantumCircuit(qubits)
oracle.z(0)  # good state = first qubit is |1>
grover_op = GroverOperator(oracle, insert_barriers=True)

sim = AerSimulator(method='matrix_product_state')
circ = transpile(grover_op)
#circ.measure_all()
circ.measure_all()
#result = execute(circ, sim, shots=1, blocking_enable=True, blocking_qubits=7).result()

result = execute(circ, sim, shots=100, blocking_enable=True, blocking_qubits=5).result()
#result = run(grover_op)

print(result)
#print(result.get_counts())
print('----------------------------------------------------- \n')