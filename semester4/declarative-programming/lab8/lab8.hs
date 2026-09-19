import System.IO

-- task 1
frequencies [] = []
frequencies (x : xs) = (x, length (filter (x ==) xs) + 1) : frequencies (filter (x /=) xs)

-- task 5
wordCount input = (length . words) input

printWordCount = do
  file <- openFile "test.txt" ReadMode
  content <- hGetContents file
  let wordsCounter = wordCount content
  putStr "Word count: "
  print wordsCounter
  hClose file

wordsLengths :: [String] -> [Int]
wordsLengths = map length

printWordLengths = do
  file <- openFile "test.txt" ReadMode
  content <- hGetContents file
  let wordsLengthList = wordsLengths (words content)
  print wordsLengthList
  hClose file

-- task 6
compositions :: (Eq a, Num a) => a -> [[a]]
compositions 1 = [[1]]
compositions n = map add ns ++ map prep ns
  where
    ns = compositions (n - 1)
    prep is = 1 : is
    add (i : is) = (i + 1) : is
