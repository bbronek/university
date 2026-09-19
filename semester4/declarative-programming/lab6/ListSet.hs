module ListSet (intersection, union, difference, isSubset) where
  import Data.List (delete)

  intersection [] _ = []
  intersection (x:xs) l | elem x l = x : intersection xs l
                  | otherwise = intersection xs l
  union [] ys = ys
  union (x:xs) ys = x : union xs (delete x ys)

  difference [] ys = []
  difference (x:xs) ys = if (elem x ys) then difference xs ys
                      else x:difference xs ys

  isSubset xs ys = all (`elem` ys) xs
