-- Euler 20 solution by Jordan Scales
-- 2 November 2012

module Main where

sumDigits :: (Integral a) => a -> a
sumDigits n
  | n < 10    = n
  | otherwise = (n `mod` 10) + sumDigits (n `div` 10)

main = do
  print $ sumDigits $ product [2..100]
