-- Euler 3 solution by Jordan Scales
-- 2 November 2012

module Euler3 where
import Factor

main :: IO ()
main = do
  print $ head $ primeFactors 600851475143
