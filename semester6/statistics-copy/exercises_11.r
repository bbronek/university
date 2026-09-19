library(MASS)
data_set <- Cushings

qda_model <- qda(Type ~ Tetrahydrocortisone + Pregnanetriol, data = data_set)

prediction <- predict(qda_model)

error <- sum(prediction$class != data_set$Type) / nrow(data_set)

res <- 100

t_h_range <- seq(0, 60, length = res)
p_range <- seq(0, 12, length = res)

grid_data <- expand.grid(Tetrahydrocortisone = t_h_range, Pregnanetriol = p_range)
classification <- predict(qda_model, grid_data)

filled.contour(t_h_range, p_range, matrix(as.numeric(classification$class), nrow = res), 
               levels = 0.5:4.5, 
               col = c("gray", "lightcoral", "lightgreen", "lightblue"),
               plot.axes = {axis(1); axis(2); 
                 points(data_set$Tetrahydrocortisone, data_set$Pregnanetriol, col = data_set$Type, pch = 20, cex = 2)})

