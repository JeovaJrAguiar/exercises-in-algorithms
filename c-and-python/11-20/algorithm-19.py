# Basic operations
# Aguiar - computer science
# Federal University of Ceara - crateus campus

import math

print("\n===== Basic Operations - Python =====\n")
print("raiz: {}          raiz(64)\n".format(math.sqrt(64)))

# make 4^3, base 4, potenc. 3
result = 1
count = 1
while count <= 3:
	result *= 4
	count +=1
print("exponencial:{}      expo(4,3)\n".format(result))
print("absoluto: {}        abs(-378)\n".format(abs(-378)))
