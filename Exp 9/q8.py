import numpy as np
import matplotlib.pyplot as plt
x = np.array([0, 1, 2, 3, 4, 5])
y1 = [0, 100, 200, 300, 400, 500]
y2 = [50, 20, 40, 20, 60, 70]
y3 = [10, 20, 30, 40, 50, 60]
y4 = [200, 350, 250, 550, 450, 150]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Corrected from subplot to subplots
axs[0, 0].plot(x, y1, label='Line 1')
axs[0, 1].plot(x, y2, label='Line 2', color='r')
axs[1, 0].plot(x, y3, label='Line 3', color='g')
axs[1, 1].plot(x, y4, label='Line 4', color='m')

for ax in axs.flat:
    ax.legend()
plt.show()
