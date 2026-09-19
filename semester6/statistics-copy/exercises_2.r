ordinary_moment <- function(values, order) {
  stopifnot(length(values) > 0, is.numeric(values), length(order) == 1)
  mean(values ^ order)
}
