import os
print("\n*******Getting NYT articles using API********\n")
#os.system("python getArticle.py")

print("\n\n**********Getting NYT articles using API********\n\n")
#os.system("python getTweets.py")

print("\n\n************Word count for weekly tweets******\n\n")
os.system("python /home/shreyas/mrword.py /home/shreyas/stweetsweek.txt -r hadoop --hadoop-tmp-dir=file:///home/shreyas/temp/  > tweetWeekWordCount.txt")

print("Word count for Daily tweets")
os.system("python /home/shreyas/mrword.py /home/shreyas/tweetsday.txt -r hadoop --hadoop-tmp-dir=file:///home/shreyas/temp/  > tweetDayWordCount.txt")

print("Word count for weekly NYT articles")
os.system("python /home/shreyas/mrword.py /home/shreyas/nytarticlesweek.txt -r hadoop --hadoop-tmp-dir=file:///home/shreyas/temp/  > NYTWeekWordCount.txt")

print("Word count for Daily NYT articles")
os.system("python /home/shreyas/mrword.py /home/shreyas/nytarticlesday.txt -r hadoop --hadoop-tmp-dir=file:///home/shreyas/temp/  > NYTDayWordCount.txt")

print("Get top 10 words in txt file csv for word cloud of 50 words for tweetWeek")
os.system("python top10extract.py")

print("Get top 10 words in txt file csv for word cloud of 50 words for tweetday")
os.system("python top10extract.py")

print("Get top 10 words in txt file csv for word cloud of 50 words for NYTWeek")
os.system("python top10extract.py")

print("Get top 10 words in txt file csv for word cloud of 50 words for NYTday")
os.system("python top10extract.py")

print("Co-occurance for Tweeter data")
os.system("python /home/shreyas/cooc1.py /home/shreyas/tweetsday.txt -r hadoop --hadoop-tmp-dir=file:///home/shreyas/temp/  > coocTweet.txt")

print("Co-occurance for Tweeter data")
os.system("python /home/shreyas/coocNYT.py /home/shreyas/nytarticlesday.txt -r hadoop --hadoop-tmp-dir=file:///home/shreyas/temp/  > coocNYT.txt")

print("Removing duplicated and collecting top 10 pairs in a csv")
os.system("python removeRepeatsPairs.py")
