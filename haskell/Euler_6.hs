-- Euler 6 solution by Jordan Scales
-- 2 November 2012

module Euler6 where

main :: IO ()
main = do
  let sumSquares = sum $ map (^2) [1..100]
  let squareSum  = (^2) $ sum [1..100]
  print $ squareSum - sumSquares
