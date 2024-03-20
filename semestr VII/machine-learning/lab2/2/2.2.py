import numpy as np
import matplotlib.pyplot as plt

a = 8
b = 5
c = 2

x = np.arange(-10, 11, 0.1)

y_f = (a - 4) * x**2 + (b - 5) * x + (c - 6)

y_g = np.exp(x) * (np.exp(x) + 1)

fig, ax1 = plt.subplots()

ax1.set_xlabel('x')
ax1.set_ylabel(f'y = ({a} - 4)x^2 + ({b} - 5)x + ({c} - 6)', color='blue')
ax1.plot(x, y_f, label=f'y = ({a} - 4)x^2 + ({b} - 5)x + ({c} - 6)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.set_ylabel('y = e^x(e^x + 1)', color='red')
ax2.plot(x, y_g, label='y = e^x(e^x + 1)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Plot of the functions y = f(x) and y = g(x)')
fig.tight_layout()

plt.show()
