import numpy as np 

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
    