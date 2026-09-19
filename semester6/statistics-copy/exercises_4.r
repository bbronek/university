variance_confidence_interval <- function(values, alpha) {
  stopifnot(length(values) > 1, length(alpha) == 1, alpha > 0, alpha < 1)
  degrees_of_freedom <- length(values) - 1
  degrees_of_freedom * var(values) / qchisq(c(1 - alpha / 2, alpha / 2), degrees_of_freedom)
}
