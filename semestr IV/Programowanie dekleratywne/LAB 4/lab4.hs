import Data.List
import Data.List (delete)
-- zad 1
ciagRek i k d
  | k < 1 = []
  | i <= k = i : ciagRek (i+d) k d
  | otherwise = []

ciag a b q = [a+x*q | x <- [0..b], a+x*q <= b]
-- zad 2
wycinekRek :: (Num a1, Num a2, Ord a1, Ord a2) => a1 -> a2 -> [a3] -> [a3]
wycinekRek _ _ []  = []
wycinekRek i k (x:xs)
 | i > 1      = wycinekRek (i - 1) (k - 1) xs
 | k < 1      = []
 | otherwise  = x:wycinekRek (i - 1) (k - 1) xs

wycinek i k xs = map(xs !!) [i-1..k-1]

-- zad 3
numerowanie n xs = zip xs [n..length xs]

-- zad 4
iloczyn_zPOM (x:xs) (y:ys)
 | x == y    = x : iloczyn_zPOM xs ys
 | x < y     = iloczyn_zPOM xs (y:ys)
 | x > y     = iloczyn_zPOM (x:xs) ys
iloczyn_zPOM _ _ = []

iloczyn_z xs ys = iloczyn_zPOM (sort xs) (sort ys)

-- zad 5
-- suma_zPOM x y
--   | null x && not (null y) = y
--   | null y && not (null x) = x
--   | null x && null y = []
--   | elem (head x) (tail x) || elem (head x) (tail y) = suma_zPOM (tail x) y
--   | elem (head y) (tail x) || elem (head y) (tail y) = suma_zPOM x (tail y)
--   | (head x) == (head y) = (head x) : suma_zPOM (tail x) (tail y)
--   | otherwise = (head x) : (head y) : suma_zPOM (tail x) (tail y)

-- suma_z x y = suma_zPOM (sort x) (sort y)
suma_z [] ys = ys
suma_z (x:xs) ys = x : suma_z xs (delete x ys)

-- zad 6
roznica_z [] ys = []
roznica_z (x:xs) ys = if (elem x ys) then roznica_z xs ys
                        else x:roznica_z xs ys

-- zad 7
powerList [] = [[]]
powerList (x:xs) = powerList xs ++ map(x:) (powerList xs)

-- zad 9
nalezy x xs = foldl (\acc a -> if a == x then True else acc) False xs
-- zad 10
my_map f xs =  foldl (\ys y -> ys++[(f y)]) [] xs

-- zad 11
head' :: [a] -> a
head' = foldr1 (\x _ -> x)

last' :: [a] -> a
last' = foldl1(\_ x -> x)

maksimum [] = error "Pusta Lista"
maksimum xs = foldl1 (max) xs
