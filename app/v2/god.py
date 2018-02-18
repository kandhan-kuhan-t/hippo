from typing import List, Dict
import numpy as np
from app.v2.models import Layer


class Simulator:
    def __init__(
            self,
            number_of_layers: int,
            layer_sizes: List[int],
            dilutions: List[int]
    ):
        self.number_of_layers = number_of_layers
        self.layer_sizes = layer_sizes
        self.dilutions = dilutions

        self.input_layer = Layer(
            name="layer_0",
            is_input_layer=True,
            is_output_layer=False,
            size=self.layer_sizes[0]
        )

        self.output_layer = Layer(
            name=f"layer_{self.number_of_layers-1}",
            is_input_layer=False,
            is_output_layer=True,
            size=self.layer_sizes[-1]
        )

        self.middle_layers: List[Layer] = [self.input_layer]

        for i in range(1, self.number_of_layers-1):
            layer = Layer(
                name=f"layer_{i}",
                is_output_layer=False,
                is_input_layer=False,
                size=self.layer_sizes[i]
            )
            self.middle_layers.append(layer)

        self.middle_layers.append(self.output_layer)

        for i in range(0, self.number_of_layers-1):
            self.middle_layers[i].connect_with_next_layer(
                dilution=self.dilutions[i],
                next_layer=self.middle_layers[i+1]
            )

    def run_one_cycle(self, input_: np.ndarray):
        if len(input_) != self.input_layer.size:
            raise Exception("Error in input dimension")

        self.input_layer.store.set_neuron_activated_values(
            input_
        )
        self.input_layer.allow_neuron_firings_to_pass()

        for layer in self.middle_layers[1:-1]:
            layer.calculate_activation_value()
            layer.allow_neuron_firings_to_pass()

        self.output_layer.calculate_activation_value()

        for layer_number in range(0, self.number_of_layers-1):
            self.run_hebbian(layer_number)

        import pdb;pdb.set_trace()

    def run_hebbian(self, layer_number):
        left_layer = self.middle_layers[layer_number]
        right_layer = self.middle_layers[layer_number+1]
        current_synapse_matrix = left_layer.store.get_current_outgoing_synapses()
        master_synapse_matrix = left_layer.store.get_master_outgoing_synapses()
        right_layer_activations = right_layer.store.get_neuron_activated_values()
        for right_index, right_neuron in enumerate(right_layer_activations):
            if right_neuron == 1:
                incoming_synapses = current_synapse_matrix[0:, right_index]
                for left_index, synapse in enumerate(incoming_synapses):
                    if synapse > 0:
                        master_synapse_matrix[left_index][right_index] += \
                            master_synapse_matrix[left_index][right_index]/10


if __name__ == '__main__':
    sim = Simulator(
        number_of_layers=4,
        layer_sizes=[5, 4, 4, 4],
        dilutions=[80, 80, 80]
    )
    sim.run_one_cycle(
        input_=np.array([0, 1, 1, 1, 0])
    )