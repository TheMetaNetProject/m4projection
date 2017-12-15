#-------------------------------------------------------------------------------
# Name:        sentences.py
# Purpose:
#
# Author:      E.D. Gutierrez (edg@icsi.berkeley.edu)
#
# Created:     18 Apr 2014
#
# Copyright:   Not subject to copyright.
#-------------------------------------------------------------------------------
import os
import os.path
import shutil

def main():
    #path_in ='C:/Users/Administrator/Documents/2692_out/'
    path_in = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped/'
    path_out = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped3/'
    stoplist = set('for a of the and to in out have do'.split())
    for file0 in os.listdir(path_in):
        if int(file0[3:4])%2==0:
            dstpath = os.path.join(path_out, file0)
            srcpath = os.path.join(path_in, file0)
            outfile = open(dstpath,'w')
            line2 = ''
            for line in open(srcpath, 'r').readlines():
                line1 = [word for word in line.split() if word not in stoplist]
                line2 = line2+ " ".join(line1)+'\n'
            outfile.write(line2)
            outfile.close()
main()