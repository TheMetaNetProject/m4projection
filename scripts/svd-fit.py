#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     27/05/2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy
import scipy.io
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
import warnings
import time

variety = 'unrasped_out/'
basepath ='/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/'+variety
phase = 1

def main(phase):
#    time.sleep(60*60*4)
    corpuspath = basepath + 'termterm_2e4-77033733-18000-nonzero.mtx'
    pmipath = basepath + 'termterm-pmi-nonzero.mat'
    countpath = basepath + 'termcounts-nonzero.mat'
    outtermpath = basepath + 'termterm-reduced-nonzero.mat'
    modelpath = basepath + 'model-nonzero.dump'
    if phase <= 0:
        termterm = scipy.io.mmread(corpuspath).astype(float)
        scipy.io.savemat('/n/shokuji/dc/edg/t.mat',{'a':termterm[0,:]})
        termcounts = scipy.io.loadmat(countpath)
        termcounts = termcounts['termcounts']
        termcounts1 = numpy.copy(termcounts)
##      ##    termcounts1 = termcounts[:(numpy.size(termterm,0))]
##      ##    vv = numpy.size(termcounts,0)<=1
##      ##    nonzeros1 = numpy.where(termcounts1>=50)[vv]
##      ##    termterm = termterm[nonzeros1, :]
        termcounts2 = numpy.copy(termcounts1)
        termcounts2 = termcounts2[:numpy.size(termterm,1)]
##      ##  nonzeros2 = numpy.where(termcounts2>=50)[vv]
##      ##  termterm = termterm[:,nonzeros2]
##      ##  corpus = numpy.copy(termterm[:,:1000])
##      ##  corpus = corpus[:1000,:]
##      ##  scipy.io.savemat('/n/shokuji/dc/edg/tinycorpus.mat',{'termterm':corpus}) 
##      ##  termterm = pmi(termterm, termcounts1[nonzeros1])
        termterm = pmi(termterm, termcounts1)
        scipy.io.savemat(pmipath, {'termterm':termterm})
    else:
        termterm = scipy.io.loadmat(pmipath)
        termterm = termterm['termterm']
#    termterm = termterm[:,:]
#    termterm = termterm[:,:]
#    termterm2 = termterm[:100,:]
 #   termterm2 = termterm2[:,:100]
#    scipy.io.savemat('/n/shokuji/dc/edg/tinytermterm.mat',{'termterm':termterm2})
    termterm = termterm[:,:9543]
    model = TruncatedSVD(n_components=300).fit(termterm)
    X_proj = model.transform(termterm)
    scipy.io.savemat(outtermpath, {'termterm':X_proj})
    with open(modelpath, 'wb') as output:
        pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)

def pmi(matrix, termcounts):
    outmatrix = numpy.zeros((numpy.size(matrix,0), numpy.size(matrix,1)))
  # computes the positive pointwise mutual information
#    numpy.seterr(all='warn')
    total = numpy.sum(termcounts)
    for j in range(numpy.size(matrix,1)):
        open('/n/shokuji/dc/edg/svd.txt','w').write(str(j))
        for i in range(numpy.size(matrix,0)):
            if matrix[i,j]>0:
                if (termcounts[i]>0)&(termcounts[j]>0):
                    ppmi = numpy.log(matrix[i,j]) + numpy.log(total) - numpy.log(termcounts[i]) - numpy.log(termcounts[j])
                    if ppmi > 0:
                        outmatrix[i,j] = ppmi
    return outmatrix
        
if __name__ == '__main__':
    main(phase)
