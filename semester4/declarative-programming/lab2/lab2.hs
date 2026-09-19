power base exponent
  | exponent < 0 = error "Exponent must be nonnegative"
  | otherwise = accumulate 1 exponent
  where
    accumulate result 0 = result
    accumulate result remaining = accumulate (result * base) (remaining - 1)

sequenceValues n
  | n < 1 = error "Sequence index must be positive"
  | otherwise = accumulate n 3 1
  where
    accumulate 1 first _ = first
    accumulate 2 _ second = second
    accumulate remaining first second = accumulate (remaining - 1) second (2 * second - first)

quadraticRoots a b c
  | a == 0 = error "Quadratic coefficient must be nonzero"
  | discriminant < 0 = error "Negative discriminant"
  | otherwise = ((-b + sqrt discriminant) / (2 * a), (-b - sqrt discriminant) / (2 * a))
  where
    discriminant = b ^ 2 - 4 * a * c

medianOfThree a b c = a + b + c - minimum [a, b, c] - maximum [a, b, c]

hour minutes = (minutes `div` 60) `mod` 12 + 1

xor first second = first /= second

orConditional first second = if first then True else second

orGuards first second
  | first = True
  | second = True
  | otherwise = False

orPattern first second = case (first, second) of
  (True, _) -> True
  (_, True) -> True
  _ -> False

contradiction p q = (p || q) && (not p && not q)

tautology p q r = not p || (not q || r) || (not q || not r)
