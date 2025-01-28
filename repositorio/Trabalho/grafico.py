import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def sistema_e_d(t, y, t_inf, t_rec):
    s, i , r = y
    dsdt = -t_inf * s * i 
    didt = t_inf * s * i - t_rec * i
    drdt = t_rec * i
    dndt = 0
    return [dsdt, didt, drdt]

t_inf = 0.5
t_rec = 0.1

s0 = 0.99
i0 = 0.01
r0 = 0.0

delta_t = (0, 50)
eval_t = np.linspace(delta_t[0], delta_t[1], 1000)

solucao = solve_ivp(sistema_e_d, delta_t, [s0, i0, r0], args=(t_inf, t_rec), eval_t=eval_t)

s = solucao.y[0]
i = solucao.y[1]
r = solucao.y[2]

plt.figure(figsize=(10, 6))
plt.plot(solucao.t, solucao.y[0], label="Suscetíveis", color="blue")
plt.plot(solucao.t, solucao.y[1], label="Infectados", color="red")
plt.plot(solucao.t, solucao.y[2], label="Recuperados", color="green")
plt.title("Dinâmica Temporal")
plt.xlabel("Tempo")
plt.ylabel("Fração da população")
plt.legend()
plt.grid()
plt.show()