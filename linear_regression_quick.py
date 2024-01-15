import sklearn.linear_model
import numpy as np

# stock price
stock_price = np.array([200,230,245,250])

# regression
model = sklearn.linear_model.LinearRegression().fit(np.arange(0,len(stock_price)).reshape((len(stock_price),1)), stock_price)

# predict
print(model.predict([[4],[5]]))
# [272.5 289. ]
