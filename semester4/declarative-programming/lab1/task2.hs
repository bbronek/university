import Prelude hiding (gcd, lcm)

piecewise x
  | x > 2 = x ^ 2
  | x > 0 && x <= 2 = x - 1
  | x <= 0 = abs x

-- volume of a cylinder
cylinderVolume (r, h) = pi * r ^ 2 * h

-- surface area of a cylinder
cylinderArea (r, h) = (2 * pi * r ^ 2) + (2 * pi * r * h)

-- a^n
pow (a, n)
  | n == 0 = 1
  | n == 1 = a
  | otherwise = pow (a, n - 1) * a

-- check if sum of numbers is even
isSumEven a b = mod (a + b) 2 == 0

-- seq a1=5 and a(n) = 2a(n-2) + 1
recurrence n =
  if n == 1
    then 5
    else 2 * recurrence (n - 1) + 1

-- fibonacci
fibonacciAt n =
  if n <= 2
    then 1
    else fibonacciAt (n - 2) + fibonacciAt (n - 1)

-- check if number x is n element of fibonacci seq
isFibonacci x = x >= 0 && x `elem` takeWhile (<= x) fibonacci
  where
    fibonacci = 0 : 1 : zipWith (+) fibonacci (tail fibonacci)

gcd a 0 = abs a
gcd a b = gcd b (a `mod` b)

lcm a b = if a == 0 || b == 0 then 0 else abs ((a `div` gcd a b) * b)

canBuildTriangle a b c = (a + b) > c && (a + c) > b && (b + c) > a
