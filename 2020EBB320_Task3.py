import numpy as np
import matplotlib.pyplot as plt
import control as co

R = 0.025
L = 0.3
A = [[0, 0, 0], [0, 0, R * np.pi], [0, 0, 0]]
B = [[R / 2, R / 2], [0, 0], [-R / L, R / L]]
B1 = [[R / 2], [0], [-R / L]]
B2 = [[R / 2], [0], [R / L]]
C = [0, 0, 1]
D = 0

ssSystem = co.ss(A, B, C, D)
ssSystem1 = co.ss(A, B1, C, D)
ssSystem2 = co.ss(A, B2, C, D)
print("R\t", R)
print("L\t", L)
print("A\t", A)
print("B\t", B)
print("C\t", C)
print("D\t", D)

print(ssSystem)
tfSystem = co.ss2tf(ssSystem1)
print(tfSystem)
tfSystem2 = co.ss2tf(ssSystem1)
print(tfSystem2)
