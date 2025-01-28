import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt('dados.txt', skiprows=1)

tempo = dados[:, 0]
s = dados[:, 1]
i = dados[:, 2]
r = dados[:, 3]
n = dados[:, 4]

plt.figure(figsize=(10, 6))
plt.plot(tempo, s, label='Suscetíveis', color='blue')
plt.plot(tempo, i, label='Infectados', color='red')
plt.plot(tempo, r, label='Recuperados', color='green')
plt.plot(tempo, n, label='Não infectados', color='purple', linestyle='--')
plt.title("Epidemia")
plt.xlabel("Tempo")
plt.ylabel('Fração da população')
plt.legend()
plt.grid()
plt.show()
