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
  expr <- parseExpr
  skipWhiteSpaces $ char ')'
  return $ PARENS expr

parseTerm :: Parser LogicExpr
parseTerm = (NOT <$> (skipWhiteSpaces (string "NOT") *> parseTerm))
            <|> parseBool <|> parseParens

parseExpr :: Parser LogicExpr
parseExpr = chainl1 conjunction (OR <$ skipWhiteSpaces (string "OR"))
  where conjunction = chainl1 parseTerm (AND <$ skipWhiteSpaces (string "AND"))

parseExpr2 :: Parser LogicExpr
parseExpr2 = whitespace *> parseExpr <* eof

showExpr :: LogicExpr -> String
showExpr (BOOL b) = show b
showExpr (NOT expression) = "not " ++ showExpr expression
showExpr (AND a b) = (showExpr a) ++ " and " ++ (showExpr b)
showExpr (OR a b) = (showExpr a) ++ " or " ++ (showExpr b)
showExpr (PARENS m) = "(" ++ (showExpr m) ++ ")"

instance Show LogicExpr where show = showExpr

-- Evaluate
eval :: LogicExpr -> Bool
eval (BOOL b) = b
eval (NOT expression) = not (eval expression)
eval (AND a b) = (eval a) && (eval b)
eval (OR a b) = (eval a) || (eval b)
eval (PARENS m) = eval m


-- Usage example
-- in: showExpr (AND (BOOL True) (BOOL False))
-- out: "True and False"
