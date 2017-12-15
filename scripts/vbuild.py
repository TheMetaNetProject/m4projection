#-------------------------------------------------------------------------------
# Name:        vbuild
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
import numpyu
import scipy
import scipy.sparse as sparse
import scipy.io
import re
import collections
import sys


def main(query1, query2, topX_context=1e4, window=5e2, minline=0, maxline=5e5):
    topX_context = int(topX_context)
    minline = int(minline)
    maxline = int(maxline)
    srcpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    outpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    vocab = [word.strip() for word in open(srcpath+'contextwords2e4-pos-clean-nonzero.txt','r').readlines()]
    query1 = vocab.index(query1)
    query2 = vocab.index(query2)
    window = int(window)
    out_matrix = numpy.zeros((1, topX_context),dtype=int)
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
            go = True
            while go:
                try:
                    a = words.index(query1)
                    try:
                        if words[a+1]==query2:
                            for word2 in words:
                                if word2 < topX_context:
                                    out_matrix[word2] = out_matrix[word2] + 1
                    except IndexError:
                        go = False
                    del words[a]
                except ValueError:
                    go = False
            if line_count%10000==1:
                open(os.path.join(outpath,'termterm_'+query1+'-'+query2+'-'+str(minline)+'-'+'.sparse.txt'), 'w').write(str(line_count))
            rem = int(1e5)
            if line_count%rem==1:
                scipy.io.mmwrite(os.path.join(outpath,'termterm_'+query1+'-'+query2+'-'+str(line_count)+'-'+'-nonzero.mtx'), out_matrix)
#                scipy.io.savemat(os.path.join(outpath,'termterm_2e4-'+str(line_count)+'-'+'-nonzero.mat'), mdict={'termterm':out_matrix})
                if line_count-2>minline+rem:
                    try:
                        os.remove(os.path.join(outpath,'termterm_'+query1+'-'+query2+'-'+str(line_count-rem)+'-'+'-nonzero.mtx'), out_matrix)
#                        os.remove(os.path.join(outpath,'termterm_2e4-'+str(line_count-rem)+'-'+'-nonzero.mat'))
                    except:
                        pass
#    scipy.io.savemat(os.path.join(outpath,'termterm_2e4-'+str(maxline)+'-'+'-nonzero.mat'), mdict={'termterm':out_matrix})
    scipy.io.mmwrite(os.path.join(outpath,'termterm_'+query1+'-'+query2+'-'+str(maxline)+'-'+'-nonzero.mtx'), out_matrix)
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
    main(query1=sys.argv[1], query2 = sys.argv[1], topX_context=1e4, window=5e2, minline = 0, maxline = int(1e8))
    #minline = sys.argv[2], maxline=sys.argv[3])
