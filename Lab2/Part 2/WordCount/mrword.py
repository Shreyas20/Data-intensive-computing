from mrjob.job import MRJob
import re
import nltk
from nltk.corpus import stopwords



class MRWordFreqCount(MRJob):

	def mapper(self, _, line):
		WORD_RE = re.compile(r"[\w']+")
		wl=WORD_RE.findall(line)
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
				continue
			yield (word, 1)

	def combiner(self, word, counts):
		yield (word, sum(counts))

	def reducer(self, word, counts):
		yield (word, sum(counts))


if __name__ == '__main__':
	MRWordFreqCount.run()
