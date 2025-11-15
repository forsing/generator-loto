# Quantum Lotto Number Generator

"""
Za Srbiju Loto 7/39.
Ukupno kombinacija 15380937 (7 brojeva od 1 do 39). 
Koristi kvantni generator slucajnih brojeva baziran na Qiskit biblioteci.
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile

from qiskit_aer import Aer

def generate_random_number(bits=8, shots=15380937):
    
    qr = QuantumRegister(bits)
    cr = ClassicalRegister(bits)
    circuit = QuantumCircuit(qr, cr)
    
    for i in range(bits):
        circuit.h(qr[i])
    
    circuit.measure(qr, cr)
    
    backend = Aer.get_backend('qasm_simulator')

    job = transpile(circuit, backend)
    result = backend.run(job).result()

    counts = result.get_counts(circuit)
      
    binary_str = list(counts.keys())[0]  
    
    return int(binary_str, 2)


def generate_random_sequence(n_numbers, bits=8):
    
    return [generate_random_number(bits=bits) for _ in range(n_numbers)]


def generate_lotto_numbers_7():
    
    numbers = set()
    
    while len(numbers) < 7:
        num = generate_random_number(bits=6)
        
        if 1 <= num <= 39:
            numbers.add(num)
    
    # return list(numbers)
    return sorted(list(numbers))

##########################################################

if __name__ == "__main__":
    print()
    print("Quantum Lotto Number Generator")
    print()

    lotto_numbers_7 = generate_lotto_numbers_7()
    
    formatted_numbers_7 = [f"{num:02d}" for num in lotto_numbers_7]
    
    print(f"Quantum random generisani brojevi: {' - '.join(formatted_numbers_7)}")
    print()

    """
    Quantum Lotto Number Generator

    Quantum random generisani brojevi: 06 - 13 - 14 - 20 - 31 - 34 - 35
    """
