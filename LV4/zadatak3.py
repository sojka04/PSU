import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def true_function(x):
    y = 1.6345 - 0.6235 * np.cos(0.6067 * x) - 1.3501 * np.sin(0.6067 * x) - 1.1622 * np.cos(2 * x * 0.6067) - 0.9443 * np.sin(2 * x * 0.6067)
    return y

def add_noise_to_data(y):
    np.random.seed(14)
    noise_variance = np.max(y) - np.min(y)
    noisy_data = y + 0.1 * noise_variance * np.random.normal(0, 1, len(y))
    return noisy_data

x = np.linspace(1, 10, 50)
y_true = true_function(x)
y_noisy = add_noise_to_data(y_true)

x = x[:, np.newaxis]
y_noisy = y_noisy[:, np.newaxis]

poly = PolynomialFeatures(degree=15)
x_new = poly.fit_transform(x)

np.random.seed(12)
indices = np.random.permutation(len(x_new))
train_indices = indices[:int(np.floor(0.7 * len(x_new)))]
test_indices = indices[int(np.floor(0.7 * len(x_new))) + 1:]

x_train = x_new[train_indices,]
y_train = y_noisy[train_indices]

x_test = x_new[test_indices,]
y_test = y_noisy[test_indices]

linear_model = lm.LinearRegression()
linear_model.fit(x_train, y_train)

y_test_pred = linear_model.predict(x_test)
MSE_test = mean_squared_error(y_test, y_test_pred)

plt.figure(1)
plt.plot(x_test[:, 1], y_test_pred, 'og', label='predicted')
plt.plot(x_test[:, 1], y_test, 'or', label='test')
plt.legend(loc=4)
plt.show()

plt.figure(2)
plt.plot(x, y_true, label='f')
plt.plot(x, linear_model.predict(x_new), 'r-', label='model')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_train[:, 1], y_train, 'ok', label='train')
plt.legend(loc=4)
plt.show()
