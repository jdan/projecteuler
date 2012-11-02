-- Euler 4 solution by Jordan Scales
-- 2 November 2012
-- kinda slow :(

module Main where

-- digits 1234 -> [1,2,3,4]
digits :: Integer -> [Integer]
digits 0 = []
digits n = digits (n `div` 10) ++ [n `mod` 10]

-- center [1,2]     -> []
-- center [1,2,3,4] -> [2,3]
center :: [Integer] -> [Integer]
center ls = take (length ls - 2) $ tail ls

palindrone :: Integer -> Bool
palindrone n = palindrone' $ digits n

palindrone' :: [Integer] -> Bool
palindrone' [] = True
palindrone' ls =
  (head ls == last ls) && palindrone' (center ls)

main :: IO ()
main = do
  print $ maximum
    (filter palindrone 
      [x1 * x2 | x1 <- [1..999], x2 <- [1..x1]])
