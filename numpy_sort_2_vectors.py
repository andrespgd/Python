import numpy as np

sat_scores = np.array([1100,1256,1543,1020,2000,1000])
students   = np.array(['John','Bob','Jillian','Marsh','Frank'])

# one liner sort
top_3 = students[np.argsort(sat_scores)][:-4:-1]

print(top3)
