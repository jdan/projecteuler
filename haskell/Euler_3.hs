-- Euler 3 solution by Jordan Scales
-- 2 November 2012

module Main where
import Factor

main :: IO ()
main = do
  print $ head $ primeFactors 600851475143
