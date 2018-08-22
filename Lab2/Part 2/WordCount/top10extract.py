file1=input("Enter 1. for NYT day\n2. for NYT week\n 3. for twitter day\n 4. for twitter week\n")
if file1=='4':
    filename="tweetWeekWordCount.txt"
elif file1=='3':
    filename="tweetDayWordCount.txt"
elif file1=='2':
    filename="NYTWeekWordCount.txt"
elif file1=='1':
    filename="NYTDayWordCount.txt"

import pandas as pd
data = pd.read_csv(filename, sep="\t", header=None)
data.columns = ['word', 'count']
df_sort=data.sort_values('count',ascending=False)
top50=df_sort.head(50)
cloudfile=input("Enter filename for wordcloud with csv extension:\n")

top50.to_csv(cloudfile, header=True, index=False, sep='\t', mode='a')

top10=df_sort.head(10)
top10words=top10['word']
dw=input("Day(d) or week(w)?\n")
if dw=="d":
    choice=input("Tweets(T) or articles(A)?\n")
    if choice=="T" or choice=="t":
        top10file="top10wordstweets.txt"
    elif choice=="A" or choice=="a":
        top10file="top10wordsNYT.txt"

    top10words.to_csv(top10file, header=False, index=False, sep='\t', mode='a')
else:
    print("Bye")
