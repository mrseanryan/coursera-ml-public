# multi *label*
# so, each training item can have more than 1 expected output

import tensorflow as tf
import numpy as np

Y = np.array([
    [1, 0, 1], # car + pedestrian
    [1, 0, 1], # car + bus
    [0, 1, 1], # pedestrian + bus
])

# could train 3 x neural nets, 1 for each label
# OR 1 x neural net, with 3 outputs.  sigmoid activations on the output layer.
