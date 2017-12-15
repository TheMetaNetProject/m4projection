#!/bin/bash

#cat /proc/meminfo
cd /n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/sentences2_out

#export CLASSPATH=${CLASSPATH}:/n/shokuji/dc/edg/semanticvectors-5.4.jar
export _JAVA_OPTIONS="-Xms512m -Xmx2000m -XX:MaxPermSize=256m"
export JAVA_OPTS=-Xms512m -Xmx2000m -XX:MaxPermSize=256m
export JAVA_HOME=/l/local64/lang/jdk1.7.0_25
export PATH=/l/local64/lang/jdk1.7.0_25/bin
#export JAVA_HOME=/usr/lib/jvm/java-1.7.0
#export PATH=/usr/lib/jvm/java-1.7.0/bin
ulimit -v unlimited
ulimit -f unlimited

java -version

#java -cp /n/shokuji/dc/edg/semanticvectors-5.4.jar -Xms512m -Xmx2000m pitt.search.lucene.IndexFilePositions /n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/sentences2 -index /n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/sentences2_out/a
java -cp /n/shokuji/dc/edg/semanticvectors-5.4.jar -Xms512m -Xmx2000m pitt.search.semanticvectors.BuildPositionalIndex -windowradius 50 -luceneindexpath /n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/sentences2_out/positional_index -dimension 1000 -minfrequency 100

#java org.apache.lucene.demo.IndexFiles -docs /n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped -index /n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/lucene_index
#java pitt.search.semanticvectors.BuildIndex -luceneindexpath /n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/positional_index


exit $?