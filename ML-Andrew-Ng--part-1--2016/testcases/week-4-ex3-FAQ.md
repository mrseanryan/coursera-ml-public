week 4 - ex3 - FAQ
====

ref:
[https://www.coursera.org/learn/machine-learning/discussions/weeks/4/threads/GS0y6z_iEear2wpBpCdaRw]

VIDEO LECTURE FAQ

Q1) How do you compute the number of units in a NN Theta matrix?

The size of a Theta matrix is (outputs x inputs).

For the output layer use the number of classifications. For the input size, use the number of hidden layer units plus one for the bias unit.

QUIZ FAQ

PROGRAMMING EXERCISE FAQ

See the Resources menu for tutorials and additional test cases.

Q1) I get the correct results for the One-vs-All Classifier, but the submit grader doesn't give me any score.

The submit grader uses a different test case than the one in the exercise script. It has a different number of training examples, features, and classifications.

Be sure your code makes no assumptions about any of these parameters. Your code must work with any size of data set.

Q2) Why are the images of the digits upside-down?

The gnuplot library changed its default image orientation some time ago. The scripts for this course have not been updated yet. You can restore the images correctly by adding a line at line 50 of displayData.m:

display_array = flipud(display_array);

Q3) Why do I only get about 69% training accuracy?

Be sure you're using the sigmoid() function in forward propagation.

Q4) My NN predict() function doesn't pass the grader. What should I check?

The bias units you add during forward propagation should be after using the sigmoid() function.

Q5) I am using the max() function, but can't get the correct results for predictOneVsAll() or predict(). What's the trick?

The Hint text in predictOneVsAll.m and predict.m both have this instruction:

... the max function can also return the index of the max element, for more information see 'help max'. If your examples are in rows, then, you can use max(A, [], 2) to obtain the max for each row.

The max() function can return two values:

The maximum value in each row. We don't care about that.
The row index where the maximum value was found. That is our predicted classification - the row where the maximum value was found.
Try these commands in your console to see how it works:


```
Q = magic(4)      % just some test data

[val idx] = max(Q, [], 2)
```
