from mrjob.job import MRJob
import re
import nltk
from nltk.corpus import stopwords

class MRWordFreqCount(MRJob):


	def mapper(self, _, line):
		para=re.split(r'\n+', line)
		f=open('/home/shreyas/top10wordsNYT.txt','r')
		l=f.read()
		f.close()
		top10=l.split('\n')

		for p in range(0,len(para)):

			WORD_RE = re.compile(r"[\w']+")
			wl=WORD_RE.findall(para[p])
			wl=[x.lower() for x in wl]
			wl=[x for x in wl if not any(c.isdigit() for c in x)]
			wl = [i for i in wl if len(i) > 1]
			bl=['advertise']
			B=re.compile('|'.join([re.escape(word) for word in bl]))
			wl=[word for word in wl if not B.search(word)]
			wl = [x.replace('_', '').replace("'",'') for x in wl]
			sr = stopwords.words('english')
			for word in wl:
				if word in sr:
					wl.remove(word)
			n=0
	    #print(n)
			while n<len(wl):
	        #n+=1
	        #print(n)
				for i in range(n,len(wl)):
	            #print("a",n)
					n+=1
					if wl[i] in top10:
						word1=wl[i]
	                #print(word)
						for j in range(n,len(wl)):
							if wl[j] in top10:
								word2=wl[j]
	                        #print(word2)
								if word2==word1:
									continue
								yield ((word1, word2), 1)

	def combiner(self, word, counts):
		yield (word, sum(counts))

	def reducer(self, word, counts):
		yield (word, sum(counts))


if __name__ == '__main__':
	MRWordFreqCount.run()
