week-5-ex4-test-cases
===

ref:
[https://www.coursera.org/learn/machine-learning/discussions/weeks/5/threads/oRjv1jr2EeWm9SIAC5HAew]

ex4 test case for sigmoidGradient()
===

```
sigmoidGradient([[-1 -2 -3] ; magic(3)])
ans =
  1.9661e-001  1.0499e-001  4.5177e-002
  3.3524e-004  1.9661e-001  2.4665e-003
  4.5177e-002  6.6481e-003  9.1022e-004
  1.7663e-002  1.2338e-004  1.0499e-001
```

============================
Test case for ex4 nnCostFunction()
===
Tom MosherMentorWeek 5 · 9 months ago · Edited
Here is a test case for the nnCostFunction() with (and without) regularization:

Enter these values in your console workspace, compare your results with those given.

Test Case with regularization:

```
il = 2;              % input layer
hl = 2;              % hidden layer
nl = 4;              % number of labels
nn = [ 1:18 ] / 10;  % nn_params
X = cos([1 2 ; 3 4 ; 5 6]);
y = [4; 2; 3];
lambda = 4;
[J grad] = nnCostFunction(nn, il, hl, nl, X, y, lambda)
```

output:

```
exp_J = 19.474
exp_grad = [
0.76614;
0.97990;
0.37246;
0.49749;
0.64174;
0.74614;
0.88342;
0.56876;
0.58467;
0.59814;
1.92598;
1.94462;
1.98965;
2.17855;
2.47834;
2.50225;
2.52644;
2.72233 ]
```


Here are the values for all internal variables for the regularized test case:

```
exp_d2 =
   [0.79393,   1.05281;
   0.73674,   0.95128;
   0.76775,   0.93560]

exp_d3 =
   [0.888659   0.907427   0.923305  -0.063351;
   0.838178  -0.139718   0.879800   0.896918;
   0.923414   0.938578  -0.049102   0.960851]

exp_Delta1 =
   [2.298415  -0.082619  -0.074786;
   2.939691  -0.107533  -0.161585]

exp_Delta2 =
   [2.65025   1.37794   1.43501;
   1.70629   1.03385   1.10676;
   1.75400   0.76894   0.77931;
   1.79442   0.93566   0.96699]

exp_z2 =
   [0.054017   0.166433;
  -0.523820  -0.588183;
   0.665184   0.889567]

sigmoidGradient(z2)
exp_ans =
   [0.24982   0.24828;
   0.23361   0.22957;
   0.22426   0.20640]

exp_a2 =
   [1.00000   0.51350   0.54151;
   1.00000   0.37196   0.35705;
   1.00000   0.66042   0.70880]

exp_a3 =
   [0.88866   0.90743   0.92330   0.93665;
   0.83818   0.86028   0.87980   0.89692;
   0.92341   0.93858   0.95090   0.96085]
```

Test case *without* regularization (uses same data, but 0 for lambda):
===
```
il = 2;              % input layer
hl = 2;              % hidden layer
nl = 4;              % number of labels
nn = [ 1:18 ] / 10;  % nn_params
X = cos([1 2 ; 3 4 ; 5 6]);
y = [4; 2; 3];
lambda = 4;

>> [J grad] = nnCostFunction(nn, il, hl, nl, X, y, 0)
J =  7.4070
grad =
   0.766138
   0.979897
  -0.027540
  -0.035844
  -0.024929
  -0.053862
   0.883417
   0.568762
   0.584668
   0.598139
   0.459314
   0.344618
   0.256313
   0.311885
   0.478337
   0.368920
   0.259771
   0.322331
```

=====================
Values for Delta1 and Delta2 (the unregularized gradient, from tutorial Step 5 and Step 6) - truncated to 3 decimal places, prior to scaling by 1/m.
====

```
Delta1 = 
  2.298 -0.082 -0.074
  2.939 -0.107 -0.161

Delta2 =
  2.650  1.377  1.435
  1.706  1.033  1.106
  1.754  0.768  0.779
  1.794  0.935  0.966

```
