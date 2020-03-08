% to debug:
%
%ref: [https://www.gnu.org/software/octave/doc/v4.0.0/Debug-Mode.html]

A = magic(5)

disp(A)

disp('dbwhere, dblist')
disp('dbstep, dbstep in, dbstep out')
disp('dbcont, dbquit')

keyboard % a breakpoint
