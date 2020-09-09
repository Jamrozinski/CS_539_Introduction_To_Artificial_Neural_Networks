#!/usr/bin/env python3

"""mp_neuron.py: naive implementation of the McCulloch-Pitts Neuron Model"""

__author__ = "Peter S Jamrozisnki"
__copyright__ = "Copyright 2020, Peter S Jamrozinski"

########################################################################

from .neuron import all

class mp_neuron(neuron):
    def __init__(self):
        super().__init__()

    def weightedSum(self, v_inputs, v_weights):

        weightedSum = 0

        if not isinstance(v_inputs, list) or not isinstance(v_weights, list):
            raise TypeError("input must be of type 'list'")
        elif len(v_inputs) != len(v_weights):
            raise Exception("size of input list but equal size of weights list")
        else:
            for i,w in zip(v_inputs, v_weights):
                weightedSum += i*w

        return weightedSum

    def activation(self, v_inputs, v_weights, threshold):
        weightedSum = self.weightedSum(v_inputs, v_weights)

        activation = 0

        if (weightedSum >= threshold):
            activation = 1

        return activation


