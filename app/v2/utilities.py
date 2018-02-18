import numpy as np
from typing import Union, List
import random
from app.v2 import store

LayerOfNeurons = np.ndarray
SynapseMatrix = np.ndarray


def get_random_numbers(
        number: int,
        from_: int,
        to_: int
) -> List[int]:
    return random.sample(list(range(from_, to_)), k=number)


def get_layer_by_name(
        layer_name: str
) -> LayerOfNeurons:
    return store.get_(
        layer_name
    )


def set_layer_by_name(
        layer: LayerOfNeurons,
        layer_name: str
) -> None:
    store.set_(
        layer_name,
        layer
    )


def set_synapse_matrix(
        layer_1_name: str,
        layer_2_name: str,
        synapse_matrix: SynapseMatrix
) -> None:
    synapse_matrix_name = f"master_{layer_1_name}_to_{layer_2_name}"
    store.set_(
        synapse_matrix_name,
        synapse_matrix
    )


def get_synapse_matrix(
        layer_1_name: str,
        layer_2_name: str
) -> SynapseMatrix:
    synapse_matrix_name = f"master_{layer_1_name}_to_{layer_2_name}"
    synapse_matrix = store.get_(
        synapse_matrix_name
    )
    return synapse_matrix


def create_layer(
        layer_name: str,
        number_of_neurons: int,
) -> LayerOfNeurons:
    new_layer = np.ndarray(
        (number_of_neurons, )
    )
    set_layer_by_name(
        layer_name=layer_name,
        layer=new_layer
    )
    return new_layer


def connect(
        layer_1_name: str,
        layer_2_name: str,
        dilution: float or int,
        initial_value: float
) -> SynapseMatrix:
    layer_1 = get_layer_by_name(layer_1_name)
    layer_2 = get_layer_by_name(layer_2_name)
    layer_1_len = len(layer_1)
    layer_2_len = len(layer_2)
    synapse_matrix: SynapseMatrix = np.full(
        (layer_1_len, layer_2_len), dtype='float', fill_value=-1
    )
    # INITIAL: No connections between layer 1 and layer 2 denoted by -1
    number_of_connections: int = int((layer_2_len / 100) * dilution)
    for layer_1_index, _ in enumerate(layer_1):
        layer_2_indices = get_random_numbers(
            from_=0,
            to_=layer_2_len,
            number=number_of_connections
        )
        for layer_2_index in layer_2_indices:
            synapse_matrix[layer_1_index][layer_2_index] = initial_value
    set_synapse_matrix(
        layer_1_name=layer_1_name,
        layer_2_name=layer_2_name,
        synapse_matrix=synapse_matrix
    )
    return synapse_matrix


def get_synapse_value(
        layer_1_name: str,
        layer_2_name: str,
        layer_1_cell_index: int,
        layer_2_cell_index: int
) -> Union[float, int]:
    synapse_matrix = get_synapse_matrix(
        layer_1_name=layer_1_name,
        layer_2_name=layer_2_name
    )
    return synapse_matrix[layer_1_cell_index][layer_2_cell_index]


def get_synapse_values_for_cell_from_firstlayer(
        layer_1_name,
        layer_2_name,
        cell_index
) -> np.ndarray:
    synapse_matrix = get_synapse_matrix(
        layer_1_name=layer_1_name,
        layer_2_name=layer_2_name
    )
    return synapse_matrix[cell_index]


def get_synapse_values_for_cell_from_secondlayer(
        layer_1_name,
        layer_2_name,
        cell_index
) -> np.ndarray:
    synapse_matrix = get_synapse_matrix(
        layer_1_name=layer_1_name,
        layer_2_name=layer_2_name
    )
    return synapse_matrix[0:, cell_index]
