#week-7-ex6 test cases

ex6 Test Case for gaussianKernel()

gaussianKernel([1 2 3], [2 4 6], 3)

% result
ans =  0.45943



% Verify that the same point returns 1
>> gaussianKernel([1 1], [1 1], 1)

ans =
     1


% Verify that disimilar points return 0 (or close to it)
>> gaussianKernel([1 1], [100 100], 1)

ans =
     0


% ============================
Test result for dataset3Params()

For a quick test of dataset3Params(), here are the error values when running ex6.m and holding C fixed at 0.3 and evaluating all eight values of sigma:

0.565000      % for sigma = 0.01
0.060000   
0.035000   
0.060000   
0.105000   
0.180000   
0.185000   
0.185000     % for sigma = 30

You may occasionally see some slight variation from these values, due to the random factors used by svmTrain().

% =============================
ex6: Test case for processEmail()

Here is a test case for the processEmail() function:

word_indices  = processEmail('ab abov abil ab footwork ab ab')
% output:
==== Processed Email ====
ab abov abil ab footwork ab ab 
=========================
word_indices =
   2
   6
   3
   2
   2
   2

% =============================
ex6 test case for emailFeatures()

Test case for emailFeatures()

% input
idx = [2 4 6 8 2 4 6 8]';
v = emailFeatures(idx);
v(1:10)
sum(v)

% results
>> v(1:10)
ans =
   0
   1
   0
   1
   0
   1
   0
   1
   0
   0

>> sum(v)
ans =  4
>>


