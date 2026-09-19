module ListSet (intersection, union, difference, isSubset) where

import Data.List (delete)

intersection [] _ = []
intersection (value : rest) values
  | value `elem` values = value : intersection rest values
  | otherwise = intersection rest values

union [] values = values
union (value : rest) values = value : union rest (delete value values)

difference [] _ = []
difference (value : rest) values
  | value `elem` values = difference rest values
  | otherwise = value : difference rest values

isSubset values candidates = all (`elem` candidates) values
