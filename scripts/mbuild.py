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


def main(topX_context=1e4, minX=5e3, maxX =1e4, window=5e2, minline=0, maxline=5e5):
    topX_context = int(topX_context)
    topX_terms = int(maxX)
    minX = int(minX)
    maxX = int(maxX)
    minline = int(minline)
    maxline = int(maxline)
    srcpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    outpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    window = int(window)
    out_matrix = numpy.zeros((maxX-minX, topX_context),dtype=int)
#######    out_matrix = sparse.lil_matrix((maxX-minX, topX_context), dtype=int)
#######    srcpath = '/n/shokuji/dc/edg/deletethis/'
#######    outpath = '/n/shokuji/dc/edg/deletethis/'
    dict1 = {}
    #for file0 in os.listdir(srcpath):
     #   print file0
     #   print '\n'
#        with os.path.join(srcpath, file0) as file0:
#            text = file0.read()
    infile = open(os.path.join(outpath, 'corpus-2e4_lower.tok'),'r')
#    infile = open(os.path.join(outpath, 'corpus-2e4.tok'),'r')
#    out_matrix = scipy.io.mmread(os.path.join(outpath,'termterm_quicker2014_05_20.mtx')).tolil()
    line_count = 0
    for text in infile.xreadlines():
        line_count = line_count + 1
        if (line_count > minline)&(line_count <=maxline):
            if 1==1:
#            for (i,word0) in enumerate(contextList):
                for i in range(minX, maxX):
                    ii = i - minX
                    context = get_instances(text, str(i), window)
                    if context is not None:
                        for word1 in context:
                            j = int(word1)
                            if j < topX_context:
                                out_matrix[ii,j] = out_matrix[ii,j] + 1
#                            print str(j)
#                            open(os.path.join(outpath,'termterm1_quicker.txt'), 'a').write(str(out_matrix[ii,j]))
                if line_count%50000==1:
                    open(os.path.join(outpath,'termterm1_25e3_line'+str(minline)+'-'+str(minX)+'-'+str(maxX)+'.sparse.txt'), 'w').write(str(line_count))
                rem = int(1e5)
                if line_count%rem==1:
##                scipy.io.mmwrite(os.path.join(outpath,'termterm_25e3_true.mtx'), out_matrix)
##                open(os.path.join(outpath,'termterm_quicker.txt'), 'w').write(str(line_count))
##########                scipy.io.mmwrite(os.path.join(outpath,'termterm_25e3_true'+str(line_count)+'-'+str(minX)+'-'+str(maxX)+'.mtx'), out_matrix)
                    scipy.io.savemat(os.path.join(outpath,'termterm_25e3_true'+str(line_count)+'-'+str(minX)+'-'+str(maxX)+'.mat'), mdict={'termterm':out_matrix})
                    if line_count-2>minline+rem:
                        try:
                            os.remove(os.path.join(outpath,'termterm_25e3_true'+str(line_count-rem)+'-'+str(minX)+'-'+str(maxX)+'.mat'))
                        except:
                            pass
#        else:
#            if line_count==183201:
 #               out_matrix = scipy.io.loadmat(os.path.join(outpath,'termterm.mat'))
  #              out_matrix = out_matrix['termterm'].tolil()
   #             open(os.path.join(outpath,'termterm1_quicker.txt'), 'w').write(str(line_count))
###########    scipy.io.mmwrite(os.path.join(outpath,'termterm_25e3_true'+str(maxline)+'-'+str(minX)+'-'+str(maxX)+'.mtx'), out_matrix)
    scipy.io.savemat(os.path.join(outpath,'termterm_25e3_true'+str(maxline)+'-'+str(minX)+'-'+str(maxX)+'.mat'), mdict={'termterm':out_matrix})

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
    main(topX_context=1e4, minX=sys.argv[1], maxX =sys.argv[2], window=5e2, minline = sys.argv[3], maxline=sys.argv[4])
