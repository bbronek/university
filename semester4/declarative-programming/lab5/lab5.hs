-- task 1
-- (\x -> x >= 0) 3 a1
-- 3 -> True
-- (\x -> x^x) 3 a2
-- x^x = 3^3 = 27
-- (\x y -> y > x) 6 7 b1
--  7 > 6 -> True
-- (\x y -> flip div x y) 4 5 b2
-- 5 div 4 -> 1
-- (\a b c -> b^c - div a b) 3 4 5 c1
-- 4^5 - 0 = 1024
-- (\a b c -> not a && (b || c)  ) True False True
-- input: True False True | Output: False

-- task 2
data CarBrand = Audi | BMW | Skoda | Fiat | Toyota
  deriving (Show, Eq)

madeIn :: Country -> CarBrand

type Country = [Char]

madeIn country
  | country == "Germany" = Audi
  | country == "Czech Republic" = Skoda
  | country == "Italy" = Fiat
  | otherwise = error "Country not available"

maximumSpeed c = case c of
  Audi -> 270
  BMW -> 320
  Skoda -> 250
  Toyota -> 260
  _ -> error "Invalid car brand"

-- task 3
data University = UW | UJ | Uwr | UAM | UG
  deriving (Show, Eq)

universityData c = case c of
  UW -> (1, "Warszawa")
  UJ -> (-23, "Krakow")
  UAM -> (2345, "Poznan")
  UG -> (-5345435, "Gdańsk")
  _ -> error "University not available"

-- task 4
data Tree a = Empty | Node a (Tree a) (Tree a)
  deriving (Show, Eq)

t1 :: Tree Int
t1 =
  Node
    1
    ( Node
        2
        (Node 4 Empty Empty)
        ((Node 5 Empty) (Node 8 Empty Empty))
    )
    ( Node
        3
        ((Node 6 Empty) (Node 9 Empty Empty))
        (Node 7 Empty Empty)
    )

t2 :: Tree Char
t2 =
  Node
    'a'
    ( Node
        'b'
        Empty
        (Node 'd' (Node 'f' Empty Empty) Empty)
    )
    ( Node
        'c'
        ( Node
            'e'
            Empty
            (Node 'g' Empty Empty)
        )
        Empty
    )

depth :: Tree a -> Int
depth Empty = 0
depth (Node _ l r) = 1 + max (depth l) (depth r)

preorder :: Tree a -> [a]
preorder Empty = []
preorder (Node a l r) = [a] ++ preorder l ++ preorder r

inorder :: Tree a -> [a]
inorder Empty = []
inorder (Node a l r) = inorder l ++ [a] ++ inorder r

postorder :: Tree a -> [a]
postorder Empty = []
postorder (Node a l r) = postorder l ++ postorder r ++ [a]

-- task 5
-- a)
treeMember1 :: (Eq a) => a -> Tree a -> Bool
treeMember1 _ Empty = False
treeMember1 x (Node a l r) = x `elem` preorder (Node a l r)

-- b)
treeMember2 :: (Eq a) => a -> Tree a -> Bool
treeMember2 x Empty = False
treeMember2 x (Node a l r)
  | x == a = True
  | otherwise = treeMember2 x l || treeMember2 x r

-- task 6
subtree :: (Eq a) => Tree a -> Tree a -> Bool
subtree t1 t2 | t1 == t2 = True
subtree t1 (Node _ c1 c2) = subtree t1 c1 || subtree t1 c2
subtree _ _ = False

-- task 7
zipWith' f xs [] = xs
zipWith' f [] xs = xs
zipWith' f (x : xs) (y : ys) = f x y : zipWith' f xs ys

levels :: Tree a -> [[a]]
levels Empty = [[]]
levels (Node a Empty Empty) = [[a]]
levels (Node a l r) = [a] : zipWith' (++) (levels l) (levels r)
