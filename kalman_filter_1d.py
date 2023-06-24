# Updates and predicts based on:
# -location measurements AND
# -inferred motions

def update(mean1, var1, mean2, var2):
    new_mean = (mean1 * var2 + mean2 * var1) / (var1 + var2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var  = var1  + var2
    return [new_mean, new_var]

# data
measurements = [5, 6, 7, 9, 10]
motion       = [1, 1, 2, 1,  1]
# variance
measurement_sig = 4
motion_sig      = 2

# first mu and sig are guesses 0 and 10_000
mu  = 0
sig = 10_000
# loop thru update and predict steps
for n in range(len(measurements)):
    #
    mu, sig = update(mu, sig, measurements[n], measurement_sig)
    print('UPDATE ',  mu, sig)
    #
    mu, sig = predict(mu, sig, motion[n], motion_sig)
    print('PREDICT', mu, sig)
