import Data.List (delete, sort)

-- task 1
sequenceRecursive i k d
  | k < 1 = []
  | i <= k = i : sequenceRecursive (i + d) k d
  | otherwise = []

sequenceValues a b q = [a + x * q | x <- [0 .. b], a + x * q <= b]

-- task 2
sliceRecursive :: (Num a1, Num a2, Ord a1, Ord a2) => a1 -> a2 -> [a3] -> [a3]
sliceRecursive _ _ [] = []
sliceRecursive i k (x : xs)
  | i > 1 = sliceRecursive (i - 1) (k - 1) xs
  | k < 1 = []
  | otherwise = x : sliceRecursive (i - 1) (k - 1) xs

slice i k xs = map (xs !!) [i - 1 .. k - 1]

-- task 3
enumerateFrom n xs = zip xs [n ..]

-- task 4
intersectionSorted (x : xs) (y : ys)
  | x == y = x : intersectionSorted xs ys
  | x < y = intersectionSorted xs (y : ys)
  | x > y = intersectionSorted (x : xs) ys
intersectionSorted _ _ = []

intersection xs ys = intersectionSorted (sort xs) (sort ys)

-- task 5
union [] ys = ys
union (x : xs) ys = x : union xs (delete x ys)

-- task 6
difference [] ys = []
difference (x : xs) ys =
  if (elem x ys)
    then difference xs ys
    else x : difference xs ys

-- task 7
powerList [] = [[]]
powerList (x : xs) = powerList xs ++ map (x :) (powerList xs)

-- task 9
contains x xs = foldl (\acc a -> if a == x then True else acc) False xs

-- task 10
mapWithFold f xs = foldr (\y ys -> f y : ys) [] xs

-- task 11
head' :: [a] -> a
head' = foldr1 (\x _ -> x)

last' :: [a] -> a
last' = foldl1 (\_ x -> x)

maximumValue [] = error "Empty list"
maximumValue xs = foldl1 (max) xs
