import numpy as np
import math
from typing import List
import random

TwoDimensionalArray = np.ndarray
OneDimensionalArray = np.ndarray


class HelperMixin:

    def __init__(
            self,
            store_manager,
            layer
    ):
        self.store = store_manager
        self.layer = layer

    def get_synapse_values_for_cell(
            self,
            in_or_out: str,
            cell_index: int
    ) -> OneDimensionalArray:
        if in_or_out == 'IN':
            return self.store.get_current_incoming_synapses()[0:, cell_index]
        elif in_or_out == 'OUT':
            return self.store.get_current_outgoing_synapses()[cell_index]
        raise Exception

    @staticmethod
    def get_random_numbers(
            number: int,
            from_: int,
            to_: int
    ) -> List[int]:
        return random.sample(
            list(
                range(from_, to_)
            ), k=number
        )

    def connect(
            self,
            dilution: float or int,
            initial_value: float
    ) -> TwoDimensionalArray:
        layer_1_len = self.layer.size
        layer_2_len = self.layer.next_layer.size
        synapse_matrix: TwoDimensionalArray = np.full(
            (layer_1_len, layer_2_len), dtype='float', fill_value=-1
        )
        # INITIAL: No connections between layer 1 and layer 2 denoted by -1
        number_of_connections: int = int((layer_2_len / 100) * dilution)
        for layer_1_index in range(0, layer_1_len):
            layer_2_indices = self.get_random_numbers(
                from_=0,
                to_=layer_2_len,
                number=number_of_connections
            )
            for layer_2_index in layer_2_indices:
                synapse_matrix[layer_1_index][layer_2_index] = initial_value
        return synapse_matrix

    @staticmethod
    def _multiply_product(
            vector: np.ndarray,
            matrix: np.ndarray
    ):
        resp = []
        for i in range(0, len(vector)):
            resp.append(np.multiply(vector[i], matrix[i]))
        return np.array(resp)

    def multiply_neurons_synapses(
            self,
            neuron_vector: OneDimensionalArray,
            synapse_matrix: TwoDimensionalArray
    ) -> TwoDimensionalArray:
        return self._multiply_product(vector=neuron_vector, matrix=synapse_matrix)

    @staticmethod
    def if_one_third_synapses_activated(
            synapse_values_of_a_neuron: OneDimensionalArray,
            bool_mask: OneDimensionalArray
    ) -> int:
        existent_synapse_count = 0
        activated_synapse_count = 0

        for index, synapse_value in enumerate(synapse_values_of_a_neuron):
            if bool_mask[index]:
                existent_synapse_count += 1
                if synapse_value > 0:
                    activated_synapse_count += 1
        if activated_synapse_count > math.ceil(existent_synapse_count / 3):
            return 1
        return 0

    def apply_activation_function_to_layer(
            self
    ):
        synapse_matrix = self.store.get_current_incoming_synapses()
        bool_mask = self.store.get_existent_synapses_mask(is_incoming=True)
        activation_values = []
        for i in range(0, synapse_matrix.shape[1]):
            is_activated: int = self.if_one_third_synapses_activated(
                                    synapse_matrix[0:, i],
                                    bool_mask[0:, i]
                                )
            activation_values.append(
                is_activated
            )
        return np.array(activation_values)


class StoreManager:
    # Abstraction over storage of matrices - disk, memory.
    _store = {}

    def __init__(
            self,
            layer_name: str,
            is_input_layer: bool,
            is_output_layer: bool,
            previous_layer_name: str = None,
            next_layer_name: str = None
    ):
        self.layer_name: str = layer_name
        self.previous_layer_name: str = previous_layer_name
        self.next_layer_name: str = next_layer_name
        self.activated_values_key: str = None
        self.master_incoming_synapses_key: str = None
        self.master_outgoing_synapses_key: str = None
        self.current_incoming_synapses_key: str = None
        self.current_outgoing_synapses_key: str = None

        self.is_input_layer = is_input_layer
        self.is_output_layer = is_output_layer

        self.activated_values_key = f"Activated_Values_{self.layer_name}"

        self.incoming_synapses_existent_mask_key = f"Incoming_Synapses_Existent_Mask_{self.layer_name}"
        self.outgoing_synapses_existent_mask_key = f"Outgoing_Synapses_Existent_Mask_{self.layer_name}"

        self._is_names_set = False

    def set_names(self):
        if not self.is_input_layer:
            self.current_incoming_synapses_key = f"Current_Incoming_Synapses_to_{self.layer_name}" \
                                                 f"_from_{self.previous_layer_name}"
            self.master_incoming_synapses_key = f"Master_Incoming_Synapses_to_{self.layer_name}" \
                                                 f"_from_{self.previous_layer_name}"

        if not self.is_output_layer:
            self.current_outgoing_synapses_key = f"Current_Outgoing_Synapses_from_{self.layer_name}" \
                                                 f"_to_{self.next_layer_name}"
            self.master_outgoing_synapses_key = f"Master_Outgoing_Synapses_from_{self.layer_name}" \
                                                 f"_to_{self.next_layer_name}"

        self._is_names_set = True

    def set_neuron_activated_values(
            self,
            neuron_values: OneDimensionalArray
    ) -> None:
        self._store[self.activated_values_key] = neuron_values

    def get_neuron_activated_values(
            self
    ) -> OneDimensionalArray:
        return self._store.get(self.activated_values_key)

    def set_master_incoming_synapses(
            self,
            synapse_matrix: TwoDimensionalArray
    ) -> None:
        if not self._is_names_set:
            raise Exception
        self._store[self.master_incoming_synapses_key] = synapse_matrix

    def get_master_incoming_synapses(
            self
    ) -> TwoDimensionalArray:
        if not self._is_names_set:
            raise Exception
        return self._store.get(self.master_incoming_synapses_key)

    def set_master_outgoing_synapses(
            self,
            synapse_matrix: TwoDimensionalArray
    ) -> None:
        if not self._is_names_set:
            raise Exception
        self._store[self.master_outgoing_synapses_key] = synapse_matrix

    def get_master_outgoing_synapses(
            self
    ) -> TwoDimensionalArray:
        if not self._is_names_set:
            raise Exception
        return self._store.get(self.master_outgoing_synapses_key)

    def set_current_incoming_synapses(
            self,
            synapse_matrix: TwoDimensionalArray
    ) -> None:
        if not self._is_names_set:
            raise Exception
        self._store[self.current_incoming_synapses_key] = synapse_matrix

    def get_current_incoming_synapses(
            self
    ) -> TwoDimensionalArray:
        if not self._is_names_set:
            raise Exception
        return self._store.get(self.current_incoming_synapses_key)

    def set_current_outgoing_synapses(
            self,
            synapse_matrix: TwoDimensionalArray
    ) -> None:
        if not self._is_names_set:
            raise Exception
        self._store[self.current_outgoing_synapses_key] = synapse_matrix

    def get_current_outgoing_synapses(
            self
    ) -> TwoDimensionalArray:
        if not self._is_names_set:
            raise Exception
        return self._store.get(self.current_outgoing_synapses_key)

    def set_current_equal_to_master(self):
        if not self._is_names_set:
            raise Exception
        self.set_current_outgoing_synapses(
            synapse_matrix=self.get_master_outgoing_synapses()
        )
        self.set_current_incoming_synapses(
            synapse_matrix=self.get_master_incoming_synapses()
        )

    def set_existent_synapses_mask(self, boolean_mask: np.ndarray, is_incoming: bool):
        if is_incoming:
            self._store[self.incoming_synapses_existent_mask_key] = boolean_mask
        else:
            self._store[self.outgoing_synapses_existent_mask_key] = boolean_mask

    def get_existent_synapses_mask(self, is_incoming: bool) -> np.ndarray:
        if is_incoming:
            return self._store[self.incoming_synapses_existent_mask_key]
        return self._store[self.outgoing_synapses_existent_mask_key]


class Layer(HelperMixin):
    def __init__(
            self,
            name: str,
            size: int,
            is_input_layer: bool,
            is_output_layer: bool
    ):
        self.name: str = name
        self.size: int = size
        self.is_input_layer: bool = is_input_layer
        self.is_output_layer: bool = is_output_layer

        self.state: str = None
        self.previous_layer: Layer = None
        self.next_layer: Layer = None

        self.store = StoreManager(
            layer_name=self.name,
            is_input_layer=self.is_input_layer,
            is_output_layer=self.is_output_layer
        )

        super(Layer, self).__init__(store_manager=self.store, layer=self)

    def connect_with_next_layer(
            self,
            dilution: int,
            next_layer
    ):
        self.next_layer = next_layer
        self.store.next_layer_name = next_layer.name
        self.store.set_names()
        self.next_layer.previous_layer = self
        self.next_layer.store.previous_layer_name = self.name
        self.next_layer.store.set_names()
        synapse_matrix = self.connect(
            dilution=dilution,
            initial_value=0.1
        )

        boolean_mask_existent_synapses = np.ndarray((self.size, self.next_layer.size), dtype='bool')
        for i, _ in enumerate(synapse_matrix):
            for j, _ in enumerate(synapse_matrix[i]):
                if synapse_matrix[i][j] < 0:
                    boolean_mask_existent_synapses[i][j] = False
                else:
                    boolean_mask_existent_synapses[i][j] = True

        self.store.set_existent_synapses_mask(
            boolean_mask=boolean_mask_existent_synapses,
            is_incoming=False
        )

        self.store.set_master_outgoing_synapses(
            synapse_matrix=synapse_matrix
        )

        next_layer.store.set_master_incoming_synapses(
            synapse_matrix=synapse_matrix
        )

        next_layer.store.set_existent_synapses_mask(
            boolean_mask=boolean_mask_existent_synapses,
            is_incoming=True
        )

        self.store.set_current_equal_to_master()
        next_layer.store.set_current_equal_to_master()

    def calculate_activation_value(
            self
    ) -> None:
        activation_values = self.apply_activation_function_to_layer()
        self.store.set_neuron_activated_values(activation_values)

    def allow_neuron_firings_to_pass(self):
        # multiply activated values, master outgoing synapse matrix
        effected_synapse_matrix = self.multiply_neurons_synapses(
            neuron_vector=self.store.get_neuron_activated_values(),
            synapse_matrix=self.store.get_current_outgoing_synapses()
        )
        self.store.set_current_outgoing_synapses(synapse_matrix=effected_synapse_matrix)
        self.next_layer.store.set_current_incoming_synapses(synapse_matrix=effected_synapse_matrix)


if __name__ == '__main__':
    first_layer = Layer(
        name='1',
        size=3,
        is_input_layer=True,
        is_output_layer=False
    )
    second_layer = Layer(
        name='2',
        size=2,
        is_input_layer=False,
        is_output_layer=False
    )
    first_layer.connect_with_next_layer(
        dilution=100,
        next_layer=second_layer
    )
    print(first_layer.store.get_current_outgoing_synapses())
    first_layer.store.set_neuron_activated_values(
        np.array([1, 0, 1])
    )
    first_layer.allow_neuron_firings_to_pass()
    print(first_layer.store.get_current_outgoing_synapses())
    second_layer.calculate_activation_value()
    print(second_layer.store.get_neuron_activated_values())
    second_layer_activated_values = second_layer.store.get_neuron_activated_values()
