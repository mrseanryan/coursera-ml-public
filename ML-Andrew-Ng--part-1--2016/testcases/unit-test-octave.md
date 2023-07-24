Add to very bottom of code after end in file:


%!test
%! p = polyFeatures([1:3]',4)
%! p_expected = [1    1    1    1; 2    4    8   16; 3    9   27   81];
%! assert(p, p_expected, 1);


to run:
test polyFeatures
