week-6 ex5 test cases
===

ref [https://www.coursera.org/learn/machine-learning/discussions/all/threads/O25D0QykEeWZSyIAC5bWOg]

ex5 test case linearRegCostFunction
Tom MosherMentorWeek 6 · a year ago · Edited
Here is a test case for linearRegCostFunction().

```
X = [[1 1 1]' magic(3)];
y = [7 6 5]';
theta = [0.1 0.2 0.3 0.4]';
[J g] = linearRegCostFunction(X, y, theta, ?)

%--- results based on value entered for ? (lambda)
--------------------------
lambda = 0  |   lambda = 7
--------------------------
J = 1.3533  |   J = 1.6917
g =         |   g = 
   -1.4000  |      -1.4000
   -8.7333  |      -8.2667
   -4.3333  |      -3.6333
   -7.9333  |      -7.0000
```

Here is a test case with just one training example in X.

helps with debugging problems in learningCurve()

```
X = [1 2 3 4];
y = 5;
theta = [0.1 0.2 0.3 0.4]';
[J g] = linearRegCostFunction(X, y, theta, 7)

% results
J =  3.0150
g =
  -2.0000
  -2.6000
  -3.9000
  -5.2000
```

======
learning curve
===
Do use regularization to train each system.

Do not use regularization when you measure the training or validation errors.

Calculate the training set error on the same training examples you used for training.

Calculate the validation error on the entire validation set.

Here is a link to a test case.

[https://www.coursera.org/learn/machine-learning/discussions/qJHffPEFEeSUBCIAC9QURQ/replies/HwRvRvFBEeSUBCIAC9QURQ/comments/4Fe-AfFYEeSkXCIAC4tJTg]

```
X = [ones(5,1) reshape(-5:4,5,2)];
y = [-2:2]';
Xval=[X;X]/10;
yval=[y;y]/10;
[et ev] = learningCurve(X,y,Xval,yval,1)
```

exp_theta =
  -2.00000
   0.00000
   0.00000


And here is the theta value for i=2:

theta =

  -0.50000
   0.25000
   0.25000

=========================

Linear Regression - no poly features - lambda = 0.000000
# Training Examples     Train Error     Cross Validation Error
        1               0.000000        205.121096
        2               0.000000        110.300366
        3               3.286595        45.010231
        4               2.842678        48.368911
        5               13.154049       35.865165
        6               19.443963       33.829962
        7               20.098522       31.970986
        8               18.172859       30.862446
        9               22.609405       31.135998
        10              23.261462       28.936207
        11              24.317250       29.551432
        12              22.373906       29.433818


=============
X = [ones(5,1) reshape(-5:4,5,2)];
y = [-2:2]';
Xval=[X;X]/10;
yval=[y;y]/10;
[et ev] = learningCurve(X,y,Xval,yval,1)

exp_et =

   0.000000
   0.031250
   0.013333
   0.005165
   0.002268

exp_ev =

  3.0000e-002
  5.3125e-003
  6.0000e-004
  9.2975e-005
  2.2676e-005

  ===============================

  Test Case for polyFeatures()
Tom MosherMentorWeek 6 · a year ago
Here is a test case for the polyFeatures() function

```
>> polyFeatures([1:3]',4)
exp_ans =
    1    1    1    1
    2    4    8   16
    3    9   27   81
```

 Using the element-wise exponentiation operator .^ is the key.

 X_poly = bsxfun(@(a,b) a.^b, X, 1:p);


 =============================

 Test Case for validationCurve()
Tom MosherMentorWeek 6 · a year ago · Edited
Here is a test case for the validationCurve() function.

Note: you may get some "division by zero" warnings. This is normal.



1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
X = [1 2 ; 1 3 ; 1 4 ; 1 5]
y = [7 6 5 4]'
Xval = [1 7 ; 1 -2]
yval = [2 12]'
[lambda_vec, error_train, error_val] = validationCurve(X,y,Xval
    ,yval )
% results:
lambda_vec =
    0.00000
    0.00100
    0.00300
    0.01000
    0.03000
    0.10000
    0.30000
    1.00000
    3.00000
   10.00000
error_train =
   0.00000
   0.00000
   0.00000
   0.00000
   0.00002
   0.00024
   0.00200
   0.01736
   0.08789
   0.27778
error_val =
   0.25000
   0.25055
   0.25165
   0.25553
   0.26678
   0.30801
   0.43970
   1.00347
   2.77539
   6.80556
===============

keywords: test case validationcurve
 3 Upvote
 · 
Follow 18
 · 

```
X = [1 2 ; 1 3 ; 1 4 ; 1 5]
y = [7 6 5 4]'
Xval = [1 7 ; 1 -2]
yval = [2 12]'
[lambda_vec, error_train, error_val] = validationCurve(X,y,Xval,yval )

% results:
lambda_vec =
    0.00000
    0.00100
    0.00300
    0.01000
    0.03000
    0.10000
    0.30000
    1.00000
    3.00000
   10.00000

error_train =

   0.00000
   0.00000
   0.00000
   0.00000
   0.00002
   0.00024
   0.00200
   0.01736
   0.08789
   0.27778

error_val =

   0.25000
   0.25055
   0.25165
   0.25553
   0.26678
   0.30801
   0.43970
   1.00347
   2.77539
   6.80556

```

