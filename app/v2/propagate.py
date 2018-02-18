import numpy as np
from app.v2.utilities import get_layer_by_name, get_synapse_matrix
from app.v2 import store
from app.v2.activation_function import if_one_third_synapses_activated


"""
Master Synapse Matrix
Current Synapse Matrix
"""


def set_current_synapse_matrix(
        layer_1_name: str,
        layer_2_name: str,
        current_synapse_matrix: np.ndarray
):
    store.set_(
        name=f"Current_{layer_1_name}_to_{layer_2_name}",
        obj=current_synapse_matrix
    )


def get_current_synapse_matrix(
        layer_1_name: str,
        layer_2_name: str
) -> np.ndarray:
    return store.get_(
        name=f"Current_{layer_1_name}_to_{layer_2_name}"
    )


def apply_output_to_synapses(
        from_layer_name: str,
        to_layer_name: str,
        set_to_store: bool=True
) -> np.ndarray:
    from_layer = get_layer_by_name(
        layer_name=from_layer_name
    )
    synapse_matrix = get_synapse_matrix(
        layer_1_name=from_layer_name,
        layer_2_name=to_layer_name
    )
    current_synapse_matrix = _multiply_product(
        vector=from_layer,
        matrix=synapse_matrix
    )
    if set_to_store:
        set_current_synapse_matrix(
            layer_1_name=from_layer_name,
            layer_2_name=to_layer_name,
            current_synapse_matrix=current_synapse_matrix
        )
    return current_synapse_matrix


def apply_activation_function_to_layer(
        from_layer_name: str,
        to_layer_name: str
):
    synapse_matrix = get_current_synapse_matrix(
        layer_1_name=from_layer_name,
        layer_2_name=to_layer_name
    )
    activation_values = []
    for i in range(0, synapse_matrix.shape[1]):
        activation_values.append(
            if_one_third_synapses_activated(
                synapse_matrix[0:, i]
            )
        )
    return np.array(activation_values)


def _multiply_product(
        vector: np.ndarray,
        matrix: np.ndarray
):
    resp = []
    for i in range(0, len(vector)):
        resp.append(np.multiply(vector[i], matrix[i]))
    return np.array(resp)

# def a(
#         vector: np.ndarray,
#         matrix: np.ndarray
# ):
#     resp = []
#     for i in range(0, len(vector)):
#         resp.append(np.multiply(vector[i], matrix[i]))
#     return resp
#
#
# def b(
#         vector: np.ndarray,
#         matrix: np.ndarray
# ):
#     return np.multiply(
#         vector,
#         matrix
#     )
#
#
# test_a = timeit.timeit("""a(vector, matrix)""",
#                        number=10, setup="""from __main__ import a;import numpy as n;vector=n.full((10000, ), dtype='float', fill_value=1);matrix=n.full((10000,9000), dtype='float', fill_value=0.2);"""
#                        )
# test_b = timeit.timeit("""b(vector, matrix.T)""",
#                        number=10, setup="""from __main__ import b;import numpy as n;vector=n.full((10000, ), dtype='float', fill_value=1);matrix=n.full((10000,9000), dtype='float', fill_value=0.2);"""
#                        )