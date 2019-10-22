library("ggplot2")

findCovariance <- function(x,y) {
  meanX <- mean(x)
  meanY <- mean(y)
  desSum <- 0
  i <- 1
  while (i <= length(x)) {
    desSum = desSum + ((x[i] - meanX)*(y[i]-meanY))
    i = i + 1
  }
  return(desSum/(length(x)-1))
}

findVariance <- function(x) {
  meanX <- mean(x)
  desSum <- 0
  i <- 1
  while (i <= length(x)) {
    desSum = desSum + (x[i] - meanX)^2
    i = i + 1
  }
  return((desSum/(length(x)-1)))
}

findSlope <- function(x,y) {
  covarianceXY <- findCovariance(x,y)
  varianceX <- findVariance(x)
  return (covarianceXY/varianceX)
}

findYInt <- function(x,y) {
  meanX <- mean(x)
  meanY <- mean(y)
  m <- findSlope(x,y)
  return(meanY - m*meanX)
}

findStd <- function(x) {
  return(sqrt(findVariance(x)))
}

findCorrelation <- function(x,y) {
  meanX <- mean(x)
  meanY <- mean(y)
  stdX <- findStd(x)
  stdY <- findStd(y)
  desSum <- 0
  i <- 1
  while (i <= length(x)){
    desSum = desSum + (x[i]*y[i])
    i = i + 1
  }
  return((desSum - length(x)*meanX*meanY)/((length(x)-1)*stdX*stdY))
} 

m <- findSlope(mtcars$hp, mtcars$mpg)
b <- findYInt(mtcars$hp, mtcars$mpg)
r <- findCorrelation(mtcars$hp, mtcars$mpg)
eq = paste0("y = ", round(m,4), "*x + ", round(b,4),"   Correlation: ", round(r,4))

ggplot(mtcars, aes(hp, mpg, size = wt)) + geom_point(aes(colour = qsec)) + scale_color_gradient(low = "red", high = "blue") + geom_abline(intercept = b, slope = m, color = "green") + annotate(geom = "text",x = 200, y = 25, label = eq, size = 2.25) + labs(title = "Horsepower, Weight and Speed vs Miles per Gallon", subtitle = "How does horsepower and other factors affect fuel efficiency?", colour = "1/4 Mile Time", size = "Weight (1000 lbs)") + xlab("Horsepower") + ylab("Miles Per Gallon")



