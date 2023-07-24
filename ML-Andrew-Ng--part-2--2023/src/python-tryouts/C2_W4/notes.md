# C2_W4 Notes

## Decision Trees

- literally, a tree of decisions, forking from root towards 'leaves'

- each node is a decision, based on a Feature
- features MAY be repeated across nodes (except for binary features at that sub-tree)

### Learning

- this node = root node

Recursive algorithm:
- start at 'this' node, with ALL examples
- decide which feature is in the next node:
-- calculate Information gain for all possible features
-- pick the feature with the highest information gain
--> pick the "purest"

- split dataset according to the selected feature - create left and right brances

- keep recursing until stopping criteria is met, for this sub-tree

#### Stopping criteria (for this sub-tree)

Can be one or combination of:
- a node reaches min % for +ve case, or for 1 class
- max tree level depth (number of hops from root node)
-- more levels == more complex model -> can lead to over-fitting (Variance). OSS libraries can pick max-levels for you.
- when improvements in Information Gain (purity score) are below a threshold
- when number of examples in a node is below a threshold

### Impurity (Entropy)

Entropy H is a measure of impurity.
Entropy shows the degree of predictability of an event.

- p1 = fraction of examples at a node, that are +ve
- H(p1) = entropy - if 50/50 is 1 (maximally impure!) (max probability! IS useful information)
- if ALL +ve or ALL -ve -> H(p1) = 0 (is pure!) (lowest probability - is NOT useful information)

p0 = 1 - p1

H(p1) = - p1 x log<2>(p1) - p0 x log<2>(p0)
      = - p1 x log<2>(p1) - (1 - p1)log<2>(1 - p1)

- also used: the Gini criteria (Gini co-efficient?)

### Choosing a split: Information Gain

(minimising entropy)

- use weigthed average of entropy, since many examples are more important than few examples

For each node at next level:
Information Gain = Entropy(root node) - (weighted Entropy(next node))
= H(root node) - ( +ve-left/total-root * H(left) ) + ( +ve-right/total-root * H(+ve-right) )
= H(p1-root) - ( Wleft x H(p1-left) + Wright x H(p1-right) )

- pick the node with the Highest information gain

## Categorical Features - Features with multiple values -> one-hot encode new features

Example: Ear shape can be one of [Pointy, Oval, Floppy]
Can model this as 3 new one-hot encoded features (since they are mutually exclusive)
- Pointy, Oval, Floppy

In general, if a categorical feature can take on k values,
then replace it by creating k binary features.

Can also use one-hot enconding for NN or Linear Regression or Logistic Regression training.

### Benefits of one-hot encoding:
- simpler + faster.
- One-hot encoding ensures that machine learning does not assume that higher numbers are more important!
- why faster to train: a format that can be more easily processed by machine learning algorithms. We can reduce bias (under-fit), improve accuracy, and improve interpretability

## Splitting on a continuous variable

e.g. weight: is this a cat?

- pick a treshold
- calc the information gain
- repeat until have the best threshold

Can sort the training examples, and try a threshold in-between each example -> the best possible threshold, for that training set.
- can that overfit?

# Regression (to predict a number) with Decision Trees

- try to predict a continuous variable (like weight)

- use a decision tree to classify into smaller groups
- at bottom of the tree, take the average for that node = the prediction

## How to pick - reduce variance

Rather than information gain, we choose to reduce variance of the predicted variable.
- weighted average variance for each node (each side of the next split)
- pick the feature that gives average weight with the lowest variance

For each feature:

Reduction in Variance = Variance (root node) - ( p-left/total-root * variance-left +  p-right/total-root * variance-right )

- pick the feature with the largest reduction in variance

## Stopping criteria

- min threshold for reducing variance
- max tree levels

# Tree Ensembles

Decision Trees are prone to small changes in the input.
- changing 1 training example can result in a very different decision tree!

This can be mitigated via ensembles.

A Tree Ensemble == a set of Decision Trees

- each tree has a different feature at root
- predict by voting -> majority decides

## Sampling the training set, with replacement

- pick a series of random training examples
- there can be repeated duplicate, hence 'replacement'

This new training set is similar to the full training set, but different enough to produce a slightly different decision tree.

Tree count = Size of B = about 100
= a Bagged decision tree

## Random forest algorithm

Ramdonmizing the feature choice
- at each node, only allow algorithm to choose a random *subset*, size k, of the available features.
- k = sqrt(n)

## Boosted trees

- Bagged decision tree, BUT built more likely to pick *mis-classified* training examples, from the previously trained trees.

Implementation:

- XGBoost - eXtreme Gradient Boosting
- fast, built-in regularization to avoid overfitting

# When to use Decision Trees

- tabular/structured data
- NOT for unstructured data (images, audio, text) -> NN better for that

## Advantages
- fast to train -> you can iterate faster
- human interpretable (at least, small decision trees)

## When to use NN

- works on ALL data (structured OR un-structured)
- slower to train
- DOES work with transfer learning (pre-training)
- easier to string together multiple NNs (you can train them all together, unlike decision trees)
