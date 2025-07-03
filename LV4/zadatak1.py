import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error

def true_function(x):
    y = 1.6345 - 0.6235 * np.cos(0.6067 * x) - 1.3501 * np.sin(0.6067 * x) - 1.1622 * np.cos(2 * x * 0.6067) - 0.9443 * np.sin(2 * x * 0.6067)
    return y

def add_noise_to_data(y):
    np.random.seed(14)
    noise_variance = np.max(y) - np.min(y)
    noisy_data = y + 0.1 * noise_variance * np.random.normal(0, 1, len(y))
    return noisy_data

x = np.linspace(1, 10, 100)
y_true = true_function(x)
y_noisy = add_noise_to_data(y_true)

plt.figure(1)
plt.plot(x, y_noisy, 'ok', label='mjereno')
plt.plot(x, y_true, label='stvarno')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)
plt.show()

np.random.seed(12)
indices = np.random.permutation(len(x))
train_indices = indices[:int(np.floor(0.7 * len(x)))]
test_indices = indices[int(np.floor(0.7 * len(x))) + 1:]

x = x[:, np.newaxis]
y_noisy = y_noisy[:, np.newaxis]

x_train = x[train_indices]
y_train = y_noisy[train_indices]

x_test = x[test_indices]
y_test = y_noisy[test_indices]

plt.figure(2)
plt.plot(x_train, y_train, 'ob', label='train')
plt.plot(x_test, y_test, 'or', label='test')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)
plt.show()

linear_model = lm.LinearRegression()
linear_model.fit(x_train, y_train)

print('Model je oblika y_hat = Theta0 + Theta1 * x')
print(f'y_hat = {linear_model.intercept_} + {linear_model.coef_[0]} * x')

y_test_pred = linear_model.predict(x_test)

MSE_test = mean_squared_error(y_test, y_test_pred)
print(f'MSE na testnim podacima: {MSE_test}')

plt.figure(3)
plt.plot(x_test, y_test_pred, 'og', label='predicted')
plt.plot(x_test, y_test, 'or', label='test')
plt.legend(loc=4)

x_line = np.array([1, 10])
x_line = x_line[:, np.newaxis]
y_line = linear_model.predict(x_line)
plt.plot(x_line, y_line)
plt.show()