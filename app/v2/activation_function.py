import numpy as np
import math


def if_one_third_synapses_activated(
        synapse_values_of_a_neuron: np.ndarray
) -> int:
    existent_synapse_count = 0
    activated_synapse_count = 0

    for synapse_value in synapse_values_of_a_neuron:
        if synapse_value > -0.:
            print(f"existent synapse - {synapse_value}")
            existent_synapse_count += 1
            if synapse_value != 0:
                activated_synapse_count += 1
    if activated_synapse_count >= math.ceil(existent_synapse_count/3):
        return 1
    return 0
