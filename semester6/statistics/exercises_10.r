library(MASS)
data_set <- Cushings

qda_model <- qda(Type ~ Tetrahydrocortisone + Pregnanetriol, data = data_set)

prediction <- predict(qda_model)

classification_error <- sum(prediction$class != data_set$Type) / nrow(data_set)

resolution <- 100

t_h_range <- seq(0, 60, length = resolution)
p_range <- seq(0, 12, length = resolution)

grid_data <- expand.grid(Tetrahydrocortisone = t_h_range, Pregnanetriol = p_range)
classification <- predict(qda_model, grid_data)

filled.contour(t_h_range, p_range, matrix(as.numeric(classification$class), nrow = resolution),
               levels <- 0.5:4.5,
               col <- c("gray", "lightcoral", "lightgreen", "lightblue"),
               plot.axes = {axis(1); axis(2);
                 points(data_set$Tetrahydrocortisone, data_set$Pregnanetriol, col = data_set$Type, pch = 20, cex = 2)})
