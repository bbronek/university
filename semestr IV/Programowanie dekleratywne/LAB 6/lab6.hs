import Mojzbior

-- zad 1
-- iloczyn [1,2,3] [2] 
-- out: [2]

data Tree a = Empty | Node a (Tree a) (Tree a)
                deriving (Show, Eq)

-- zad 2
t1::Tree Int
t2::Tree Char

t1 = Node 1 (Node 2 (Node 4 Empty Empty)
          ((Node 5 Empty) (Node 8 Empty Empty)))
    (Node 3 ((Node 6 Empty) (Node 9 Empty Empty))
          (Node 7 Empty Empty))

t2 = Node 'a' (Node 'b' Empty
                        (Node 'd' (Node 'f' Empty Empty) Empty))
              (Node 'c' (Node 'e' Empty
                                (Node 'g' Empty Empty))
                        Empty)

minHeight :: Tree a -> Int
minHeight Empty = 1
minHeight (Node a Empty Empty) = 0
minHeight (Node a l r) = 1 + min (minHeight r) (minHeight l)

-- zad 3
data TernaryTree a = Empty1 | Node1 a (TernaryTree a) (TernaryTree a) (TernaryTree a)
                        deriving (Show)

terT1::TernaryTree Int 

terT1 = Node1 1 (Node1 2 (Node1 5 Empty1 Empty1 Empty1) Empty1 Empty1)
        (Node1 3 Empty1 Empty1 Empty1)
        (Node1 2 Empty1 Empty1 Empty1)

sumTernaryTree::TernaryTree Int -> Int
sumTernaryTree Empty1 = 0
sumTernaryTree (Node1 a l m r) = a + sumTernaryTree l + sumTernaryTree m + sumTernaryTree r

-- zad 4
class Nazwisko a where
  fun1 :: a -> String

data Imie = Bartek | Robert | Tomasz
            deriving(Show)

instance Nazwisko Imie where
  fun1 Bartek = "Bronikowski"
  fun1 Robert = "Kowalski"
  fun1 Tomasz = "Nowak"

-- fun1 to funkcja ktora dla unikalnego imienia przyporzadkowuje nazwisko
-- przyklad:
-- in: fun1 Bartek
-- out "Bronikowski"
