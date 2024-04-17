import Control.Monad
import System.Environment 
import Text.ParserCombinators.Parsec
import Data.Bool

data LogicExpr = BOOL Bool
              | AND LogicExpr LogicExpr 
              | OR LogicExpr LogicExpr 
              | NOT LogicExpr
              | PARENS LogicExpr

-- Skip whitespaces 
whitespace :: Parser ()
whitespace = void $ many $ oneOf " \n\t"

skipWhiteSpaces :: Parser a -> Parser a
skipWhiteSpaces p = do
  x <- p
  whitespace
  return x

parseBool :: Parser LogicExpr
parseBool = skipWhiteSpaces $ do
  val <- string "TRUE" <|> string "FALSE"
  return $ case val of
    "TRUE" -> BOOL True
    "FALSE" -> BOOL False

parseParens :: Parser LogicExpr
parseParens = do
  skipWhiteSpaces $ char '('
  expr <- skipWhiteSpaces $ (try parseOp <|> parseBool)
  skipWhiteSpaces $ char ')'
  return $ PARENS expr

parseBoolOrParens :: Parser LogicExpr
parseBoolOrParens = parseBool <|> parseParens

parseOp :: Parser LogicExpr
parseOp = chainl1 parseBoolOrParens op
  where
    op = do
      val <- skipWhiteSpaces $ (string "AND" <|> string "OR")
      return  $  case val of
        "AND" -> AND
        "OR" -> OR

parseExpr :: Parser LogicExpr
parseExpr = parseParens
            <|> parseOp
            <|> parseBool

parseExpr2 = do
  whitespace
  t <- parseExpr
  return t
   
showExpr :: LogicExpr -> String
showExpr (BOOL b) = show b
showExpr (AND a b) = (showExpr a) ++ " and " ++ (showExpr b)
showExpr (OR a b) = (showExpr a) ++ " or " ++ (showExpr b)
showExpr (PARENS m) = "(" ++ (showExpr m) ++ ")"

instance Show LogicExpr where show = showExpr

-- Evaluate
eval :: LogicExpr -> Bool
eval (BOOL b) = b
eval (AND a b) = (eval a) && (eval b)
eval (OR a b) = (eval a) || (eval b)
eval (PARENS m) = eval m


-- Przyklad uzycia
-- in: showExpr (AND (BOOL True) (BOOL False))
-- out: "True and False"
