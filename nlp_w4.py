import nltk
from nltk.corpus import cmudict
from nltk.corpus import wordnet as wn

# names = nltk.corpus.names
# print(names.fileids())
# print(len(names.words('male.txt')))
# print(len(names.words('female.txt')))
#
# cfd = nltk.ConditionalFreqDist((fileid, name[-1]) for fileid in names.fileids() for name in names.words(fileid))
# cfd.plot()

entries = cmudict.entries()
#
# list = [w for w in cmudict.words()]
#
# fdlist = nltk.FreqDist(list)
#
# final_list = [w for w in fdlist.keys() if fdlist[w] > 1]
#
# print(len(final_list))
#
# #print(len(set(cmudict.words())))
#
# print(fdlist.most_common(1))

# syn = ['N','IH0','K','S']
#
# syn2 = ['S', 'K', 'IH0', 'N']
#
# result = [word for word,pron in entries if len(pron) >= 4 and pron[-4:] == syn]
#
# print(len(result))

# print(wn.synset('car.n.01').definition())
# print(wn.synset('car.n.01').examples())
#
# print(wn.synset('car.n.01').lemmas())

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print(types_of_motorcar)
lemma = [lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()]
print(lemma)

paths = motorcar.hypernym_paths()
print(len(paths))