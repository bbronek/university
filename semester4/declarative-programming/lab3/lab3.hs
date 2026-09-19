-- task 1
-- a)
addAtHead x y = x : y

-- b)
insertAt [] elem 0 = [elem]
insertAt [] _ _ = error "Position out of range"
insertAt (x : xs) elem pos
  | pos == 0 = elem : x : xs
  | pos > 0 = x : insertAt xs elem (pos - 1)
  | otherwise = error "Position must be nonnegative"

-- penultimate)
addAtTail x y = y ++ x

-- task 2
-- a)
secondElement a = a !! 1

-- b)
thirdElement a = a !! 2

-- penultimate)
penultimate a = a !! (length a - 2)

-- task 3

-- task 4
-- a)
countEven n = length [x | x <- [1 .. n], even x]

-- b)
countMultiplesOfThree n = length [x | x <- [1 .. n], mod x 3 == 0]

-- penultimate)
sumMultiplesOfThree n = sum [x | x <- [1 .. n], mod x 3 == 0]

-- task 5
evenLength a = even (length a)

-- task 6
-- a)
squaresWithMap = map (^ 2)

-- b)
squaresWithComprehension a = [x ^ 2 | x <- a]

-- task 7
count _ [] = 0
count s xs = length (filter (== s) xs)

-- task 8
duplicate _ n | n <= 0 = []
duplicate xs n = xs : duplicate xs (n - 1)

-- task 9
palindrome xs = xs == reverse xs

-- task 10
deleteN _ [] = []
deleteN i (x : xs)
  | i == 0 = xs
  | otherwise = x : deleteN (i - 1) xs

-- task 11
subList [] [] = True
subList _ [] = False
subList [] _ = True
subList (x : xs) (y : ys)
  | x == y = subList xs ys
  | otherwise = subList (x : xs) ys

-- task 12
reversedTuples xs = [(a, b) | (b, a) <- xs]
