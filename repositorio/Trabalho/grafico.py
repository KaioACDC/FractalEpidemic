import numpy as np
import matplotlib.pyplot as plt

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


