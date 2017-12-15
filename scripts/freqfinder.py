#-------------------------------------------------------------------------------
# Name:        freqfinder
# Purpose: finds the topX most frequent words in a corpus
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
import scipy.io
import re
import collections

def main(topX=2e4):
    topX = int(topX)
    srcpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped/'
    outpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/'
#    outpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped4_out/'
#    srcpath = '/n/shokuji/dc/edg/deletethis/'
#    outpath = '/n/shokuji/dc/edg/deletethis/'
    dict1 = {}
    filecount = 0
    for file0 in os.listdir(srcpath):
        if filecount < 20000:
            print filecount
            print '\n'
            dict2 = file_dict(os.path.join(srcpath,file0))
            dict1 = combine_dicts(dict1, dict2)
            dict1 = dict(collections.Counter(dict1).most_common(int(topX*1.7)))
            dict3 = collections.Counter(dict1).most_common(topX)
            outfile = open(os.path.join(outpath, 'contextwords.txt'),'w')
            for word in dict3:
                outfile.write(word[0]+'\n')
            filecount = filecount + 1
            outfile.close()   
    dict1 = collections.Counter(dict1).most_common(topX)
    outfile = open(os.path.join(outpath, 'contextwords2e4_pos.txt'),'w')
    for word in dict1:
        outfile.write(word[0]+'\n')
    outfile.close()

def file_dict(filename):
    with open(filename) as f:
       passage = f.read()
    passage = passage.lower()
    words = re.findall(r'\w+', passage)
    word_counts = collections.Counter(words)
    return word_counts

def combine_dicts(a, b, op=None):
    op = op or (lambda x, y: x + y)
    return dict(a.items() + b.items() +
        [(k, op(a[k], b[k])) for k in set(b) & set(a)])

if __name__ == '__main__':
    main()
