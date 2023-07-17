
make_string_rating <- function(bool_var){
    interval_list = c(1, length(bool_var))
    for (i in 1:length(bool_var)) {
      var = as.numeric(bool_var[i])
      interval = "0"
     
      if(var >= 90){
          interval = "90 - 100 points"
      }
          
      else{
          interval = "80 - 90 points"
      }
          
      interval_list[i] = interval
     }
      
     return(interval_list)
   }
  
  
  blox_plot <- function(x, var, y_title, x_title){
     max_y = nrow(var)
     plot <- hcboxplot(x = x, var = var, var2 = var, outliers=FALSE) %>%
               hc_chart(type = "bar") %>%
               hc_yAxis(title = list(text = y_title),
               labels = list(format = "$ {value}"), min = 0) %>%
               hc_xAxis(title = list(text = x_title),
               labels = list(format = "{value}")) %>%
               hc_add_theme(hc_theme_google())
      
     htmltools::tagList(plot)
  }
  
  
  blox_plot(df$price, make_string_rating(df$points), 'Price', 'Points')