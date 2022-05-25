from qiskit import QuantumCircuit, execute
from qiskit import transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.aer import AerSimulator
import random
import operator
import sys

qubits_number = int(sys.argv[1])

def n_rnd(n = qubits_number):
    return format(random.randint(0, 2**n - 1), "b").zfill(n)

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
    output_qubit = QuantumRegister(2, name='out')
    cbits = ClassicalRegister(qubits_number, name='cbits')
    
    circ = QuantumCircuit(var_qubits, output_qubit, cbits)
    
    r = n_rnd()
    # print(r)
    print('Número buscado : ' + ''.join(reversed(r)))
    
    L = []
    for i in range(qubits_number): L.append(i)
    
    circ.h(range(n))
    cont = 1
    while cont < (2**qubits_number)**(1/2) * 3.1415/4:
        circ.barrier(range(n))

        # Random
        c = '0'
        aux = []
        for pos,char in enumerate(r):
            if(char == c):
                aux.append(pos)

        if len(aux)!=0:
            for i in aux:
                circ.x(var_qubits[i])

        circ.mct(L[:n],output_qubit[0],output_qubit[1], mode= 'recursion')
        circ.z(output_qubit)
        circ.mct(L[:n],output_qubit[0],output_qubit[1],mode= 'recursion')

        if len(aux)!=0:
            for i in aux:
                circ.x(var_qubits[i])

        circ.barrier(range(n))

        circ.append(diffuser(n), L[:n])
        cont+=1
    
    circ.measure((L[:n]),(L[:n]))
    
    return circ

g = transpile(grover())

backend= AerSimulator(method="statevector")

h = int(sys.argv[2])

job = execute(g,backend, shots = 1024, blocking_enable=True, blocking_qubits=h )

result = job.result()

count = result.get_counts(g)

max_key = max(count, key = count.get)
print(str(max_key) + ' : '+ str(count[max_key]))
print(count)
print(result.time_taken)