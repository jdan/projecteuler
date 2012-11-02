module Euler1 where

fizzOrBuzz :: Integer -> Bool
fizzOrBuzz n = (n `rem` 3 == 0) || (n `rem` 5 == 0)

main = do
  print $ sum $ filter fizzOrBuzz [1..999]
