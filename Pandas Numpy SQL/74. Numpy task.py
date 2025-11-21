import numpy as np

# Random 3x3 matrix
A = np.random.rand(3, 3)

# Row-wise norms
row_norms = np.linalg.norm(A, axis=1, keepdims=True)

# Normalize rows
A_normalized = A / row_norms

print("Original matrix:\n", A)
print("\nRow-normalized matrix:\n", A_normalized)