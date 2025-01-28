import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def sistema_e_d(t, y, t_inf, t_rec):
    s, i , r = y
    dsdt = -t_inf * s * i 
    didt = t_inf * s * i - t_rec * i
    drdt = t_inf * i
    return [dsdt, didt, drdt]

t_inf = 0.5
t_rec = 0.1

s0 = 0.99
i0 = 0.01
r0 = 0.0

delta_t = (0, 50)
eval_t = np.linspace(delta_t[0], delta_t[1], 1000)

solucao = solve_ivp(sistema_e_d, delta_t, [s0, i0, r0], args=(t_inf, t_rec), eval_t=eval_t)

x = solucao.y[0]
y = solucao.y[1]

plt.figure(figsize=(8, 8))
for i in range(len(x)):
    plt.plot(x[:i], y[:i], 'b-', alpha=0.5, linewidth=0.5)

plt.title("Gráfico")
plt.xlabel("Suscetíveis")
plt.ylabel("Infectados")
plt.grid(True)
plt.show()