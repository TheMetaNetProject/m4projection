#-------------------------------------------------------------------------------
# Name:        unparse
# Purpose:     Convert corpus from RASP XML to token_pos format
#
# Author:      Administrator
#
# Created:     16/04/2014
# Copyright:   (c) Administrator 2014
# License:     none
#-------------------------------------------------------------------------------
import os
import os.path

def main():
    path_in ='/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unzipped/'
    path_out = '/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped/'
    #path_in ='C:/Users/Administrator/Documents/2692/'
    #path_out ='C:/Users/Administrator/Documents/2692_out/'
    for file0 in os.listdir(path_in):
        infile = open(os.path.join(path_in,file0),'r')
        outfile =open(os.path.join(path_out,file0+'.txt'),'w')
        print file0
        for line in infile.readlines():
            strout = ''
            line1 = line
            start_indx = line1.find('lem=')
            while start_indx>-1:
                line1 = line1[(start_indx+5):]
                end_indx = line1.find("'")
                str1 = line1[:end_indx]
                strout = strout + str1 + '_'
                line1 = line1[end_indx:]
                start_indx = line1.find('pos=')
                str1 = line1[(start_indx+5):(start_indx+6)]
                if str1.lower() == 'n':
                    try:
                        if line1[(start_indx+6)+(start_indx+7)].lower()=='p':  #handle proper nouns
                            str1 = 'x'
                    except:
                        pass
                strout = strout + str1 + ' '
                line1 = line1[(start_indx+6):]
                start_indx = line1.find('lem=')
            if len(strout)>0:
                outfile.write(strout+'\n')
        outfile.close()



main()

