import System.IO

readInt :: [Char] -> Int
readInt x = read x :: Int

-- zad 1
fun1 = do
  putStr "Podaj pierwsza liczbe: "
  a <- getLine

  putStr "Podaj druga liczbe: "
  b <- getLine

  let suma = readInt a + readInt b
  let iloczyn = readInt a * readInt b
  let roznica = readInt a - readInt b
  
  putStrLn(a ++ "+" ++ b ++ "=" ++ show suma ++ " " ++ a ++ "*" ++ b ++ "=" ++ show iloczyn ++ " " ++ a ++ "-" ++ b ++ "=" ++ show roznica)

-- zad 2
fun2 = do
  putStr "Podaj imie: "
  imie <- getLine

  putStr "Podaj nazwisko: "
  nazwisko <- getLine

  putStr "Podaj numer pesel: "
  pesel <- getLine

  let rokPesel = readInt (take 2 pesel)
  let miesiacPesel = readInt  (drop 2 (take 4 pesel))
  let dzienPesel = readInt  (drop 4 (take 6 pesel))

  let miesiac =  if rokPesel > 22 then miesiacPesel
                 else miesiacPesel -20

  let dzien =  dzienPesel

  let rok =  if rokPesel > 22 then rokPesel + 1900
             else rokPesel + 2000

  let miesiacString = if miesiac <= 9 then "0" ++ show miesiac
                      else show miesiac

  let dzienString = if dzien <= 9 then "0" ++ show dzien
                    else show dzien

  putStrLn(imie ++ " " ++ nazwisko ++ " urodzil sie " ++ dzienString ++ "." ++ miesiacString ++ "." ++ show rok)

-- zad 3
nwd a b
  | a == b = a
  | a > b = nwd (a-b) b
  | otherwise = nwd a (b-a)

nww a b = (a * b) `div` nwd a b

fun3 = do
  putStr "Podaj pierwsza liczbe: "
  a <- getLine

  putStr "Podaj druga liczbe: "
  b <- getLine

  let firstNumber = readInt a
  let secondNumber = readInt b

  let nwdResult = nwd firstNumber secondNumber
  let nwwResult = nww firstNumber secondNumber

  putStrLn("NWD" ++ "(" ++ show firstNumber ++ "," ++ show secondNumber ++ ")" ++ "=" ++ show nwdResult  
            ++ " NWW" ++ "(" ++ show firstNumber ++ "," ++ show secondNumber ++ ")" ++ "=" ++ show nwwResult)

-- zad 4
fun4 = do
  putStr "Podaj pierwsze slowo: "
  string1 <- getLine

  putStr "Podaj drugie slowo: "
  string2 <- getLine

  let result = if length string1 < length string2 then string1
               else string2

  putStrLn("Krotsze slowo to: " ++ result)

-- zad 5
fun5 = do
  let x = 42
  print "Ogadnij okreslona liczbe z zakresu 0-99 masz 10 prob"
  loop x 1 where
    loop :: Integer -> Integer -> IO ()
    loop x tries = do
      guess <- readLn :: IO Integer
      if tries < 10 then 
        case compare guess x of
          LT -> do
            putStrLn "Zbyt mala!"
            loop x $ succ tries
          GT -> do
            putStrLn "Zbyt duza!"
            loop x $ succ tries
          EQ -> do
            print "Trafiles!"
      else 
        print "Wykorzystales 10 prob!"
