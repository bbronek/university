import System.IO
import Text.Printf (printf)

readInt :: [Char] -> Int
readInt x = read x :: Int

-- task 1
fun1 = do
  putStr "Enter the first number: "
  a <- getLine

  putStr "Enter the second number: "
  b <- getLine

  let union = readInt a + readInt b
  let intersection = readInt a * readInt b
  let difference = readInt a - readInt b
  
  putStrLn(a ++ "+" ++ b ++ "=" ++ show union ++ " " ++ a ++ "*" ++ b ++ "=" ++ show intersection ++ " " ++ a ++ "-" ++ b ++ "=" ++ show difference)

-- task 2
fun2 = do
  putStr "Enter your first name: "
  firstName <- getLine

  putStr "Enter your last name: "
  lastName <- getLine

  putStr "Enter your PESEL: "
  pesel <- getLine

  if length pesel /= 11 || any (`notElem` ['0'..'9']) pesel
    then putStrLn "PESEL must contain 11 digits"
    else do
      let encodedYear = readInt (take 2 pesel)
          encodedMonth = readInt (take 2 (drop 2 pesel))
          day = readInt (take 2 (drop 4 pesel))
          century = case encodedMonth `div` 20 of
            0 -> 1900
            1 -> 2000
            2 -> 2100
            3 -> 2200
            _ -> 1800
          month = encodedMonth `mod` 20
      printf "%s %s was born on %02d.%02d.%04d\n" firstName lastName day month (century + encodedYear)

-- task 3
greatestCommonDivisor = gcd
leastCommonMultiple = lcm

fun3 = do
  putStr "Enter the first number: "
  a <- getLine

  putStr "Enter the second number: "
  b <- getLine

  let firstNumber = readInt a
  let secondNumber = readInt b

  let gcdResult = greatestCommonDivisor firstNumber secondNumber
  let lcmResult = leastCommonMultiple firstNumber secondNumber

  putStrLn("GCD" ++ "(" ++ show firstNumber ++ "," ++ show secondNumber ++ ")" ++ "=" ++ show gcdResult  
            ++ " LCM" ++ "(" ++ show firstNumber ++ "," ++ show secondNumber ++ ")" ++ "=" ++ show lcmResult)

-- task 4
fun4 = do
  putStr "Enter the first word: "
  string1 <- getLine

  putStr "Enter the second word: "
  string2 <- getLine

  let result = if length string1 < length string2 then string1
               else string2

  putStrLn("Shorter word: " ++ result)

-- task 5
fun5 = do
  let x = 42
  print "Guess a number from 0 to 99 in 10 attempts"
  loop x 1 where
    loop :: Integer -> Integer -> IO ()
    loop x tries = do
      guess <- readLn :: IO Integer
      if tries <= 10 then 
        case compare guess x of
          LT -> do
            putStrLn "Too small!"
            loop x $ succ tries
          GT -> do
            putStrLn "Too large!"
            loop x $ succ tries
          EQ -> do
            print "Correct!"
      else 
        print "You have used all 10 attempts!"
