import numpy as np
from math import exp
from scipy.special import expit

"""
ip = [1, 2, 3, 4, 5]

layer_1 = [0.0, 0.0, 0.0, 0.0, 0.0]

layer_2 = [0.0, 0.0, 0.0, 0.0, 0.0]


input_to_layer_1_connections = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

layer_1_layer_2_connections = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

input_to_layer_summed = np.dot(input_to_layer_1_connections, ip)
layer_1_output = np.dot(layer_1_layer_2_connections, input_to_layer_summed)

print(input_to_layer_summed, layer_1_output)
"""

data_ = {
    "meta": {
        "layers": [
            {
                "name": "input",
                "number": 5,
                "initial": [1.0, 2.0, 3.0, 4.0, 5.0]
            },
            {
                "name": "layer_1",
                "number": 5
            },
            {
                "name": "layer_2",
                "number": 5
            }
        ],
        "initial_weights": [
            {
                "from": "input",
                "to": "layer_1",
                "weight": 1,
                "connection_type": "direct_only"
            },
            {
                "from": "layer_1",
                "to": "layer_2",
                "weight": 1,
                "connection_type": "direct_only"
            }
        ]
    }
}


def create(data):
    meta = data['meta']
    vectors = {}
    for layer in meta['layers']:
        if 'initial' in layer.keys():
            vectors[layer['name']] = np.array(layer['initial'])
        else:
            vectors[layer['name']] = np.zeros(layer['number'])
    # print(vectors)
    connections = {}

    for initial_synapse in meta['initial_weights']:
        connection_name = initial_synapse['from'] + 'to' + initial_synapse['to']
        connection = np.zeros(
            (
                len(vectors[initial_synapse['from']]),
                len(vectors[initial_synapse['to']])
            ),
        )
        connections[connection_name] = connection
        if initial_synapse['connection_type'] == 'direct_only':
            np.fill_diagonal(connection, initial_synapse['weight'])
        print(connection)

    def get_total_input(from_layer, to_layer):
        total_input = np.dot(vectors[from_layer], connections[from_layer+'to'+to_layer])
        return total_input

    vectors['layer_1'] = get_total_input('input', 'layer_1')
    print(get_total_input('layer_1', 'layer_2'))


# create(data_)


def binary_step_activation_function(value):
    return 0 if value <= 0 else 1


def sigmoid_activation_function(x):
    "Numerically-stable sigmoid function."
    if x >= 0:
        z = exp(-x)
        return 1 / (1 + z)
    else:
        z = exp(x)
        return z / (1 + z)


class Layer:
    """

    """
    def __init__(self, no, next_layer=None, synapses='direct_only',
                 activation_function='expit'):
        self.number_of_neurons = no
        self.vector = np.zeros(self.number_of_neurons)
        self.next_layer = next_layer
        self.synapses = None
        if synapses == 'direct_only':
            if self.next_layer is None:
                raise Exception
            self.synapses = np.zeros((self.number_of_neurons, self.next_layer.number_of_neurons))
            np.fill_diagonal(self.synapses, 1)
        self.multiplied_synapse_values = None
        self.activation_function = activation_function

    def set_input(self, vector):
        self.vector = vector

    def multiply_with_synapses(self):
        self.multiplied_synapse_values = np.dot(self.vector, self.synapses)

    def apply_activation_function(self):
        if self.activation_function == 'expit':
            self.vector = expit(self.vector)

    def send_to_next_layer(self):
        self.next_layer.set_input(self.multiplied_synapse_values)


layer_2 = Layer(no=5, synapses=None)
layer_1 = Layer(no=5, next_layer=layer_2)
input_layer = Layer(no=5, next_layer=layer_1)
input_layer.set_input(np.array([1, 2, 3, 4, 5]))
input_layer.apply_activation_function()
input_layer.multiply_with_synapses()
input_layer.send_to_next_layer()
layer_1.synapses[0][1] = 1
layer_1.apply_activation_function()
layer_1.multiply_with_synapses()
layer_1.send_to_next_layer()
