#!/bin/bash
cd /n/picnic/xw/metanet/corpora/EN/UKWaC/rasp/
for file in *.gz
do 
    gunzip -c $file > /n/picnic/xw/metanet/corpora/EN/unzipped/$file
done
