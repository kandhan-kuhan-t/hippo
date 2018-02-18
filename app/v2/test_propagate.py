from unittest import TestCase
from app.v2.propagate import _multiply_product, apply_activation_function_to_layer, set_current_synapse_matrix
import numpy


class TestPropagate(TestCase):
    def setUp(self):
        pass

    def test_multiply_product(self):
        neuron_vector = [
            0, 1
        ]
        # Layer 1 size: 2
        # Layer 2 size: 4
        # Dilution : 100

        # Layer_1_Cell_1 -> All cells of Layer 2
        # Layer_1_Cell_2 -> All cells of Layer 2

        synapse_matrices = [
            [0.1, 0.1, 0.1, 0.1],
            [0.1, 0.1, 0.1, 0.1]
        ]

        multiplied_synapses = _multiply_product(
            vector=numpy.array(neuron_vector),
            matrix=numpy.array(synapse_matrices)
        )
        self.assertListEqual(
            list(multiplied_synapses[0]),
            [0, 0, 0, 0]
        )
        self.assertEqual(
            list(multiplied_synapses[1]),
            [0.1, 0.1, 0.1, 0.1]
        )

    def test_apply_activation_function_to_layer(self):
        neuron_vector = [
            0, 1
        ]
        # Layer 1 size: 2
        # Layer 2 size: 4
        # Dilution : 100

        # Layer_1_Cell_1 -> All cells of Layer 2
        # Layer_1_Cell_2 -> All cells of Layer 2

        synapse_matrices = [
            [-1, 0.1, 0.1, 0.1],
            [0.1, 0.1, 0.1, 0.1]
        ]

        multiplied_synapses = _multiply_product(
            vector=numpy.array(neuron_vector),
            matrix=numpy.array(synapse_matrices)
        )

        set_current_synapse_matrix(
            layer_1_name='test_activation_layer1',
            layer_2_name='test_activation_layer2',
            current_synapse_matrix=multiplied_synapses
        )

        activated_values  = apply_activation_function_to_layer(
            from_layer_name='test_activation_layer1',
            to_layer_name='test_activation_layer2'
        )

        self.assertListEqual(
            list(activated_values),
            [True, True, True, True]
        )