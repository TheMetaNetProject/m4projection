import numpy
import sys
import scipy.io
from sklearn.decomposition import TruncatedSVD
from sklearn.pls import PLSRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
import warnings
import time
import os
from itertools import izip

variety = 'unrasped_out/'
basepath ='/n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/'+variety

def main(adj):
    print adj
    maxline = 100000000 # 77033733  # number of lines in our corpus
    adjpath = os.path.join(basepath,'termterm_adj-'+adj+'-'+str(maxline)+'-'+'-nonzero.mtx')
    vocabpath = basepath+'contextwords2e4-pos-clean-nonzero1.txt'
    nounpath = basepath + 'termterm-reduced.mat'
    modelpath = basepath + 'model.dump'
    corpuspath = basepath + 'corpus-2e4_lower_new-clean.tok'
    outmatpath = basepath+'PLScoefs.mat'
    outmodelpath = basepath+'PLSmodel.dump'
    adjcountpath = basepath + 'adjcounts-'+adj+'.mat'
    countpath = basepath + 'termcounts.mat'
    termcounts = scipy.io.loadmat(countpath)
    termcounts = termcounts['termcounts']
    vocab = [word.strip() for word in open(vocabpath,'r').readlines()]
    adjind = vocab.index(adj)
    try:
        adjcounts = scipy.io.loadmat(adjcountpath)
        adjcounts = adjcounts['adjcounts']
    except:
        adjcounts = adjcounter(adjind, corpuspath,vocab)
        scipy.io.savemat(adjcountpath, {'adjcounts':adjcounts})
    adjnouns = scipy.io.mmread(adjpath)
    try:
        adjnouns = scipy.io.loadmat(basepath+'termterm-pmi-adj-'+adj+'-nonzero.mat')
        adjnouns = adjnouns['adjnouns']
    except:
        adjnouns = pmi(adjnouns, termcounts, adjcounts)
        scipy.io.savemat(basepath+'termterm-pmi-adj-'+adj+'-nonzero.mat',{'adjnouns':adjnouns})
    a = scipy.io.loadmat(basepath+'termterm-pmi.mat')
    print 'a'
    a = numpy.shape(a['termterm'])
    nouninds = numpy.zeros((len(vocab),1))
    print 'b'
    for (i,word) in enumerate(vocab):
        if word[-1]=='n':
	    nouninds[i] = 1
    nouninds = nouninds[:a[0]]
    adjnouns = adjnouns[numpy.nonzero(nouninds)[0],:]
    adjnouns1 = adjnouns[:a[0],:]
    adjnouns1 = adjnouns1[:,:a[1]]
    nouns = scipy.io.loadmat(nounpath)
    nouns = nouns['termterm']
    nouns = nouns[numpy.nonzero(nouninds)[0],:]
    with open(modelpath,'rb') as input:
       model = pickle.load(input)
    print 'c'
    adj_matrix_proj = model.transform(adjnouns1)  #numpy.zeros(numpy.shape(a))
#   # for i in range(numpy.shape(a)[0]):
#   #     row1 = model.transform(adjnouns1[i,:])
#   #     adj_matrix_proj[i,:] = row1
#    adj_matrix_proj = model.transform(adjnouns1)
    print 'd'
    pls = PLSRegression(n_components=50)
    pls.fit(nouns, adjnouns)
    print 'e'
    A = pls.coefs
    scipy.io.savemat(outmatpath,{'PLS':A})
    with open(outmodelpath,'wb') as outfile:
        pickle.dump(pls,outfile)

def pmi(matrix, termcounts, contextcounts):
    outmatrix = numpy.zeros((numpy.size(matrix,0), numpy.size(matrix,1)))
  # computes the positive pointwise mutual information
#    numpy.seterr(all='warn')
    total = numpy.sum(termcounts)
    for j in range(numpy.size(matrix,1)):
        open('/n/shokuji/dc/edg/svd.txt','w').write(str(j))
        for i in range(numpy.size(matrix,0)):
            if matrix[i,j]>0:
                if (termcounts[i]>0)&(contextcounts[j]>0):
                    ppmi = numpy.log(matrix[i,j]) + numpy.log(total) - numpy.log(termcounts[i]) - numpy.log(contextcounts[j])
                    if ppmi > 0:
                        outmatrix[i,j] = ppmi
    return outmatrix

def adjcounter(adjind, corpuspath, vocab):
    infile = open(corpuspath,'r')
    adjcounts = numpy.zeros(len(vocab))
    for text in infile.xreadlines():
        go = True
        while go:
            try:
                a = words.index(adjind)
                try:
                    word1 = words[a+1]
                    adjcounts[word1] = adjcounts[word1]+1
                    del words[a]
                except IndexError:
                    go = False
            except:
                go = False
    return adjcounts
if __name__ == '__main__':
    main(adj=sys.argv[1])