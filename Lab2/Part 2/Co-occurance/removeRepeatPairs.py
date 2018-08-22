import pandas as pd
choice1=input("Tweets(T) or articles(A)?\n")
if choice1=="T" or choice1=="t":
    coocfile="coocTweet.txt"
elif choice1=="A" or choice1=="a":
    coocfile="coocNYT.txt"

data1 = pd.read_csv(coocfile, sep="\t", header=None)
data1.columns = ['wordpair', 'count']

from ast import literal_eval
droplist=[]
for i in range(0,len(data1)):
    for j in range(i,len(data1)):
        a=literal_eval(data1['wordpair'][i])
        b=literal_eval(data1['wordpair'][j])
        #print(a,b)

        if (a[0]==b[1] and b[0]==a[1]):
#             print("yes")
#             print(data1['count'][i])
#             print(data1['count'][j])
            data1['count'][i]=data1['count'][i]+data1['count'][j]
            droplist.append(j)

#print(droplist)
data1=data1.drop(data1.index[droplist])
df_sort1=data1.sort_values('count',ascending=False)
top50cooc=df_sort1.head(10)
cloudfile=input("Enter filename for wordcloud with csv extension")

top50cooc.to_csv(cloudfile, header=True, index=False, sep='\t', mode='a')

#print(len(data1))
if choice1=="T" or choice1=="t":
    coocfileRR="coocTweetRR.txt"
elif choice1=="A" or choice1=="a":
    coocfileRR="coocNYTRR.txt"

data1.to_csv(coocfileRR, header=False, index=False, sep='\t', mode='a')
