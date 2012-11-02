-- Euler 12 solution by Jordan Scales
-- 2 November 2012

module Main where
import Factor

-- basic Godel encoding of a given Integral
simpleGodel :: (Integral a) => a -> [a]
simpleGodel n = simpleGodel' (primeFactors n) 2 0

simpleGodel' :: (Integral a) => [a] -> a -> a -> [a]
simpleGodel' [] _ r = [r]
simpleGodel' (x:xs) c r
  | x == c    = simpleGodel' xs c (r+1)
  | otherwise = r : simpleGodel' xs x 1

numDivisors :: (Integral a) => a -> a
numDivisors n = foldl (*) 1 (map (+1) $ simpleGodel n)

triangle :: (Integral a) => a -> a
triangle n = (n * (n+1)) `div` 2

main :: IO ()
main = do
  print $ head $ filter (\n -> (numDivisors n) > 500) $ map triangle [1..]
