"""
| Paket                       | Verzija |
| --------------------------- | ------- |
| **python**                  | 3.11.13 |
| **qiskit**                  | 1.4.4   |
| **qiskit-machine-learning** | 0.8.3   |
| **qiskit-ibm-runtime**      | 0.43.0  |
| **macOS**                   | Tahos   |
| **Apple**                   | M1      |
"""

"""
https://github.com/forsing
https://github.com/forsing?tab=repositories
"""

"""
Loto Skraceni Sistemi
https://www.lotoss.info
ABBREVIATED LOTTO SYSTEMS
"""

"""
svih 4510 izvlacenja
30.07.1985.- 11.11.2025.
"""



from random import randint

# Broj nasumičnih brojeva koje želimo da generišemo
brojeva = 7  

# Opseg iz kojeg želimo da generišemo nasumične brojeve
opseg = (1, 40) 

print()
for i in range(brojeva):
    print(randint(opseg[0], opseg[1]))
print()
"""
31
38
8
16
32
21
15
"""

