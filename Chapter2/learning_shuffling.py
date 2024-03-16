import random

# Sample dataset
data = ['apple', 'banana', 'orange', 'grape', 'pineapple']
labels = [0, 1, 2, 3, 4]

# Original order
print("Original order:")
for d, l in zip(data, labels):
    print(f"Data: {d}, Label: {l}")

# Shuffling indices
num_samples = len(data)
shuffled_indices = list(range(num_samples))
random.shuffle(shuffled_indices)

# Shuffled order
print("\nShuffled order:")
for index in shuffled_indices:
    print(f"Data: {data[index]}, Label: {labels[index]}")
