from unittest import TestCase
import numpy
from app.v2.utilities import create_layer, set_layer_by_name, \
    get_layer_by_name, connect, get_synapse_values_for_cell_from_firstlayer, get_synapse_value, \
    get_synapse_values_for_cell_from_secondlayer


class TestUtilities(TestCase):
    def setUp(self):
        pass

    def test_create_layer(self):
        number_of_neurons = 30
        layer = create_layer(
            layer_name='test_layer_1',
            number_of_neurons=number_of_neurons
        )
        self.assertEqual(isinstance(layer, numpy.ndarray), True)
        self.assertEqual(len(layer), 30)

    def test_set_get_layer_by_name(self):
        layer = numpy.ndarray((10, ))
        set_layer_by_name(
            layer=layer,
            layer_name='test_1'
        )
        layer_fetched = get_layer_by_name(
            layer_name='test_1'
        )
        self.assertEqual(len(layer), len(layer_fetched))

    def test_connect(self):
        layer_1 = create_layer(
            layer_name='test_connect_layer1',
            number_of_neurons=100
        )
        layer_2 = create_layer(
            layer_name='test_connect_layer2',
            number_of_neurons=500
        )
        synapse = connect(
            layer_1_name='test_connect_layer1',
            layer_2_name='test_connect_layer2',
            dilution=50,
            initial_value=0.1
        )
        synapse_values_for_ceLL1_layer1 = get_synapse_values_for_cell_from_firstlayer(
            layer_1_name='test_connect_layer1',
            layer_2_name='test_connect_layer2',
            cell_index=0
        )
        number_of_existent_connections_average = 0
        for i in range(0, 500):
            number_of_existent_connections = 0
            synapse_values_for_cellX_layer2 = get_synapse_values_for_cell_from_secondlayer(
                layer_1_name='test_connect_layer1',
                layer_2_name='test_connect_layer2',
                cell_index=i
            )
            for synapse in synapse_values_for_cellX_layer2:
                if synapse != -1:
                    number_of_existent_connections += 1
            number_of_existent_connections_average += number_of_existent_connections
        print(f"Average number of connections from layer 1 to layer 2 cell: "
              f"{number_of_existent_connections_average/500}")
        # Dilution is 50,
        # => 1 cell of layer 1 is connected to 50% of layer 2
        # => 1 cell of layer 1 is connected to 250 cells of layer 2
        self.assertEqual(len(synapse_values_for_ceLL1_layer1), 500)

        number_of_connections_in_created_matrix = 0
        connection_indices = []
        for index, synapse in enumerate(synapse_values_for_ceLL1_layer1):
            if synapse != -1:
                number_of_connections_in_created_matrix += 1
                connection_indices.append(index)

        self.assertEqual(number_of_connections_in_created_matrix, 250)

        for connected_index in connection_indices:
            synapse_value = get_synapse_value(
                layer_1_name='test_connect_layer1',
                layer_2_name='test_connect_layer2',
                layer_1_cell_index=0,
                layer_2_cell_index=connected_index
            )
            self.assertEqual(synapse_value, 0.1)
