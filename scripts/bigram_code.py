import nltk
import string
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
f = open('laverdad_21000.txt','r')
lines = f.readlines()
words =[]
for line in lines:
    linewords = line.split()
    for word in linewords:
        word1 = nltk.clean_html(word)
        word1 = word1.translate(string.maketrans("",""), string.punctuation)
        word1 = word1.lower()
        words.append(word1)

laverdad = BigramCollocationFinder.from_words(words)
laverdad.apply_freq_filter(20)
laverdad_bigrams = laverdad.nbest(bigram_measures.pmi, 25)
laverdad = TrigramCollocationFinder.from_words(words)
laverdad.apply_freq_filter(20)
laverdad_trigrams = laverdad.nbest(trigram_measures.pmi, 25)

f = open('lajornadadezacatecas_0.txt','r')
lines = f.readlines()
words =[]
for line in lines:
    linewords = line.split()
    for word in linewords:
        word1 = nltk.clean_html(word)
        word1 = word1.translate(string.maketrans("",""), string.punctuation)
        word1 = word1.lower()
        words.append(word1)

lajornada =BigramCollocationFinder.from_words(words)
lajornada.apply_freq_filter(20)
lajornada_bigrams = lajornada.nbest(bigram_measures.pmi, 25)
lajornada =TrigramCollocationFinder.from_words(words)
lajornada.apply_freq_filter(20)
lajornada_trigrams = lajornada.nbest(trigram_measures.pmi, 25)

f = open('genteypoder_1.txt','r')
lines = f.readlines()
words =[]
for line in lines:
    linewords = line.split()
    for word in linewords:
        word1 = nltk.clean_html(word)
        word1 = word1.translate(string.maketrans("",""), string.punctuation)
        word1 = word1.lower()
        words.append(word1)

genteypoder =BigramCollocationFinder.from_words(words)
genteypoder.apply_freq_filter(20)
genteypoder_bigrams = genteypoder.nbest(bigram_measures.pmi, 25)
genteypoder =TrigramCollocationFinder.from_words(words)
genteypoder.apply_freq_filter(20)
genteypoder_trigrams = genteypoder.nbest(trigram_measures.pmi, 25)

f = open('elsol_100M_words_new_d.txt','r')
lines = f.readlines()
words =[]
for line in lines:
    linewords = line.split()
    for word in linewords:
        word1 = nltk.clean_html(word)
        word1 = word1.translate(string.maketrans("",""), string.punctuation)
        word1 = word1.lower()
        words.append(word1)

elsol =BigramCollocationFinder.from_words(words)
elsol.apply_freq_filter(20)
elsol_bigrams = elsol.nbest(bigram_measures.pmi, 25)
elsol =TrigramCollocationFinder.from_words(words)
elsol.apply_freq_filter(20)

elsol_trigrams = elsol.nbest(trigram_measures.pmi, 25)
