# Course 2, Week 2 Notes

## Choosing an activation function

why needed: if all layers use linear activation, then the overall network behaves only like Linear Regression (so making the neural net un-necessary!).

(a linear function of a linear function, is itself a linear function)

### Hidden layer
- use ReLU activation function! - faster than Sigmoid
- is flat only in one part (to left of Y axis, for negative values) -> so optimizes faster than Sigmoid which has 2 flat parts (at either end)

### Output layer:
#### Binary classification

Loss function = BinaryCrossentropy (logistic loss)

Activation function = Sigmoid (can be easily mapped to binary output, by picking a threshold)
- # sigmoid is: 1 / (1 + e^-z)

#### Regression (predicating a number, not a category)

Activation function = linear
Loss function = MeanSquaredError

If Y always negative -> use ReLU Activation function

### Other options for Activation function

#### alt: ReLU (Rectified Linear Unit)
- g(z) = max(0,z)
- used in image classification? (hidden layer anyway)

#### alt: Linear ("no activation function")
g(z) = z

#### alt: Softmax [multiclass]

- for multiclass classification - OUTPUT layer
- N outputs (a probability for each class)

For N classes:

- a1 = e^z1 / ( e^z1 + e^z2 + e^z3 + e^z4 ... + e^zN )
- a2 = e^z2 / ( e^z1 + e^z2 + e^z3 + e^z4 ... + e^zN )
...
- aN = e^zN / ( e^z1 + e^z2 + e^z3 + e^z4 ... + e^zN )

- softmax for 2 classes -> same as logistic regression!

Loss function = SparseCategoricalCrossentropy.
- sparse: since in Y we expect only 1 class to be represented (even though we have probabilities for all N classes!)

##### SparseCategorialCrossentropy or CategoricalCrossEntropy
Tensorflow has two potential formats for target values and the selection of the loss defines which is expected.
- SparseCategorialCrossentropy: expects the target to be an integer corresponding to the index. For example, if there are 10 potential target values, y would be between 0 and 9. 
- CategoricalCrossEntropy: Expects the target value of an example to be one-hot encoded where the value at the target index is 1 while the other N-1 entries are zero. An example with 10 potential target values, where the target is 2 would be [0,0,1,0,0,0,0,0,0,0].

#### alt: LeakyReLU

## Layer Summary

- Binary classification -> hidden = ReLU, output = Sigmoid (Logistic Regression) -> a probability -> a threshold -> 0 or 1
- Multiclass classification -> hidden = ReLU, output = Softmax -> one probability for each class.

Output layer: has 1 node for each class.

### Layer types

- Dense - each neuron output is a function of ALL the inputs to that layer
- Convolutional - (used in image recognition) - a neuron output is a function of SOME of the inputs to that layer
-- image processing: each neuron looks at just part of the image (the parts may overlap)
-- faster
-- needs less training data (less prone to over-fitting)

### Softmax Activation function for multiclass classification:
- unlike ReLU and Sigmoid, the softmax spans multiple outputs.
- From C2_W2_Multiclasss_TF lab: *the values have been coordinated between the units. It is not sufficient for a unit to produce a maximum value for the class it is selecting for, it must also be the highest value of all the units for points in that class. This is done by the implied softmax function that is part of the loss function (SparseCategoricalCrossEntropy). Unlike other activation functions, the softmax works across all the outputs.*

## Training
### Gradient descent - to minimise the loss function

- prone to local optimization

- back propogation of errors -> learn better parameters (done by Tensorlow fit())

### Alt: Adam optimizers
- faster for neural net training, than gradient descent
