conf_int = function(x, alpha) 
{
  n = length(x)
  v = var(x)
  a =(n-1)*v/qchisq(1-alpha/2, n-1)
  b =(n-1)*v/qchisq(alpha/2, n-1)
  return(c(a, b))
}