import numpy as np

# Sample dataset of student scores
scores = np.array([88, 75, 92, 67, 85, 90, 78, 95])

# Searching for specific scores
search_scores = [75, 90]
indices = {score: np.where(scores == score)[0] for score in search_scores}

# Sorting the array
sorted_ascending = np.sort(scores)
sorted_descending = np.sort(scores)[::-1]

# Output results
print("Indices of searched scores:", indices)
print("Scores in ascending order:", sorted_ascending)
print("Scores in descending order:", sorted_descending)
