from random import random, seed
from activation_functions import *

class Neuron:
    """
    A class to handle the working of a single neuron in the network.
    """
    def __init__(self, no_of_inputs, actifunc = relu, zero = False):

        if not zero:
            self.weights = [random() for _ in range(no_of_inputs)]
        else: 
            self.weights = [0 for _ in range(no_of_inputs)]
        self.bias = 0
        self.actifunc = actifunc

    def fire(self, input):

        output = sum([input*weight for input,weight in zip(input,self.weights)])

        return self.actifunc(output)

    def __repr__(self):
        
        return "Weights: " + str(' '.join([str(x) for x in self.weights])) + "\nBias: " + str(self.bias)

def test():
    seed(1)
    neuron = Neuron(5,actifunc = leaky_relu)
    print(neuron)
    print(neuron.fire([1,2,3,4,5]))

if __name__=="__main__":
    test()
