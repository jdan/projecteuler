-- Euler 2 solution by Jordan Scales
-- 1 November 2012

module Euler2 where

main :: IO ()
main = do
  let fibs = map fst $ iterate (\(a,b) -> (b, a+b)) (0,1)
  print $ sum $ filter even $ takeWhile (< 4000000) fibs
