# test cases for week 3

# ex 2

================
ref:
[https://www.coursera.org/learn/machine-learning/discussions/all/threads/JHorKeknEeS0tyIAC9RBcw]

## Sigmoid Function Unit Tests

sigmoid(1200000)
expected_ans = 1

sigmoid(-25000)
expected_ans = 0

sigmoid(0)
expected_ans = 0.5

sigmoid([4 5 6])
exp_ans = 0.9820 0.9933 0.9975

sigmoid(magic(3))
exp_ans =
0.9997 0.7311 0.9975
0.9526 0.9933 0.9991
0.9820 0.9999 0.8808

sigmoid(eye(2))
ans =
0.7311 0.5000
0.5000 0.7311

================
#Predict() unit tests

X = [1 1 ; 1 2.5 ; 1 3 ; 1 4]
theta = [-3.5 ; 1.3]
predict(theta, X)

% results
exp_ans = [   0;   0;   1;1]

predict([0.3 ; 0.2], [1 2.4; 1 -17; 1 0.5])
exp_ans =[   1;   0;   1]

=================
#ex2 test cases for costFunction() and costFunctionReg()

ref:
[https://www.coursera.org/learn/machine-learning/discussions/weeks/3/threads/tA3ESpq0EeW70BJZtLVfGQ]

X = [ones(3,1) magic(3)];
y = [1 0 1]';
theta = [-2 -1 1 2]';

% un-regularized
[j g] = costFunction(theta, X, y)
% or...
[j g] = costFunctionReg(theta, X, y, 0)

% results
exp_j = 4.6832

exp_g =  [0.31722;  0.87232;  1.64812;  2.23787]

% regularized
[j g] = costFunctionReg(theta, X, y, 3)
% note: also works for ex3 lrCostFunction(theta, X, y, 3)

% results
exp_j = 7.6832

exp_g = [0.31722;   -0.12768;  2.64812;  4.23787]

===================
# from the previous ref but related to costFunction:

X = [ones(4,1) magic(4)];
y = [1 0 1 0]';
[j g] = costFunction([-1 2 -3 4 -5]', X, y)

% results
j =  22.000
g = [  -0.25000;  -5.25000;   1.25000;   1.50000; -6.00000];

