import System.IO
-- zad 1
fun1 [] = []
fun1 (x:xs) = (x, length (filter (x ==) xs) + 1) : fun1 (filter (x /=) xs)

-- zad 2
-- compare "" "" = ""
-- compare xs ys 
-- fun2 = do
--     print "Podaj pierwszy string: "
--     string1 <- getLine

--     print "Podaj drugi string: "
--     string2 <- getLine


-- zad 3
-- saveToFile = do
--     file <- openFile "zad3.txt" WriteMode
--     c <- getLine
--     hPutStr file c
--     hClose file

-- readFromFile = do
--     file <- openFile "zad3.txt" ReadMode
--     content <- hGetContents file
--     putStrLn content
--     putStrLn "Liczba znakow: " ++ show(length content)

-- -- zad 4
-- fun4a n = [(i,j) | i <- [1..n], j <- [i+1..n]]

-- fun4b n = do
--     i <- [1..n]
--     j <- [i+1..n]
--     return (i,j)

-- zad 5
wordCount input = (length . words) input

fun5_a = do
  file <- openFile "test.txt" ReadMode
  content <- hGetContents file
  let wordsCounter = wordCount content
  putStr "Liczba slow wynosi: "
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

-- zad 6
f6 :: (Eq a, Num a) => a -> [[a]]
f6 1 = [[1]]
f6 n = map add ns ++ map prep ns
  where ns          = f6 (n-1)
        prep is    = 1:is
        add (i:is) = (i+1):is
