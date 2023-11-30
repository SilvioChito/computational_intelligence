import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import hamming
"""
# Sample boolean vectors (replace these with your actual data)
vectors = np.random.choice([0, 1], size=(50, 10))

# Calculate Hamming distances
hamming_distances = np.zeros((len(vectors), len(vectors)))

for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
        distance = hamming(vectors[i], vectors[j])
        hamming_distances[i, j] = distance
        hamming_distances[j, i] = distance

# Calculate similarity scores
similarity_scores = 1 - hamming_distances

# Scatter plot with circle sizes and similarity scores on the y-axis
plt.figure(figsize=(8, 8))
plt.scatter(range(len(vectors)), similarity_scores.mean(axis=1), s=100, alpha=0.5)

plt.title("Graph with Circle Sizes Based on Hamming Distance")
plt.xlabel("Vector Index")
plt.ylabel("Mean Similarity Score")
plt.show()
-------------------
"""

# Sample boolean vectors (replace these with your actual data)
vectors = np.random.choice([0, 1], size=(50, 10))

# Calculate Hamming distances
hamming_distances = np.zeros((len(vectors), len(vectors)))

for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
        distance = hamming(vectors[i], vectors[j])
        hamming_distances[i, j] = distance
        hamming_distances[j, i] = distance

# Create a heatmap
plt.figure(figsize=(10, 8))
heatmap = plt.imshow(hamming_distances, cmap='viridis', interpolation='nearest')

plt.title("Hamming Distances Heatmap")
plt.xlabel("Vector Index")
plt.ylabel("Vector Index")

# Display a colorbar
plt.colorbar(heatmap, label="Hamming Distance")

plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import hamming

# Sample boolean vectors (replace these with your actual data)
vectors = np.random.choice([0, 1], size=(100, 10))

# Calculate Hamming distances
hamming_distances = np.zeros((len(vectors), len(vectors)))

for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
        distance = hamming(vectors[i], vectors[j])
        hamming_distances[i, j] = distance
        hamming_distances[j, i] = distance

# Calculate the mean Hamming distance for each vector
mean_distances = np.mean(hamming_distances, axis=1)

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(range(len(vectors)), mean_distances**2, color='skyblue', edgecolor='black')

plt.title("Mean Hamming Distance for Each Vector")
plt.xlabel("Vector Index")
plt.ylabel("Mean Hamming Distance")
plt.show()

"""