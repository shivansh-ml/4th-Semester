import numpy as np
import matplotlib.pyplot as plt
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
plt.boxplot([box1, box2], labels=['Box 1', 'Box 2'])
plt.title("Box Plot")
plt.show()
