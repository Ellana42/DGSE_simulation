import matplotlib.pyplot as plt
import numpy as np
from math import exp, log
import seaborn as sns

# constants
theta = 5
sigma = 0.6
heta = 0.5
c_min = 0.1
c_max = 5.1

# variable = 0.1 phase A, 0.55 phase B, 0.75 1.05 phase C
c_0s = [0.1, 0.55, 0.75, 1.05]


def next_log_prod(current_log_prod):
    return heta * current_log_prod + np.sqrt(1 - heta ** 2) * np.random.normal(0, 1)


def g(conso):
    return c_min + (c_max - c_min) / (1 + exp(2 * theta * (c_0 - conso)))


def next_conso(current_conso, current_log_prod):
    return exp(next_log_prod(current_log_prod)) * g(current_conso), next_log_prod(current_log_prod)


zeta_0 = 0

current_log_prod = zeta_0

iterations = range(1000)
i = 0

plt.style.use('ggplot')
fig, axs = plt.subplots(len(c_0s), 2, gridspec_kw={'width_ratios': [3, 1]})
fig.suptitle('Numeric simulation')

for c_0 in c_0s:

    current_conso = c_0
    consos = []

    for _ in iterations:
        consos.append(log(current_conso))
        current_conso, current_log_prod = next_conso(
            current_conso, current_log_prod)

    axs[i, 0].plot(consos, linewidth=1)
    axs[i, 0].plot([log(c_0) for _ in iterations], '--', label='x0', color='c')
    axs[i, 0].set_ylabel('c0 : ' + str(c_0))
    axs[i, 0].legend()

    sns.distplot(consos, ax=axs[i, 1], color='lightblue', hist=False)
    axs[i, 1].axvline(log(c_0), ls='--', label='x0', color='c')
    axs[i, 1].legend()

    i += 1

plt.show()
