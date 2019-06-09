library(quantmod)
library(plyr)

what_metrics <- yahooQF(c("Previous Close", 
                          "Open",
                          "Volume"))

Symbols<-c("^DJI","^FTSE","^GDAXI","^HSI","^STI","^KLSE")
  
metrics <- getQuote(paste(Symbols, sep="", collapse=";"), what=what_metrics)

write.table(metrics, '/Users/yapboonhui/Documents/WQD7005/index.csv', sep=",", 
            row.names=TRUE, col.names=TRUE)
