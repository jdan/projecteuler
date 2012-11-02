-- Euler 9 solution by Jordan Scales
-- 2 November 2012

module Main where

main :: IO ()
main = do
  print $ head [a*b*(1000-a-b) | a <- [1000, 999..1],
                                 b <- [a, a-1..1],
                                 a^2 + b^2 == (1000-a-b)^2]
