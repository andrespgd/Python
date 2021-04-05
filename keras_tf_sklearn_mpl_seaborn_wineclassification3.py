## SOURCE: https://www.datacamp.com/community/tutorials/deep-learning-python#gs.8aUP2A0

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn.metrics
import sklearn.model_selection
import sklearn.preprocessing
import tensorflow as tf

# read data
white = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')
red   = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')

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

############# PLOT - ALCOHOL #############

# histogram bin edges
bins = list(range(5,18))

# histogram values to list
hist_r_alc = np.histogram(red.alcohol,   bins=bins)
hist_w_alc = np.histogram(white.alcohol, bins=bins)

# histogram plot
fig, ax = plt.subplots(1, 2, sharey=True, figsize=(8, 6), dpi=200)
ax[0].hist(red.alcohol,   bins, facecolor='red',   ec='black', lw=0.5, alpha=0.5, label='Red wine')
ax[1].hist(white.alcohol, bins, facecolor='white', ec='black', lw=0.5, alpha=0.5, label='White wine')
ax[0].set_xlabel('Alcohol in % Vol')
ax[0].set_ylabel('Frequency')
ax[1].set_xlabel('Alcohol in % Vol')
ax[1].set_ylabel('Frequency')
fig.suptitle('Distribution of Alcohol in % Vol')
plt.show()

############# PLOT - SULPHATES #############

fig, ax = plt.subplots(1, 2, sharey=True, figsize=(8, 6), dpi=200)
ax[0].scatter(red['quality'],   red['sulphates'],   color='red',   edgecolors='black', lw=0.5)
ax[1].scatter(white['quality'], white['sulphates'], color='white', edgecolors='black', lw=0.5)
ax[0].set_title('Red Wine')
ax[1].set_title('White Wine')
ax[0].set_xlabel('Quality')
ax[1].set_xlabel('Quality')
ax[0].set_ylabel('Sulphates')
ax[1].set_ylabel('Sulphates')
ax[0].set_xlim([0, 10])
ax[1].set_xlim([0, 10])
fig.suptitle('Wine Quality by Amount of Sulphates')
plt.show()

############# PLOT - ACIDITY #############

np.random.seed(570)

redlabels   = np.unique(red['quality'])
whitelabels = np.unique(white['quality'])

fig, ax = plt.subplots(1, 2, sharey=True, figsize=(8, 6), dpi=200)
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
    
ax[0].set_title('Red Wine')
ax[1].set_title('White Wine')
ax[0].set_xlim([0, 1.7])
ax[1].set_xlim([0, 1.7])
ax[0].set_ylim([5, 15.5])
ax[1].set_ylim([5, 15.5])
ax[0].set_xlabel('Volatile Acidity')
ax[0].set_ylabel('Alcohol')
ax[1].set_xlabel('Volatile Acidity')
ax[1].set_ylabel('Alcohol') 
ax[1].legend(whitelabels, loc='best', bbox_to_anchor=(1.3, 1))
fig.subplots_adjust(top=0.85, wspace=0.7)
plt.show()

############# PRE-PROCESS THE DATA #############

# create 'type' 1/0 for red/white and append to wines DF
red['type']   = 1
white['type'] = 0
wines = red.append(white, ignore_index=True)

############### PLOT - CORRELATION MATRIX #############

corr = wines.corr()

# upper triangle (to mask later)
up_triangle = np.triu(corr)

# plot
f, ax = plt.subplots(figsize=(15, 12), dpi=200)
sns.heatmap(corr, xticklabels=corr.columns.values,
                  yticklabels=corr.columns.values,
                  mask=up_triangle,
                  square=True,
                  linewidths=0.5,
                  cmap='Spectral',
                  annot=True,
                  annot_kws={'size':12})
plt.show()

############# TRAIN AND TEST SETS #############

# features
X = wines.iloc[:,0:11]

# target labels (flatten the array)
y = np.ravel(wines.type)

# split
X_train, X_test, y_train, y_test = \
    sklearn.model_selection.train_test_split(X, y, test_size=0.33, random_state=42)

############# STANDARDIZE THE DATA #############

# define the scaler 
scaler = sklearn.preprocessing.StandardScaler().fit(X_train)

# scale the train/test sets
X_train = scaler.transform(X_train)
X_test  = scaler.transform(X_test)

############# MODEL1 - Predict Wine Type Red/White #############

# NN model
model = tf.keras.Sequential()
# input layer 
model.add(tf.keras.layers.Dense(12, activation='relu', input_shape=(11,)))
# hidden layer 
model.add(tf.keras.layers.Dense(8, activation='relu'))
# output layer 
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

# output shape, summary, config, list all weight tensors
model.output_shape
model.summary()
model.get_config()
model.get_weights()

############# COMPILE AND FIT #############

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
                   
model.fit(X_train, y_train,epochs=20, batch_size=1, verbose=1)

############# PREDICT VALUES #############

y_pred = model.predict(X_test)
print('model1 y_test', y_test[:5])
print('model1 y_pred', y_pred[:5])

############# EVALUATE MODEL #############

score = model.evaluate(X_test, y_test,verbose=1)
print('model1 score =', score)
print('model1 r2 =', sklearn.metrics.r2_score(y_test, y_pred))

#from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score
##-Confusion matrix
#confusion_matrix(y_test, y_pred)
##-Precision is a measure of a classifier’s exactness
#precision_score(y_test, y_pred)
##-Recall is a measure of a classifier’s completeness
#recall_score(y_test, y_pred)
##-The F1 Score or F-score is a weighted average of precision and recall
#f1_score(y_test,y_pred)
##-The Kappa or Cohen’s kappa is the classification accuracy normalized by the imbalance of the classes in the data
#cohen_kappa_score(y_test, y_pred)

############# MODEL2A - PREDICTING WINE QUALITY #############

# target label (quality)
y = wines.quality

# create feature vector and scale it
X = wines.drop('quality', axis=1) 
X = sklearn.preprocessing.StandardScaler().fit_transform(X)

# split
X_train, X_test, y_train, y_test = \
    sklearn.model_selection.train_test_split(X, y, test_size=0.33, random_state=42)

# scaler 
scaler = sklearn.preprocessing.StandardScaler().fit(X_train)

# scale the train/test sets
X_train = scaler.transform(X_train)
X_test  = scaler.transform(X_test)

# define model
model2a = tf.keras.Sequential()
model2a.add(tf.keras.layers.Dense(64, input_dim=12, activation='relu'))
model2a.add(tf.keras.layers.Dense(1))

# compile - using rmsprop and mse - very popular for regression
model2a.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

# fit                   
model2a.fit(X_train, y_train, epochs=20, batch_size=1, verbose=1)

# predict 
y_pred = model2a.predict(X_test)
print('model2a y_test', y_test[:5].values.tolist())
print('model2a y_pred', y_pred[:5])

# evaluate
score = model2a.evaluate(X_test, y_test, verbose=1)
print('model2a score =', score)
print('model2a r2 =', sklearn.metrics.r2_score(y_test, y_pred))

############# MODEL2B - PREDICTING WINE QUALITY - WITH K-FOLD #############

seed = 7
np.random.seed(seed)

kfold = sklearn.model_selection.StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)

scores_mae = []
scores_r2 = []
for train, test in kfold.split(X, y):
    # create model
    model2b = tf.keras.Sequential()
    model2b.add(tf.keras.layers.Dense(64, input_dim=12, activation='relu'))
    model2b.add(tf.keras.layers.Dense(1))
    # compile
    model2b.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    # fit
    model2b.fit(X[train], y[train], epochs=10, verbose=1)
    # evaluate MAE
    scores = model2b.evaluate(X[test], y[test], verbose=0)
    scores_mae.append(scores[1] * 100)
    # evalue r2
    y_pred = model2b.predict(X[test])
    #score = model2b.evaluate(X[test], y[test], verbose=1)
    scores_r2.append(sklearn.metrics.r2_score(y[test], y_pred))

print('model2b scores_mae')
print(scores_mae)
print('%.2f%% (+/- %.2f%%)' % (np.mean(scores_mae), np.std(scores_mae)))

print('model2b scores_r2')
print(scores_r2)


