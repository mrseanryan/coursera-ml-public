week 5 FAQ
===

ref [https://www.coursera.org/learn/machine-learning/discussions/weeks/5/threads/ag_zHUGDEeaXnBKVQldqyw]

FAQ for Week 5 and programming exercise 4
===
Tom MosherMentorWeek 5 · 2 months ago · Edited
VIDEO LECTURE FAQ

There are a LOT of errors in the Week 5 video lectures. The Course Wiki has a list of them in the Errata section. Do yourself a favor and keep the Errata list handy while you are watching the videos.

Here is a link to the Course Wiki: https://share.coursera.org/wiki/index.php/ML:Main

QUIZ FAQ

(empty)

PROGRAMMING EXERCISE FAQ

ex4 is the most challenging programming exercise in the course.

I strongly recommend you read the tutorial for ex4 via the "Resources" menu. This tutorial provides the vectorized method, which has a couple of significant advantages over the iterative for-loop method Prof Ng lectures about and discusses in ex4.pdf:

The vectorized method is far easier to implement. It consists almost entirely of matrix multiplication. There are very few matrix indexes to worry about.
The vectorized method runs 30x to 50x faster than the for-loop method.

Q1) My gradient checking results are wrong. How can I fix it?

The key point to remember about backpropagation is that the hidden layer bias unit does not connect back to the input layer. So we do not include the first column of Theta2 in the backpropagation calculations that lead to Delta1 and Theta1_grad.

Here are some common reasons for this issue:

You have only excluded the first element of Theta2 from backpropagation into Theta1, instead of excluding all of the first column.
You have artificially added some rows or columns to Theta2 in order to force the dimensions to be correct. This is a bad thing - the only items to add are the bias units in forward propagation.
You are including the bias unit when you compute the sigmoid() or sigmoidGradient(). This is a bad thing.
