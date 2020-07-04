## WEBSITE: https://www.datacamp.com/community/tutorials/deep-learning-python#gs.8aUP2A0

# Import pandas 
import pandas as pd

# Read in white wine data 
white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')
# Read in red wine data 
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')


##################################################### DATA EXPLORATION

# Print info on white wine
print(white.info())
# Print info on red wine
print(red.info())

# First rows of `red` 
red.head()
# Last rows of `white`
white.tail()
# Take a sample of 5 rows of `red`
red.sample(5)
# Describe `white`
white.describe()
# Double check for null values in `red`
pd.isnull(red)


############# VISUALIZE THE DATA - ALCOHOL #############

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2)
ax[0].hist(red.alcohol, 10, facecolor='red', alpha=0.5, label="Red wine")
ax[1].hist(white.alcohol, 10, facecolor='white', ec="black", lw=0.5, alpha=0.5, label="White wine")
fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=1)
ax[0].set_ylim([0, 1000])
ax[0].set_xlabel("Alcohol in % Vol")
ax[0].set_ylabel("Frequency")
ax[1].set_xlabel("Alcohol in % Vol")
ax[1].set_ylabel("Frequency")
fig.suptitle("Distribution of Alcohol in % Vol")
plt.show()

import numpy as np
print(np.histogram(red.alcohol, bins=[7,8,9,10,11,12,13,14,15]))
print(np.histogram(white.alcohol, bins=[7,8,9,10,11,12,13,14,15]))


############# VISUALIZE THE DATA - SULPHATES #############

fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].scatter(red['quality'], red["sulphates"], color="red")
ax[1].scatter(white['quality'], white['sulphates'], color="white", edgecolors="black", lw=0.5)
ax[0].set_title("Red Wine")
ax[1].set_title("White Wine")
ax[0].set_xlabel("Quality")
ax[1].set_xlabel("Quality")
ax[0].set_ylabel("Sulphates")
ax[1].set_ylabel("Sulphates")
ax[0].set_xlim([0,10])
ax[1].set_xlim([0,10])
ax[0].set_ylim([0,2.5])
ax[1].set_ylim([0,2.5])
fig.subplots_adjust(wspace=0.5)
fig.suptitle("Wine Quality by Amount of Sulphates")
plt.show()


############# VISUALIZE THE DATA - ACIDITY #############

np.random.seed(570)

redlabels = np.unique(red['quality'])
whitelabels = np.unique(white['quality'])

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(8, 4))
redcolors = np.random.rand(6,4)
whitecolors = np.append(redcolors, np.random.rand(1,4), axis=0)

for i in range(len(redcolors)):
    redy = red['alcohol'][red.quality == redlabels[i]]
    redx = red['volatile acidity'][red.quality == redlabels[i]]
    ax[0].scatter(redx, redy, c=redcolors[i])
for i in range(len(whitecolors)):
    whitey = white['alcohol'][white.quality == whitelabels[i]]
    whitex = white['volatile acidity'][white.quality == whitelabels[i]]
    ax[1].scatter(whitex, whitey, c=whitecolors[i])
    
ax[0].set_title("Red Wine")
ax[1].set_title("White Wine")
ax[0].set_xlim([0,1.7])
ax[1].set_xlim([0,1.7])
ax[0].set_ylim([5,15.5])
ax[1].set_ylim([5,15.5])
ax[0].set_xlabel("Volatile Acidity")
ax[0].set_ylabel("Alcohol")
ax[1].set_xlabel("Volatile Acidity")
ax[1].set_ylabel("Alcohol") 
#ax[0].legend(redlabels, loc='best', bbox_to_anchor=(1.3, 1))
ax[1].legend(whitelabels, loc='best', bbox_to_anchor=(1.3, 1))
#fig.suptitle("Alcohol - Volatile Acidity")
fig.subplots_adjust(top=0.85, wspace=0.7)
plt.show()


############# PRE-PROCESS THE DATA #############

# Add `type` column to `red` with value 1
red['type'] = 1

# Add `type` column to `white` with value 0
white['type'] = 0

# Append `white` to `red`
wines = red.append(white, ignore_index=True)


############### INTERMEZZO: CORRELATION MATRIX #############

import seaborn as sns
corr = wines.corr()
sns.heatmap(corr, xticklabels=corr.columns.values,
                  yticklabels=corr.columns.values)
plt.show()



############# TRAIN AND TEST SETS #############

# Import `train_test_split` from `sklearn.model_selection`
from sklearn.model_selection import train_test_split

# Specify the data 
X=wines.iloc[:,0:11]

# Specify the target labels and flatten the array 
y=np.ravel(wines.type)

# Split the data up in train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)



############# STANDARDIZE THE DATA #############

# Import `StandardScaler` from `sklearn.preprocessing`
from sklearn.preprocessing import StandardScaler

# Define the scaler 
scaler = StandardScaler().fit(X_train)

# Scale the train set
X_train = scaler.transform(X_train)

# Scale the test set
X_test = scaler.transform(X_test)



############# MODEL #############

import tensorflow as tf

# Initialize the constructor
model = tf.keras.Sequential()
# Add an input layer 
model.add(tf.keras.layers.Dense(12, activation='relu', input_shape=(11,)))
# Add one hidden layer 
model.add(tf.keras.layers.Dense(8, activation='relu'))
# Add an output layer 
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

# Model output shape
model.output_shape
# Model summary
model.summary()
# Model config
model.get_config()
# List all weight tensors 
model.get_weights()


############# COMPILE AND FIT #############

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
                   
model.fit(X_train, y_train,epochs=20, batch_size=1, verbose=1)


############# PREDICT VALUES #############

y_pred = model.predict(X_test)

print(y_pred[:5])
print(y_test[:5])


############# EVALUATE MODEL #############

score = model.evaluate(X_test, y_test,verbose=1)
print(score)

## Import the modules from `sklearn.metrics`
#from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score
#
## Confusion matrix
#confusion_matrix(y_test, y_pred)
#print(confusion_matrix)
#
## Precision is a measure of a classifier’s exactness
#precision_score(y_test, y_pred)
#print(precision_score)
#
## Recall is a measure of a classifier’s completeness
#recall_score(y_test, y_pred)
#print(recall_score)
#
## The F1 Score or F-score is a weighted average of precision and recall
#f1_score(y_test,y_pred)
#print(f1_score)
#
## The Kappa or Cohen’s kappa is the classification accuracy normalized by the imbalance of the classes in the data
#cohen_kappa_score(y_test, y_pred)
#print(cohen_kappa_score)


############# PREDICTING WINE QUALITY #############

############# PRE-PROCESS THE DATA #############

# Isolate target labels
y = wines.quality

# Isolate data
X = wines.drop('quality', axis=1) 

# Scale the data with `StandardScaler`
X = StandardScaler().fit_transform(X)


############# MODEL #############

model = tf.keras.Sequential()
# Add input layer 
model.add(tf.keras.layers.Dense(64, input_dim=12, activation='relu'))
# Add output layer 
model.add(tf.keras.layers.Dense(1))


############# COMPILE THE MODEL, FIT THE DATA #############

import numpy as np
from sklearn.model_selection import StratifiedKFold

seed = 7
np.random.seed(seed)

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
for train, test in kfold.split(X, y):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(64, input_dim=12, activation='relu'))
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    model.fit(X[train], y[train], epochs=10, verbose=1)


############# EVALUATE MODEL #############

mse_value, mae_value = model.evaluate(X[test], y[test], verbose=0)
print(mse_value)
print(mae_value)

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)


############# MODEL FINE-TUNING #############

