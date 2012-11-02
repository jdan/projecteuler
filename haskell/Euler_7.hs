-- Euler 7 solution by Jordan Scales
-- 2 November 2012
-- pretty slow :(

module Euler7 where

primes :: [Integer]
primes = sieve [2..]
  where sieve (x:xs) = x : sieve [n | n <- xs, n `mod` x /= 0]

main :: IO ()
main = do
  print $ head $ drop 10000 primes
