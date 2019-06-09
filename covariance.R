# to compute covariance between stock prices
# modified from http://www.michaeljgrogan.com/variance-covariance-matrix-calculation-r/

library(dplyr)

# read all files that start with 'stock_2019' in the working directory (daily stock prices in Google Drive > Milestone 3 > Data Files)
file_list <- (list.files(pattern = "stock_2019"))
file_list

# change the header and add new column named date, remove stock names with '-'
for (file in file_list){
  readfile <- read.delim(file, sep = "|", header = FALSE)
  names(readfile) <- c("code","name","ref","open","last","change","change_perc","volume")
  readfile <- readfile[!grepl("-", readfile$name),]
  date <- basename(file) %>% strsplit(split = "_") %>% sapply( "[", 2 )
  date <- strsplit(date, split = "[.]")[[1]][[1]]
  readfile <- readfile %>% mutate(date = date)
  var_file <- strsplit(file, "[.]")[[1]][[1]]
  filee <- assign(var_file, readfile)
}

# concatenate all stocks prices into 'all_days'
all_days <- do.call(rbind, lapply( ls(patt="stock_2019"), get)) %>% arrange(name)
all_days

# select last price of every stock in each day 
for (stock in all_days$name) {
  price <- all_days %>% filter(name == stock) %>% select(last) # %>% mutate(return = diff(log(last),1))
  names(price) <- stock
  var_price <- paste("price_", stock, sep = "")
  price_table <- assign(var_price, price)
  write.csv(price_table,file = var_price)
  }

# combine all variables named 'price_' into 'all'
for (variable_price in (ls(patt="price_"))){
  all <- do.call(cbind, lapply(variable_price, get))
}

# check stock with incomplete data in another script
#for (file in file_list){
#  readfile <- read.csv(file)
#  num_row <- nrow(readfile)
#  if (num_row != "20"){
#    print(paste("price_", names(readfile)[2], sep=""))
#  }
#}
# remove stock variables with missing values 
rm(price_AIRASIAC68, price_AIRASIAC69, price_AMTEK, price_DAIMAN, price_DRBHCOMC62, price_DRBHCOMC63,price_DRBHCOMC74, price_DRBHCOMC75,
   price_DRBHCOMC76, price_DWL, price_ETH, price_GENTINGC51, price_MALAKOFC12, price_MALAKOFC13, price_MALAKOFC14, price_MALAKOFC16,
   price_MALAKOFC22, price_MALAKOFC23, price_MAYBANKC44, price_MAYBANKC45, price_MEDAINC, price_MERIDIAN,
   price_MMCCORPC12, price_MYSCM, price_PANPAGE, price_SAPNRGC68, price_SAPNRGC76, price_SGB)

all <- do.call(cbind, lapply(ls(patt="price_"), get))

# covariance matrix
range.names = names(all)
covmatrix = matrix(c(cov(all)), nrow=1002, ncol=1002)
dimnames(covmatrix) <-  list(range.names, range.names)
covmatrix

# write output
write.csv(covmatrix, file = "covmatrix.csv")
