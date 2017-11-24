'''
This script includes the quizes from the Deep Learning Section of Machine Learning Nano degree program. 

Below are the functions that we implement:
    Perception Algorithm
    Logistic Regression
	Gradient Descent

'''


import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    # Fill in code
    for i in range(len(X)):
        pred = prediction(X[i], W, b)
        
        if pred > 0 and y[i] <= 0:
            W[0] = W[0] - learn_rate*X[i][0]
            W[1] = W[1] - learn_rate*X[i][1]
            b = b - learn_rate
        elif pred <= 0 and y[i] > 0:
            W[0] = W[0] + learn_rate*X[i][0]
            W[1] = W[1] + learn_rate*X[i][1]
            b = b + learn_rate
    
    return W, b

# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines

import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))
def prediction(X, W, b):
    return sigmoid(np.matmul(X,W)+b)
def error_vector(y, y_hat):
    return [-y[i]*np.log(y_hat[i]) - (1-y[i])*np.log(1-y_hat[i]) for i in range(len(y))]
def error(y, y_hat):
    ev = error_vector(y, y_hat)
    return sum(ev)/len(ev)

# TODO: Fill in the code below to calculate the gradient of the error function.
# The result should be a list of three lists:
# The first list should contain the gradient (partial derivatives) with respect to w1
# The second list should contain the gradient (partial derivatives) with respect to w2
# The third list should contain the gradient (partial derivatives) with respect to b
def dErrors(X, y, y_hat):
    DErrorsDx1 = [-X[i][0]*(y[i]-y_hat[i]) for i in range(len(y))]
    DErrorsDx2 = [-X[i][1]*(y[i]-y_hat[i]) for i in range(len(y))]
    DErrorsDb = [-(y[i]-y_hat[i]) for i in range(len(y))]
    return DErrorsDx1, DErrorsDx2, DErrorsDb

# TODO: Fill in the code below to implement the gradient descent step.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b.
# It should calculate the prediction, the gradients, and use them to
# update the weights and bias W, b. Then return W and b.
# The error e will be calculated and returned for you, for plotting purposes.
def gradientDescentStep(X, y, W, b, learn_rate = 0.01):
    # TODO: Calculate the prediction
    y_hat = prediction(X, W, b)
    # This calculates the error
    errors = error(y, y_hat)
    # TODO: Calculate the gradient
    grad = dErrors(X, y, y_hat)
    # TODO: Update the weights
    
    W[0] -= sum(grad[0])*learn_rate
    W[1] -= sum(grad[1])*learn_rate
    b -= sum(grad[2])*learn_rate
    
    return W, b, sum(errors)

# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainLR(X, y, learn_rate = 0.01, num_epochs = 100):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    # Initialize the weights randomly
    W = np.array(np.random.rand(2,1))*2 -1
    b = np.random.rand(1)[0]*2 - 1
    # These are the solution lines that get plotted below.
    boundary_lines = []
    errors = []
    for i in range(num_epochs):
        # In each epoch, we apply the gradient descent step.
        W, b, error = gradientDescentStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
        errors.append(error)
    return boundary_lines, errors
