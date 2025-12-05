# ==============================================
# **EXERCISE 1: NUMPY ARRAYS (BANKING SECTOR)**
# ==============================================

import numpy as np

transactions = np.array([
    [1200, 1500, 1600, 1700, 1400, 1800],  # Branch 1
    [1000, 1100, 1050, 1300, 1250, 1350],  # Branch 2
    [2000, 2100, 1900, 2200, 2300, 2400],  # Branch 3
    [900,  950,  1000, 1100, 1150, 1200]   # Branch 4
])

print("Transactions Array:\n", transactions)

total_per_branch = np.sum(transactions, axis=1)
print("Total per branch:", total_per_branch)

highest_branch = np.argmax(total_per_branch) + 1
print("Branch with highest transactions: Branch", highest_branch)

avg_monthly = np.mean(transactions)
print("Average monthly transactions:", avg_monthly)

reshaped = transactions.reshape(3, 8)
print("Reshaped Array (3x8):\n", reshaped)
print("NOTE: Reshaping changes layout, not data.")
