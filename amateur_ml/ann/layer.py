from neuron import Neuron
from activation_functions import *

class Layer():
    def __init__(self, no_of_inputs, no_of_neurons, actifunc = relu):

        self.neurons = [Neuron(no_of_inputs, actifunc) for _ in range(no_of_neurons)]
        self.no_of_inputs = no_of_inputs

    def __repr__(self):

        return "Number of inputs: "+str(self.no_of_inputs) + "\nNumber of neurons: " + str(len(self.neurons))

    def details(self):
        
        print("Number of inputs: "+str(self.no_of_inputs) + "\nNumber of neurons: " + str(len(self.neurons)))

        for neuron in self.neurons:
            print(neuron)

def test():
    layer = Layer(5,10)

    print(layer.details())

if __name__=="__main__":
    test()

    
