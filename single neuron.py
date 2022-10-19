# Ahmed Nur Sidik (21091397038)

import numpy as np
# Layer input 10 features
inputs = [1.3, 1.6, 1.9, 2.2, 2.4, 2.6, 3.0, 3.5, 4.0, 4.5]
weights = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

# Neuron 1
bias = 4.0

outputs = np.dot(weights, inputs) + bias
print(outputs)