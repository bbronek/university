ordinary_moment = function(v, r) {
  sum = 0
  
  for(x in v){
    sum = sum + x^r
  }
  
  sum = sum / length(v)
}

