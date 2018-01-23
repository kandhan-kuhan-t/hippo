import numpy as np
from typing import Tuple, Dict


def create_vector(no: int):
    vector = np.zeros(no)
    return vector


class Neuron:
    def __init__(self, **kwargs):
        self.layer = kwargs.get('layer', None)
        self.type_ = kwargs.get('type_', 'no_type')
        self.current_value = kwargs.get('initial_weight', 0)
        self.vector_cell_reference = kwargs.get('vector_cell_ref', None)


class Layer:

    def __init__(self, **kwargs):
        self.type_: str = kwargs.get('type_', 'no_type')
        self.number_of_neurons: int = kwargs.get('number_of_neurons', 0)
        self.vector = create_vector(self.number_of_neurons)
        self.neurons = create_neurons(self, self.type_, self.vector)
    pass


class Bridge:
    pass


def create_neurons(layer: Layer, type_: str, vector):
    neurons = []
    for index, v in enumerate(vector):
        neurons.append(Neuron(layer=layer, vector_cell_ref=index, type_=type_))
    return neurons


if __name__ == '__main__':
    x=Layer(number_of_neurons=10)
    print(x.vector)
    print(x.neurons)
    print(x.neurons[1].vector_cell_reference)
