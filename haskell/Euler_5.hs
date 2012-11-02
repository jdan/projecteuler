-- Euler 5 solution by Jordan Scales
-- 2 November 2012

module Main where

-- divides an integer from a list of integer
-- adds the leftovers (if there are any) to the end
-- divideInto [2,3,4,5] 25 => [2,3,4,5,5]
divideInto :: (Integral a) => [a] -> a -> [a]
divideInto ls 1 = ls
divideInto [] n = [n]
divideInto (x:xs) n
  | (n `rem` x == 0) = x : (divideInto xs (n `div` x))
  | otherwise        = x : (divideInto xs n)

-- compounds divideUptoN from 2 to N
divideUptoN :: (Integral a) => a -> [a]
divideUptoN n = divideUptoN' 2 n [1]

-- order is important (small -> large)
divideUptoN' :: (Integral a) => a -> a -> [a] -> [a]
divideUptoN' n e ls
  | n == e    = ls
  | otherwise = divideUptoN' (n+1) e (divideInto ls n)

main :: IO ()
main = do
  print $ foldl (*) 1 $ divideUptoN 20
