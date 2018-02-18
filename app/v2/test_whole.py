"""
"""

"""

I want to create three layers of neuron

Layer 1 has 100 neurons
Layer 2 has 200 neurons
Layer 3 has 300 neurons

Dilution 
    Layer 1 - Layer 2: 50%
    Layer 2 - Layer 3: 100%
    
Input array will be supplied to Layer 1.
Output array is the output of Layer 3.

Inputs -> [
            [..]..
          ]
Output -> [..]

Constraints:
    Input.length == Layer1.length

Hebbian: Enabled


Process:
    
    x: Synapse=CreateSynapseMatrix(Layer1,Layer2,Dilution)
    y: Synapse=CreateSynapseMatrix(Layer2,Layer3,Dilution)
    
    Layer1
    .previous_layer=None
    .next_layer=Layer2
    .master_incoming_synapses=None
    .master_outgoing_synapses=x
    .current_incoming_synapses=None
    .current_outgoing_synapses=None
    .neurons=[..] <activated_values>
    
    
    Layer2
    .previous_layer=Layer1
    .next_layer=Layer3
    .master_incoming_synapses=x
    .master_outgoing_synapses=y
    .current_incoming_synapses=None
    .current_outgoing_synapses=None
    .neurons=[..] <activated_values>
    
    
    Layer3
    .previous_layer=Layer2
    .next_layer=None
    .master_incoming_synapses=y
    .master_outgoing_synapses=None
    .current_incoming_synapses=None
    .current_outgoing_synapses=None
    .neurons=[..] <activated_values>
    
    Layer1
    .set_activated_values(activated_values)
    .allow_activated_values_to_travel_synapses()
        .get_activated_values()
        .get_master_outgoing_synapses()
        .multiply_activated_values_with_master_outgoing_synapses()
        .set_it_to_current_outgoing_synapses()
        .allow_it_to_pass_to_next_layer()
    
    Layer2
    .compute_activation_values_from_incoming_synapse_matrix()
    .set_it_to_neuron_values()
    .allow_activated_values_to_travel_synapses()
        .get_activated_values()
        .get_master_outgoing_synapses()
        .multiply_activated_values_with_master_outgoing_synapses()
        .set_it_to_current_outgoing_synapses()
        .allow_it_to_pass_to_next_layer()
    
    Layer3
    .compute_activation_values_from_incoming_synapse_matrix()
    .set_it_to_neuron_values()
    .allow_activated_values_to_travel_synapses()
        .get_activated_values()
        .get_master_outgoing_synapses()
        .multiply_activated_values_with_master_outgoing_synapses()
        .set_it_to_current_outgoing_synapses()
        .allow_it_to_pass_to_next_layer() <calls for EXIT since there are no next layers>
        
        
Methods extracted:
    
    compute_activation_values_from_incoming_synapse_matrix()
        => synapse_values_of_a_neuron
            => incoming_synapses[0:, neuron_index]
        => is_activated(synapse_values_of_a_neuron)
        => aggregate it
        => return aggregate
        
    
    allow_activated_values_to_travel_synapses()
        => ...
    
    multiply_activated_values_with_master_outgoing_synapses()
        => activated_values(dotmul)outgoing_synapses
    
    
    allow_it_to_pass_to_next_layer()
        => self.next_layer.current_ingoing_synapses = self.current_outgoing_synapses
    
    
    
"""

"""



"""