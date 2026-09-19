import System.IO
-- task 1
fun1 [] = []
fun1 (x:xs) = (x, length (filter (x ==) xs) + 1) : fun1 (filter (x /=) xs)

-- task 5
wordCount input = (length . words) input

fun5_a = do
  file <- openFile "test.txt" ReadMode
  content <- hGetContents file
  let wordsCounter = wordCount content
  putStr "Word count: "
  print wordsCounter
  hClose file
    
wordsLengths :: [String] -> [Int]
wordsLengths = map length
fun5_b = do
  file <- openFile "test.txt" ReadMode
  content <- hGetContents file
  let wordsLengthList = wordsLengths (words content)
  print wordsLengthList
  hClose file

-- task 6
f6 :: (Eq a, Num a) => a -> [[a]]
f6 1 = [[1]]
f6 n = map add ns ++ map prep ns
  where ns          = f6 (n-1)
        prep is    = 1:is
        add (i:is) = (i+1):is
