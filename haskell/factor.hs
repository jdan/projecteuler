module Factor (primeFactors, prime) where

primeFactors :: (Integral a) => a -> [a]
primeFactors n = primeFactors' n [] 2

primeFactors' :: (Integral a) => a -> [a] -> a -> [a]
primeFactors' 1 ls _ = ls
primeFactors' n ls c
  | n == c         = c:ls
  | n `rem` c == 0 = primeFactors' (n `div` c) (c:ls) 2
  | otherwise      = primeFactors' n ls (c + 1)

prime :: (Integral a) => a -> Bool
prime n = ((==1) . length . primeFactors) n
