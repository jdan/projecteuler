sumFizzBuzz(0, T, T).
sumFizzBuzz(N, Acc, T) :- N mod 3 =:= 0, Acc2 is Acc + N, N2 is N - 1, sumFizzBuzz(N2, Acc2, T), !.
sumFizzBuzz(N, Acc, T) :- N mod 5 =:= 0, Acc2 is Acc + N, N2 is N - 1, sumFizzBuzz(N2, Acc2, T), !.
sumFizzBuzz(N, Acc, T) :- N2 is N - 1, sumFizzBuzz(N2, Acc, T), !.

euler1(M, T) :- N is M - 1, sumFizzBuzz(N, 0, T).

% euler1(1000, T)
% T = 233168.
