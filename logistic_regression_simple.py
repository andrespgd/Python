import sklearn.linear_model
import numpy as np

# Data ( number of cigarrates per day, cancer)
X = np.array([[0,False],[5,False],[10,False],[65,True],[80,True],[90,True],])

# logistic regression
model = sklearn.linear_model.LogisticRegression().fit(X[:,0].reshape(len(X),1), X[:,1])

# Predict
print(model.predict([[20],[30],[70],[85]]))
