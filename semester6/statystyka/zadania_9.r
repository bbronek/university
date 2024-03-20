klasyfikuj <- function(x, y, a, b, c) {
  y_pred = a*x^2 + b*x + c
  klasyfikacja = ifelse(y >= y_pred, 'klasa1', 'klasa2')
  return(klasyfikacja)
}