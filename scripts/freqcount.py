#-------------------------------------------------------------------------------
# Name:        freqs
# Purpose: find the frequencies of a given list of words
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
import scipy.io
import re
import collections
import sys


def main():
    minline = 0
    maxline = int(77033733)
    vocsize = int(2e4)
    outlist = open('/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/contextwords2e4-pos-clean-nonzero.txt','w')
    srcpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    outpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    out_matrix = numpy.zeros(vocsize,dtype=float)
    infile = open(os.path.join(outpath, 'corpus-2e4-lower-clean-nonzero.tok'),'r')
    line_count = 0
    for text in infile.xreadlines():
        line_count = line_count + 1
        if (line_count > minline)&(line_count <=maxline):
            for item in text.split():
                out_matrix[int(item)] = out_matrix[int(item)]+1
        if line_count%1000000==1:
            scipy.io.savemat(os.path.join(outpath,'termcounts2-nonzero.mat'), mdict={'termcounts':out_matrix})
            open('/n/shokuji/dc/edg/u.txt','w').write(str(line_count))
    scipy.io.savemat(os.path.join(outpath,'termcounts-nonzero.mat'), mdict={'termcounts':out_matrix})
    listfile = open('/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/contextwords2e4_pos-clean.txt','r')
    for (i,line) in enumerate(listfile.readlines()):
        if out_matrix[i]>=50:
            outlist.write(line)
    outlist.close
        
def combine_dicts(a, b, op=None):
    op = op or (lambda x, y: x + y)
    return dict(a.items() + b.items() +
        [(k, op(a[k], b[k])) for k in set(b) & set(a)])

if __name__ == '__main__':
    main()
