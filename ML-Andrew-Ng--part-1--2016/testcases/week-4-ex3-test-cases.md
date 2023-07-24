ex3 test cases
===

Ex3 Test Cases
Chirag UttamsinghMentorGeneral Discussion · 10 months ago · Edited by moderator
Here are the test cases for ex3 by Tom Mosher:

lrCostFunction:
```
% input
theta = [-2; -1; 1; 2];
X = [ones(5,1) reshape(1:15,5,3)/10];
y = [1;0;1;0;1] >= 0.5;       % creates a logical array
lambda = 3;
[J grad] = lrCostFunction(theta, X, y, lambda)

% results
exp_J =  2.5348
exp_grad = [ 0.14656; -0.54856; 0.72472; 1.39800]
```

Note: your cost function must return the gradient as a column vector (size n x 1), NOT as a row vector (1 x n).

============================
oneVsAll:
====

```
%input:
X = [magic(3) ; sin(1:3); cos(1:3)];
y = [1; 2; 2; 1; 3];
num_labels = 3;
lambda = 0.1;
[all_theta] = oneVsAll(X, y, num_labels, lambda)
%output:
all_theta =
  -0.559478   0.619220  -0.550361  -0.093502
  -5.472920  -0.471565   1.261046   0.634767
   0.068368  -0.375582  -1.652262  -1.410138
```

================================
predictOneVsAll
===

```
% input:
all_theta = [1 -6 3; -2 4 -3];
X = [1 7; 4 5; 7 8; 1 4];
predictOneVsAll(all_theta, X)
%output:
ans =
   1
   2
   2
   1
```

Note: your prediction function should NOT include any use of a fixed threshold. Select the classifier with the maximum output.

=====

predict:

```
Theta1 = reshape(sin(0 : 0.5 : 5.9), 4, 3);
Theta2 = reshape(sin(0 : 0.3 : 5.9), 4, 5);
X = reshape(sin(1:16), 8, 2);
p = predict(Theta1, Theta2, X)
% you should see this result
exp_p = [
  4;
  1;
  1;
  4;
  4;
  4;
  4;
2 ]
  ```

  Note: your prediction function should NOT include any use of a fixed threshold. Select the classifier with the maximum output.
