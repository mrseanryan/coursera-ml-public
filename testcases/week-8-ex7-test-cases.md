# week 8 - ex7 test cases

% test case - three examples, two features, two centroids
findClosestCentroids([0 1; 5 5; -1 8], [7 6; -2 2])

% results:
ans =

2
1
2

% ====================

% test case - 10 examples, five features, four centroids
X = reshape(sin(1:50), 10, 5)
cent = X(7:10,:)
idx = findClosestCentroids(X, cent)

% results
idx =
   1
   2
   3
   4
   4
   1
   1
   2
   3
   4

% ======================

computeCentroids([0 1; 5 5; -1 8], [2 1 2]', 2)

ans =

5.000000000000000 5.000000000000000

-0.500000000000000 4.500000000000000

% ======================

computeCentroids([magic(3) ; magic(3) ; [8 1 7]], [1 2 3 2 3 1 1]', 3)

ans =

6.666666666666667 3.666666666666667 5.000000000000000

5.500000000000000 3.000000000000000 6.500000000000000

3.500000000000000 7.000000000000000 4.500000000000000

% ======================

The random initialization of the centroids is not required to pass the grader for ex7, 
but the compressed image from running ex7.m will come out as uniform grey 
if you forget to implement kMeansInitCentroids.
Note that the code needed is explicitly given in ex7.pdf. 
We include it here just to remind people to fill in the code. 
Of course it is supposed to be random (well, pseudo-random), 
but PRNG implementations let you set the initial seed to a fixed value 
for exactly this kind of situation: in a test case, you want the results to be predictable. 
Well, either that or you have to work harder and do some kind of 
statistical analysis on your results to confirm that they have the correct properties.

% ======================

rand('state', 42);
kMeansInitCentroids([1:10 ; 11:20]', 3)

ans =

7 17

2 12

5 15

Your mileage may vary, but as long as the outputs are not all zero, you are probably in good shape.

% ======================

format long
[U, S] = pca(sin([0 1; 2 3; 4 5]))

U =

-0.654347329763442 -0.756194136469897

-0.756194136469897 0.654347329763442

S =

0.795511951488468 0

0 0.220186670785774
% ======================

format long
projectData(sin([0 1 2; 3 4 5; 6 7 8]), magic(3), 2)

ans =

6.161602661726416 12.391031765470618

-4.977144520097401 -12.273210940448021

3.693068797058487 11.909741715005456

% ======================
Test case for recoverData():
Q = reshape([1:15],5,3)
recoverData(Q, magic(5), 3)

ans =
   172   130   183   291   394
   214   165   206   332   448
   256   200   229   373   502
   298   235   252   414   556
   340   270   275   455   610
% ======================



