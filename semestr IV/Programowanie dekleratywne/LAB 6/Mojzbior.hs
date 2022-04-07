module Mojzbior (iloczyn, suma, roznica, podzbior) where
  import Data.List (delete)

  iloczyn [] _ = []
  iloczyn (x:xs) l | elem x l = x : iloczyn xs l
                  | otherwise = iloczyn xs l
  suma [] ys = ys
  suma (x:xs) ys = x : suma xs (delete x ys)

  roznica [] ys = []
  roznica (x:xs) ys = if (elem x ys) then roznica xs ys
                      else x:roznica xs ys

  podzbior [] [] = True
  podzbior _ [] = False
  podzbior [] _ = True 
  podzbior (x:xs) (y:ys) 
      | x == y = podzbior xs ys
      | otherwise = podzbior (x:xs) ys
