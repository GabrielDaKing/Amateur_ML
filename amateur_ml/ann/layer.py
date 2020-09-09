from activation_functions import *
from neuron import Neuron


class Layer():
    """
    A class to handle the working of a layer in the neural network.
    """
    def __init__(self, no_of_inputs, no_of_neurons, actifunc = relu):

        self.neurons = [Neuron(no_of_inputs, actifunc = actifunc) for _ in range(no_of_neurons)]
        self.no_of_inputs = no_of_inputs

    def __repr__(self):

        return "Number of inputs: "+str(self.no_of_inputs) + "\nNumber of neurons: " + str(len(self.neurons)) + '\n\nNeurons: \n\n' + '\n\n'.join([neuron.__repr__() for neuron in self.neurons])

def test():
    layer = Layer(5,10)

    print(layer)

if __name__=="__main__":
    test()
