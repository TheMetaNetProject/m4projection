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

def main():
    #path_in ='C:/Users/Administrator/Documents/2692_out/'
    path_in = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped/'
    path_out = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/sentences2/'
    stoplist = set('for a of the and to in out have do'.split())
    for file0 in os.listdir(path_in):
        newpath = path_out+file0[:4]
        if (not os.path.exists(newpath))&(int(file0[:4])%3==0): 
	    os.makedirs(newpath)
	    i = 0;
            for line in open(os.path.join(path_in,file0)):
                i = i + 1
                if not os.path.exists(os.path.join(newpath, file0+str(i-1)+'.txt')):
                    line1 = [word for word in line.split() if word not in stoplist]
                    if len(line1)>2:
                        outfile = open(os.path.join(newpath, file0+str(i-1)+'.txt'),'w')
                        line2 = " ".join(line1)
                        outfile.write(line2+'\n')
                        outfile.close()

main()