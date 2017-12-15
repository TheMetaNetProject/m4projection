#-------------------------------------------------------------------------------
# Name:        mbuild
# Purpose: build a term-term matrix
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


def main(topX_context=1e4, maxX =1e4, window=5e2, minline=0, maxline=5e5):
    topX_context = int(topX_context)
    topX_terms = int(maxX)
    maxX = int(maxX)
    minline = int(minline)
    maxline = int(maxline)
    srcpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    outpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    window = int(window)
    out_matrix = numpy.zeros((maxX, topX_context),dtype=int)
    dict1 = {}
    infile = open(os.path.join(outpath, 'corpus-2e4_lower_new-clean-nonzero.tok'),'r')
    line_count = 0
    for text in infile.xreadlines():
        line_count = line_count + 1
        if (line_count > minline)&(line_count <=maxline):
            words = [int(i) for i in text.split()]
            try:
                words = words[:100]
            except:
                pass
            lenwords = len(words)
            for (i,word1) in enumerate(words):
                for j in range(i+1, lenwords):
                    word2 = words[j]
                    if word1 < maxX:
                        if word2 < topX_context:
                            out_matrix[word1, word2] = out_matrix[word1, word2] + 1
                    if word2 < maxX:
                        if word1 < topX_context:
                            out_matrix[word2, word1] = out_matrix[word2, word1] + 1
            if line_count%10000==1:
                open(os.path.join(outpath,'termterm_2e4-'+str(minline)+'-'+str(maxX)+'.sparse.txt'), 'w').write(str(line_count))
            rem = int(1e5)
            if line_count%rem==1:
                scipy.io.mmwrite(os.path.join(outpath,'termterm_2e4-'+str(line_count)+'-'+str(maxX)+'-nonzero.mtx'), out_matrix)
#                scipy.io.savemat(os.path.join(outpath,'termterm_2e4-'+str(line_count)+'-'+str(maxX)+'-nonzero.mat'), mdict={'termterm':out_matrix})
                if line_count-2>minline+rem:
                    try:
                        os.remove(os.path.join(outpath,'termterm_2e4-'+str(line_count-rem)+'-'+str(maxX)+'-nonzero.mtx'), out_matrix)
#                        os.remove(os.path.join(outpath,'termterm_2e4-'+str(line_count-rem)+'-'+str(maxX)+'-nonzero.mat'))
                    except:
                        pass
#    scipy.io.savemat(os.path.join(outpath,'termterm_2e4-'+str(maxline)+'-'+str(maxX)+'-nonzero.mat'), mdict={'termterm':out_matrix})
    scipy.io.mmwrite(os.path.join(outpath,'termterm_2e4-'+str(maxline)+'-'+str(maxX)+'-nonzero.mtx'), out_matrix)
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

if __name__ == '__main__':
    main(topX_context=1e4, maxX =sys.argv[1], window=5e2, minline = sys.argv[2], maxline=sys.argv[3])
