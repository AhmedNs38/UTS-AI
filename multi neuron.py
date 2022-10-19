import numpy as np

inputs = [3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 9.3, 9.6, 9.9]
weights = [
    [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1],
    [2.7, 1.8, 2.6, 2.8, 3.6, 3.8, 4.6, 4.8, 5.6, 5.8],
    [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1],
    [2.7, 1.8, 2.6, 2.8, 3.6, 3.8, 4.6, 4.8, 5.6, 5.8],
    [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1],
]

biases = [1.3, 1.5, 1.3, 3.4, 3.8]

outputs = np.dot(weights, inputs) + biases
print(outputs)