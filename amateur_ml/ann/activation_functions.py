# https://missinglink.ai/guides/neural-network-concepts/7-types-neural-network-activation-functions-right/
from math import exp

def sig(x):
    # https://en.wikipedia.org/wiki/Sigmoid_function
    return 1/(1 + exp(-x))

def tanh(x):
    # https://en.wikipedia.org/wiki/Hyperbolic_functions
    return (exp(2*x) - 1)/(exp(2*x) + 1)

def relu(x):
    
    return max(x, 0)

def leaky_relu(x):

    return max(0.1*x, x)

def parametric_relu(x, a):

    return max(a*x, x)

def swish(x):
    # https://arxiv.org/abs/1710.05941v1
    return x/(1 + exp(-x))

def test():
    print(sig(-200))

if __name__=="__main__":
    test()
