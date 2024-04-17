-- zad 1
-- a) 
{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
addAtHead x y = x : y

-- b)
insertAtSec [] elem 2 = [elem]
insertAtSec (x:xs) elem pos
    | pos == 0 = elem : x : xs
    | pos > 0 = x : insertAtSec xs elem (pos - 1)

-- c)
addAtTail x y = y ++ x

-- zad 2
-- a)
secElem a = a !! 1

-- b)
thirdElem a = a !! 2

-- c)
c a = a !! (length a - 2)

-- zad 3

-- zad 4
-- a)
a4 n = length [x | x <- [1..n], even x ]

-- b)
b4 n = length [x | x <- [1..n], mod x 3 == 0]

-- c)
c4 n = sum [x | x <- [1..n], mod x 3 == 0]

-- zad 5
evenLength a = even (length a)

-- zad 6
-- a)
aPowList = map (^ 2)

-- b)
bPowList a = [x^2 | x <- a]

-- zad 7
count _ [] = 0
count s xs = length (filter(==s) xs)

-- zad 8
duplicate _ 0 = []
duplicate xs n = xs : duplicate xs (n-1)

-- zad 9
palindrome xs = xs == reverse xs

-- zad 10
deleteN _ [] = []
deleteN i (x:xs)
  | i == 0 = xs
  | otherwise = x : deleteN (i-1) xs

-- zad 11
subList [] [] = True
subList _ [] = False
subList [] _ = True 
subList (x:xs) (y:ys) 
  | x == y = subList xs ys
  | otherwise = subList (x:xs) ys

-- zad 12
reversedTuples xs = [(a,b) | (b,a) <- xs]

