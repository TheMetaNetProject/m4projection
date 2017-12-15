#!/bin/bash

#cat /proc/meminfo
cd /n/picnic/xw/metanet/corpora/EN/UKWaC-plaintext/unrasped4_out-small

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

java -cp /n/shokuji/dc/edg/semanticvectors-5.4.jar -Xms512m -Xmx2000m pitt.search.semanticvectors.VectorStoreTranslater -lucenetotext termtermvectors.bin unrasped4-small.mm