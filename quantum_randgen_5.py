# Quantum Lotto Number Generator

"""
Za Srbiju Loto 5/35 + 1/10.
Ukupno kombinacija 3246320 
(5 brojeva od 1 do 35 i 1 broj od 1 do 10). 
Koristi kvantni generator slucajnih brojeva baziran na Qiskit biblioteci.
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile

from qiskit_aer import Aer

def generate_random_number(bits=8, shots=3246320):
    
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


def generate_lotto_numbers_5():
    
    numbers = set()
    
    while len(numbers) < 5:
        num = generate_random_number(bits=6)
        
        if 1 <= num <= 35:
            numbers.add(num)
    
    # return list(numbers)
    return sorted(list(numbers))


def generate_lotto_numbers_1():
    
    numbers = set()
    
    while len(numbers) < 1:
        num = generate_random_number(bits=6)
        
        if 1 <= num <= 10:
            numbers.add(num)
    
    # return list(numbers)
    return sorted(list(numbers))

##########################################################

if __name__ == "__main__":
    print()
    print("Quantum Lotto Number Generator")
    print()

    lotto_numbers_5 = generate_lotto_numbers_5()
    lotto_numbers_1 = generate_lotto_numbers_1()
    
    formatted_numbers_5 = [f"{num:02d}" for num in lotto_numbers_5]
    formatted_numbers_1 = [f"{num:02d}" for num in lotto_numbers_1]

    formatted_numbers = formatted_numbers_5 + formatted_numbers_1

    print(f"Quantum random generisani brojevi: {' - '.join(formatted_numbers)}")
    print()

    """
    Quantum Lotto Number Generator

    Quantum random generisani brojevi: 10 - 18 - 20 - 24 - 31 - 10
    """
