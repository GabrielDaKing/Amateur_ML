from activation_functions import *
from layer import Layer
from random import seed

class Network:
    def __init__(self, layers, actifunc_hid = relu, actifunc_out = relu):

        self.layers = [Layer(layers[i], layers[i+1], actifunc_hid if i < (len(layers)-1) else actifunc_out) for i in range(len(layers)-1)]
        pass

    def predict(self, data):
        pass

    def train(self,  data, indept_col = -1):
        pass

    def __repr__(self):

        return '\n\n'.join(layer.__repr__() for layer in self.layers)

def test():
    seed(1)
    network = Network([3,6,6,6,2],actifunc_hid = leaky_relu)
    print(network)

if __name__=="__main__":
    test()
