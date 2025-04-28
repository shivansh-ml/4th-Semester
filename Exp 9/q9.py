import numpy as np
import matplotlib.pyplot as plt


companies = ["Apple", "Microsoft", "Google", "AMD"]
profits = [3000, 8000, 1000, 10000]
plt.figure(figsize=(8, 4))
plt.bar(companies, profits, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Company")
plt.ylabel("Profit")
plt.title("Company Profits")
plt.show()

plt.figure(figsize=(8, 4))
plt.barh(companies, profits, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Profit")
plt.ylabel("Company")
plt.title("Company Profits (Horizontal)")
plt.show()