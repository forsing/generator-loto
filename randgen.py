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
