#install.packages("ROAuth")
library(ROAuth)
library(twitteR)
api_key <- "XvVQsNpTZSLorkcht0ndsO3Wb"
api_secret <- "hFcXEdk3lyi8s0sP6xeAv5ns1wtUDTbH3fSBubcWH38eQZKGTf"
token <- "1536168896-xgL8sNgNuSUroWywj2Ev34REuFbS9oPyjmULYNh"
token_secret <- "o67cgzE9Ly3ehxh3T0elMgXYkOg2VeyNQMs8ftteQ9Kjw"
setup_twitter_oauth(api_key, api_secret, token, token_secret)
#terms<-c("flu","#usflu","#usinfluenza","#influenza","#H3N2","#H1N1","#flutests","#positiveflutest","#fluhospitalizations","#flumortality","#UnitedStatesflu","#fluepidemic","#statesflu","#flushot","#flu2018","#flu2017","#flu","usflu","usinfluenza","influenza","H3N2","H1N1","flutests","positiveflutest","fluhospitalizations","flumortality","UnitedStatesflu","fluepidemic","statesflu","flushot","flu2018","flu2017")
#terms_search <- paste(terms, collapse = " OR ")
tweets <- searchTwitter("flu OR usflu OR usinfluenza OR influenza OR H3N2 OR H1N1 OR flutests OR positiveflutest OR fluhospitalizations OR flumortality OR UnitedStatesflu OR fluepidemic OR statesflu OR flushot OR flu2018 OR flu2017", n = 500000, lang = "en")
tweets.df <-twListToDF(tweets)
write.csv(tweets.df, "tweets8.csv")

locTweets<-subset(tweets.df, is.na(tweets.df$longitude)==FALSE & is.na(tweets.df$latitude)==FALSE)
locTweets$state<-as.character(NA)
library(ggmap)
for (i in 1:nrow(locTweets)){
  geo_information <- revgeocode(c(as.numeric(locTweets$longitude[i]), as.numeric(locTweets$latitude[i])), output = "more")
  
  #print(geo_information$locality)
  #length(s1)
  (geo_information$administrative_area_level_1)
  locTweets$state[i]<-s1
}