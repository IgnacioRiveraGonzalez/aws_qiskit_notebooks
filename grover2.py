from qiskit import QuantumCircuit, execute
from qiskit import transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.aer import AerSimulator
import operator

qubits_number = 8

def diffuser(nqubits = qubits_number):
    qc = QuantumCircuit(nqubits)
    for qubit in range(nqubits):
        qc.h(qubit)
    for qubit in range(nqubits):
        qc.x(qubit)
    qc.h(nqubits-1)
    qc.mct(list(range(nqubits-1)), nqubits-1)
    qc.h(nqubits-1)
    for qubit in range(nqubits):
        qc.x(qubit)
    for qubit in range(nqubits):
        qc.h(qubit)
    U_s = qc.to_gate()
    U_s.name = "U$_s$"
    return U_s

def grover(n = qubits_number):
    var_qubits = QuantumRegister(qubits_number, name='v')
    output_qubit = QuantumRegister(1, name='out')
    cbits = ClassicalRegister(qubits_number, name='cbits')

    circ = QuantumCircuit(var_qubits, output_qubit, cbits)

    L = []
    for i in range(qubits_number): L.append(i)
    circ.h(range(n))
    cont = 1
    while cont < (2**qubits_number)**(1/2) * 3.1415/4:
        circ.barrier(range(n))
        
        circ.mct(L[:n],output_qubit,0)
        circ.z(output_qubit)
        circ.mct(L[:n],output_qubit,0)
        
        circ.barrier(range(n))

        circ.append(diffuser(n), range(n))
        cont+=1
    
    
    
    circ = transpile(circ)
    circ.measure(range(n),range(n))
    return circ

sim = AerSimulator(method='density_matrix')
#circ = transpile(grover())
#circ.measure_all()
result = execute(grover(), sim, shots = 2048, blocking_enable=True, blocking_qubits=6).result()
#result = execute(circ, sim, shots = 1, blocking_enable=True, blocking_qubits=3).result()
#print(result.get_counts())
count=result.get_counts()
max_key = max(count, key = count.get)
print(str(max_key) + ' : '+ str(count[max_key]))

print('\n ----------------------------------------------------------------------------------------------- \n')
print(result)
print('\n ----------------------------------------------------------------------------------------------- \n')