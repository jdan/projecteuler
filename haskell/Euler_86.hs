-- pairs(N) returns integer pairs (A, B) A < B such that a^2 + b^2 == n^2
pairs :: (Integral a) => a -> [(a, a)]
pairs n = [(a, b) | b <- [1..n], a <- [1..b], a < n, a^2 + b^2 == n^2]

-- solutions((A,B)) returns the number of (x,y,z) x <= y <= z solutions
-- such that x + y == A
solutions :: (Integral a) => (a, a) -> a
solutions (a, _) = quot a 2

-- cuboids(N) returns the number of integer-sided cuboids such that the
-- shortest distance from one corner to the other (around the edges) is N
cuboids :: (Integral a) => a -> a
cuboids = sum . (map solutions) . pairs

-- cuboidsUnderN(M) sums cuboids(N) for all N <= M
cuboidsUnderN :: (Integral a) => a -> a
cuboidsUnderN m = sum $ map cuboids [1..m]
