# C2_W3 Notes

## Bias (under-fit) & Variance (over-fit)

Generally, given enough data, a more complex model (e.g. higher order polynomial) will:
- reduce Jtrain (cost or error of training set) -> too complex -> can over-fit the training data == Variance
- up to a point, reduce Jcv (cost or error of Cross Validation set) [if order of polynomial too high -> Jcv starts increasing again].

Too-simple model (not enough Features) OR a model with not enough data -> under-fit == Bias.

In some NN cases, can have both Bias and Variance. For example, if over-fitting some test cases, but under-fitting others.

### Regularization term (of linear regression)

This is to try and reduce over-fitting (Variance).

lambda = how much regularization.

- small lambda -> higher Variance (over-fit)
- large lamda -> high Bias (under-fit)

Jtrain increase with lambda.
Jcv decreases with lamda, up to a point, then starts increasing again.

### Evaluate whether has high Bias or Variance: use a Baseline performance

Baseline performance:
- accuracy of Human OR Other Algorithm OR a Domain-expert guess (!)

- Jtrain (Training error) - Baseline -> small, then Variance. high, then Bias.
- Jcv (Cross Validation error) - Baseline -> high, then Variance. small, then Bias.

## Learning curves

- plot Mtrain (training set size) vs Error (Jcv, Jtrain)

### High Bias (under-fit)
-- as Mtrain increases -> (Jtrain increases to a point, Jcv decreases to a point)
Intuitively, with more cases, it is harder for the model to fit all the training examples perfectly.
-- Jcv typically > Jtrain (unseen vs seen)
-- can have too much data, for a too-simple model
-- so, a high-Bias (under-fit) model will NOT benefit from adding more data!

### High Variance: (over-fit)

-- as Jtrain increases, Jtrain increases. Jcv decreases.
--- BUT Jcv >> Jtrain.
-- Variance: increasing the Mtrain CAN help, up to a point

### caveat: Learning curves are expensive to calculate

- need to use several runs, with different training set sizes...

## Improving a Learning Algorithm

Options:
- Increase Mtrain (get more training examples) -> helps if has High Variance (over-fit)
- Simplify the model (less features OR lower polynomial order) -> need less data -> helps if has High Variance (over-fit)
- Complexify the model (more features OR higher polynomial order) -> helps if has High Bias (under-fit)
- Decrease lambda (the Regularization) -> increases over-fit -> helps if has High Bias (under-fit)
- Increase lambda (the Regularization) -> reduces over-fit -> helps if has High Variance (over-fit)

OR inverted:

### High Variance measures: [more common with NN]
- Increase Mtrain (get more training examples) -> helps if has High Variance (over-fit)
- [NOT true for NN!] Simplify the model (less features OR lower polynomial order) -> need less data -> helps if has High Variance (over-fit)
- Increase lambda (the Regularization) -> reduces over-fit -> helps if has High Variance (over-fit)

### High Bias measures:
- Complexify the model (more features OR higher polynomial order) -> helps if has High Bias (under-fit)
- Decrease lambda (the Regularization) -> increases over-fit -> helps if has High Bias (under-fit)

Do NOT reduce Mtrain (do NOT throw away training examples!)

## Bias vs Variance trade-off

Linear regression: there is a trade-off between Bias and Variance.
NN: are low-bias machines (they almost always fit data well)
1 - Jtrain high - Bias (under-fit) -> make NN bigger
2 - Jcv high? - Variance (over-fit) -> get more data (Mtrain) -> retrain (go to 1)

Limits: hardware (limits NN size) + Data

NN: generally a large NN will NOT over-fit, compared to smaller NN, so long as lambda chosen!
- cost is performance (training time)

```py
layer_1 = Dense(units=25, activation="relu", kernel_regularizer=L2(0.01)) # param to L2 is lambda, the regularization
layer_2 = Dense(units=15, activation="relu", kernel_regularizer=L2(0.01))
layer_3 = Dense(units=1, activation="linear", kernel_regularizer=L2(0.01))
```

## Precision vs Recall (tradeoff)

Precision = TP / (TP + FP)

Recall = TP / (TP + FN)

Analogy: Fish in a lake. Catch 80/100 fish -> high Recall, but if also 80 rocks -> poor Precision.

### How to choose (there is a trade-off): F1 score ('harmonic mean')

F1 score = 2 * P * R / (P + R)
# penalizes if P or R too small) = the 'harmonic mean'

### F2 score (more weight to Recall)

Depends on the Application:
- e.g. classifying to detect a rare disease that is cheap to treat -> may prefer higher R rather than P. (avoid false negatives).

The F2 score is the weighted harmonic mean of the precision and recall (given a threshold value). Unlike the F1 score, which gives equal weight to precision and recall, the F2 score gives more weight to recall than to precision.

F2 score = 5 * P * R / (4*P + R)
# penalizes if higher P -> so more weight to Recall
