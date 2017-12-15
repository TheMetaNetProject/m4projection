#!/bin/bash

export PATH=/l/local64/lang/python-2.7.3/bin/

ulimit -f unlimited

python tokenize.py

exit $?