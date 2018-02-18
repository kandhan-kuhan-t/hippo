from unittest import TestCase
from app.v2.activation_function import if_one_third_synapses_activated


class TestActivationFunctions(TestCase):
    def setUp(self):
        pass

    def test_if_one_third_activated_true(self):
        synapse_values_of_a_neuron = [
            -1, -1, -1, -1, 0, 0, 0.2, 0.3, 0.4
        ]
        is_activated = if_one_third_synapses_activated(
            synapse_values_of_a_neuron=synapse_values_of_a_neuron
        )
        self.assertEqual(is_activated, True)

    def test_if_one_third_activated_false(self):
        synapse_values_of_a_neuron = [
            -1, -1, -1, -1, 0, 0, 0, 0, 0.4
        ]
        is_activated = if_one_third_synapses_activated(
            synapse_values_of_a_neuron=synapse_values_of_a_neuron
        )
        self.assertEqual(is_activated, False)