n = 3000
suma = 0
import random

random.random()
for i in range(n):
    x = random.random()
    if 0.6 < x <= 0.8:
        suma += 1

prob = round ((suma/n)*100,2)
print(f"La probabilidad es {prob}")
