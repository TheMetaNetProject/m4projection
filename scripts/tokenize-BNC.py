#-------------------------------------------------------------------------------
# Name:       tokenize_BNC
# Purpose: creates a version of the BNC corpus where every word token is replaced by its index in an inputted vocab list
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
import time

def tokenize():
    outfilename = 'BNC-2e4-lower-new-clean-nonzero.tok'
    posfilename = 'BNC-2e4-lower-new-clean-nonzero.pos'
    variety = 'unrasped'
#    variety = 'sentences2'
    srcpath = '/n/picnic/xw/metanet/corpora/EN/bnc-xml/'
    pospath = '/n/picnic/xw/metanet/corpora/EN/bnc-pos/pos-out/' # path for the intermediate pos file
    outpath = '/n/picnic/xw/metanet/corpora/EN/bnc-pos/tokenized-out/'
    listpath = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped_out/'
    vocablist = file_to_list(listpath+'contextwords2e4-pos-clean-nonzero1.txt') #was file_to_list(os.path.join(listpath,'contextwords2e4_pos-clean.txt')) but trying a new option
    outfile = open(os.path.join(outpath, outfilename),'a')
    posfile = open(os.path.join(pospath, posfilename),'a')
    doc_counter = 0
    line_counter = 0
    for root, dir, files in os.walk(srcpath):
#        print file0
 #       print '\n'
        for file0 in files:
            file00 = os.path.join(root,file0)
            if os.path.isfile(file00):
                f = open(file00)
                for text in f.readlines():
################################################                with open(file00) as file1:
################################################                    text = file1.read()
                    a = ''
                    text = text.lower()
                    posout = ''
                    for word in text.split('<w'):
                        try:
                            pos = word[5]
                            word = word[word.find('hw="')+len('hw="'):]
                            word = word[:word.find('"')]+'_'+pos
                            try:
                                a = a + ' ' + str(vocablist.index(word))
                            except ValueError:
                                pass
                            posout = posout +' ' + word
                        except:
                            pass
                    posfile.write(posout+'\n')
                    outfile.write(a+'\n')
                    line_counter = line_counter + 1                
                doc_counter = doc_counter + 1
                outfile.close()
                outfile = open(os.path.join(outpath, outfilename),'a')
                open(os.path.join(outpath, outfilename+'.iters2'),'w').write(str(doc_counter)+'\t'+str(line_counter))
    outfile.close()

def get_instances(text, word):
    tokens = text.split()
    text = a.read()
    keyword = re.compile(word)
    context = []
    for index in range( len(tokens) ):
        if keyword.match( tokens[index] ):
            start = max(0, index-window)
            finish = min(len(tokens), index+window+1)
            context = context + tokens[start:index] + tokens[index+1:finish]

def file_to_list(filename):
    list1 = []
    for line in open(filename).readlines():
        try:
            list1.append(line.strip())
        except:
            pass
    return list1

if __name__ == '__main__':
    tokenize()
