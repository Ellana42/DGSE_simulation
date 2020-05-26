import matplotlib.pyplot as plt
import numpy as np
from math import exp, log

# constants
theta = 5
sigma = 0.6
heta = 0.5
c_min = 0.1
c_max = 5.1

# variable = 0.1 phase A, 0.55 phase B, 0.75 1.05 phase C
c_0s = [0.1, 0.55, 0.75, 1.05]


def next_error(current_error):
    return heta * current_error + np.sqrt(1 - heta ** 2) * np.random.normal(0, 1)


def g(conso):
    return c_min + (c_max - c_min) / (1 + exp(2 * theta * (c_0 - conso)))


def next_conso(current_conso, current_error):
    return exp(next_error(current_error)) * g(current_conso), next_error(current_error)


# How do I define those ???
zeta_0 = 0

current_error = zeta_0

iterations = range(1000)
i = 0

plt.style.use('ggplot')
fig, axs = plt.subplots(len(c_0s), 1)
fig.suptitle('Numeric simulation')

for c_0 in c_0s:

    current_conso = c_0
    consos = []

    for _ in iterations:
        consos.append(log(current_conso))
        current_conso, current_error = next_conso(current_conso, current_error)

    axs[i].plot(consos)
    axs[i].set_ylabel('c0 : ' + str(c_0))
    i += 1

plt.show()
