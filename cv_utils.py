import numpy as np 

# activation functuons
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def relu(x):
    return(x > 0, x , 0) # if the element is greater than 0, return that element, Otherwise, return 0.

def linear(x):
    return 

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

# loss functions
# mean squared error
def mse(p, y):
    return np.mean(np.square(p - y))

# mean absolute error
def mae(p, y):
    return np.mean(np.abs(p - y))

def binary_cross_entropy(p, y):
    return -np.mean((y * np.log(p) + (1-y) * np.log(1 - p)))

def categorical_cross_entropy(p, y):
    return -np.mean(np.log(p[np.arange(len(y)), y]))