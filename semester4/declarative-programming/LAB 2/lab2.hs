-- zad 1
pot = potPOM 1
potPOM x a n = if n == 0 then x
                 else potPOM (x * a) a (n - 1)

ciag n = ciagPOM n 3 1
ciagPOM n c1 c2
  | n == 1 = c1
  | n == 2 = c2
  | otherwise = ciagPOM (n - 1) c2 (2 * c2 - c1)

-- zad 2
root a b c = if d < 0 then error "delta mniejsza od 0" else (x, y)
                        where
                          x = (-b + sqrt d ) / (2 * a)
                          y = (-b - sqrt d ) / (2 * a)
                          d = b^2 - 4 * a * c

-- zad 3
between a b c
  | a > b && a < c = a
  | b > a && b < c = b
  | otherwise = c

-- zad 4
hour m = if hour > 12 then mod hour 12
           else hour
            where
              hour = div m 60 + 1

-- zad 5
xor x y | x && not y = True
        | not x && y = True
        | otherwise = False

-- zad 6
-- a)
alt1 x y = if x then True
            else if y then True
              else False

-- b)
alt2 x y | x = True
         | y = True
         | otherwise = False 

-- c)
alt3 x y = case (x,y) of
              (True, _) -> True
              (_, True) -> True
              _ -> False

-- zad 7
-- a)
f1 p q = (p || q) && (not p && not q)

-- b)
f2 p q r = not p || (not q || r) || (not q || not r)
            
