"""

"""

"""
Layer 1 -> Layer 2 -> Layer 3
After one cycle,
Get Activations of Layer 2
What neurons were active for this layer_2 activation
Increment the synapse between that layer_1 neuron and this layer_2 neuron

if a synapse is activated,
    
    L2_1 L2_2 L2_3
L1_1 0.1  -1   -1
L1_2 -1   0.0  0.0
L1_3 -1   -1   0.1

Activated: [0, 0, 1]

"""