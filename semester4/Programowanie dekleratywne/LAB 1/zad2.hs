{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
import Prelude hiding (gcd, lcm)

a x | x > 2          = x^2
    | x>0 && x<=2    = x-1
    | x<=0           = abs x

-- volume of a cylinder
b(r,h) = (1/3) * pi * r^2

-- surface area of a cylinder
c(r,h) = (2*pi*r^2) + (2*pi*r*h)

-- a^n
pow (a, n)
  | n == 0 = 1
  | n == 1 = a
  | otherwise = pow(a,n-1) * a

-- check if sum of numbers is even
e a b = mod(a+b) 2 == 0

-- seq a1=5 and a(n) = 2a(n-2) + 1
f n = if n == 1 then 5
          else 2*f(n-1) + 1

-- fibonacci
g n = if n <=2 then 1
        else g(n-2) + g(n-1)

-- check if number x is n element of fibonacci seq
h x = x == g x

gcd a b
  | a == b = a
  | a > b = gcd(a-b) b
  | otherwise = gcd a (b-a)

lcm a b = if gcd a b == 0 then 0
            else (a*b)/gcd a b

canBuildTriangle a b c = (a+b) > c && (a+c) > b && (b+c) > a
