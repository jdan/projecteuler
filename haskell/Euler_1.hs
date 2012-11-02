-- Euler 1 solution by Jordan Scales
-- 1 November 2012

module Main where

fizzOrBuzz :: Integer -> Bool
fizzOrBuzz n = (n `rem` 3 == 0) || (n `rem` 5 == 0)

main = do
  print $ sum $ filter fizzOrBuzz [1..999]
