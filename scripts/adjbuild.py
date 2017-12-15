#-------------------------------------------------------------------------------
# Name:        adjbuild
# Purpose: build a term-term vector for a given query term
#
# Author:      Administrator
#
# Created:     30/04/2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import os.path
import numpy
import scipy
import scipy.sparse as sparse
import scipy.io
import re
import collections
import sys


def main(adj, topX_context=1e4, window=5e2, minline=0, maxline=5e5):
    topX_context = int(topX_context)
    minline = int(minline)
    maxline = int(maxline)
    srcpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    outpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    vocab = [word.strip() for word in open(srcpath+'contextwords2e4-pos-clean-nonzero.txt','r').readlines()]
    adjind = vocab.index(adj)
    nouncodevec = numpy.zeros(len(vocab))
    for (i, word) in enumerate(vocab):
        if word[-1]=='n':
            nouncodevec[i] = 1
    nounlist = nounlistcreator(vocab)
    outfile = open(outpath+'nounlist-pos-clean-nonzero.txt','w')
    [outfile.write(word+'\n') for word in nounlist]
    outfile.close()
    print adj
    adjind  = vocab.index(adj)
    window = int(window)
    out_matrix = numpy.zeros((len(vocab), topX_context),dtype=int)
    dict1 = {}
    infile = open(os.path.join(outpath, 'corpus-2e4_lower_new-clean-nonzero.tok'),'r')
    line_count = 0
    adjcounts = numpy.zeros(len(vocab))
    for text in infile.xreadlines():
        line_count = line_count + 1
        if (line_count > minline)&(line_count <=maxline):
            words = [int(i) for i in text.split()]
            try:
                words = words[:100]
            except:
                pass
            lenwords = len(words)
            go = True
            while go:
                try:
                    a = words.index(adjind)
                    try:
                        word1 = words[a+1]
                        adjcounts[word1] = adjcounts[word1] + 1
                        isnoun = nouncodevec[word1]
                        if isnoun:
                            for word2 in words:
                                if word2 < topX_context:
                                    out_matrix[word1,word2] = out_matrix[word1,word2] + 1
                        del words[a]
                    except IndexError:
                        go = False
                except ValueError:
                    go = False
            if line_count%10000==1:
                open(os.path.join(outpath,'termterm_adj-'+adj+'-'+str(minline)+'-'+'.sparse.txt'), 'w').write(str(line_count))
            rem = int(1e6)
            if line_count%rem==1:
                scipy.io.mmwrite(os.path.join(outpath,'termterm_adj-'+adj+'-'+str(line_count)+'-'+'-nonzero.mtx'), out_matrix)
                if line_count-2>minline+rem:
                    try:
                        os.remove(os.path.join(outpath,'termterm_adj-'+adj+'-'+str(line_count-rem)+'-'+'-nonzero.mtx'), out_matrix)
                    except:
                        pass
    scipy.io.mmwrite(os.path.join(outpath,'termterm_adj-'+adj+'-'+str(maxline)+'-'+'-nonzero.mtx'), out_matrix)
    scipy.io.savemat(outpath+'adjcounts-'+adj+'.mat', {'adjcounts':adjcounts})
def indexx(list1, query):
    try:
        ind = list1.index(query)
    except IndexError:
        ind = -1

def get_instances(text, word, window):
    tokens = text.split()
    keyword = re.compile(word)
    context = []
    for index in range( len(tokens) ):
        if keyword.match( tokens[index] ):
            start = max(0, index-window)
            finish = min(len(tokens), index+window+1)
            context = context + tokens[start:index] + tokens[index+1:finish]
    return context

def file_to_list(filename):
    list1 = []
    for line in open(filename).readlines():
        list1 = list1.append(line.strip())
    return list1

def file_dict(filename):
    with open(filename) as f:
       passage = f.read()
    words = re.findall(r'\w+', passage)
    word_counts = collections.Counter(words)
    return word_counts

def combine_dicts(a, b, op=None):
    op = op or (lambda x, y: x + y)
    return dict(a.items() + b.items() +
        [(k, op(a[k], b[k])) for k in set(b) & set(a)])

def nounlistcreator(list1):
    list2 = [word for word in list1 if word[-1]=='n']
    return list2

if __name__ == '__main__':
    main(adj=sys.argv[1], topX_context=1e4, window=5e2, minline = 0, maxline = int(1e8))
