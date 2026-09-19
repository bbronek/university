classify <- function(x, y, a, b, c) {
  y_pred <- a*x^2 + b*x + c
  classification <- ifelse(y >= y_pred, 'class1', 'class2')
  return(classification)
}
