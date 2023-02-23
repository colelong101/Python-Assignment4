import numpy as np

baseArray = np.genfromtxt('packet_base.txt', delimiter=',').reshape(4096, 8)
weightArray = np.genfromtxt('packet_weight.txt', delimiter=',').reshape(4096, 8)

multipliedArray = np.multiply(baseArray, weightArray)

result = (np.max(multipliedArray, axis=1) - np.mean(multipliedArray, axis=1)) * np.min(multipliedArray, axis=1)

answer = np.floor(np.sum(result) % 4096)

print(answer)
