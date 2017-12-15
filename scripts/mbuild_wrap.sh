#!/bin/bash

sbatch -p gen --mem 3700 mbuild.sh 0 1000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 1000 2000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 2000 3000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 3000 3700 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 3700 5000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 5000 6000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 6000 7000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 7000 8000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 8000 9000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 9000 10000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 0 1000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 1000 2000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 2000 3000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 3000 3700 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 3700 5000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 5000 6000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 6000 7000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 7000 8000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 8000 9000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 9000 10000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 0 1000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 1000 2000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 2000 3000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 3000 3700 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 3700 5000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 5000 6000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 6000 7000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 7000 8000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 8000 9000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 9000 10000 3500000 3700000


sbatch -p gen --mem 3700 mbuild.sh 10000 11000 0 500000
sbatch -p gen --mem 3700 mbuild.sh 11000 12000 0 500000
sbatch -p gen --mem 3700 mbuild.sh 12000 13000 0 500000
sbatch -p gen --mem 3700 mbuild.sh 13000 13700 0 500000
sbatch -p gen --mem 3700 mbuild.sh 13700 15000 0 500000

sbatch -p gen --mem 3700 mbuild.sh 10000 11000 500000 1000000
sbatch -p gen --mem 3700 mbuild.sh 11000 12000 500000 1000000
sbatch -p gen --mem 3700 mbuild.sh 12000 13000 500000 1000000
sbatch -p gen --mem 3700 mbuild.sh 13000 13700 500000 1000000
sbatch -p gen --mem 3700 mbuild.sh 13700 15000 500000 1000000

sbatch -p gen --mem 3700 mbuild.sh 10000 11000 1000000 1500000
sbatch -p gen --mem 3700 mbuild.sh 11000 12000 1000000 1500000
sbatch -p gen --mem 3700 mbuild.sh 12000 13000 1000000 1500000
sbatch -p gen --mem 3700 mbuild.sh 13000 13700 1000000 1500000
sbatch -p gen --mem 3700 mbuild.sh 13700 15000 1000000 1500000

sbatch -p gen --mem 3700 mbuild.sh 10000 11000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 11000 12000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 12000 13000 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 13000 13700 2000000 2500000
sbatch -p gen --mem 3700 mbuild.sh 13700 15000 2000000 2500000

sbatch -p gen --mem 3700 mbuild.sh 10000 11000 2500000 3000000
sbatch -p gen --mem 3700 mbuild.sh 11000 12000 2500000 3000000
sbatch -p gen --mem 3700 mbuild.sh 12000 13000 2500000 3000000
sbatch -p gen --mem 3700 mbuild.sh 13000 13700 2500000 3000000
sbatch -p gen --mem 3700 mbuild.sh 13700 15000 2500000 3000000

sbatch -p gen --mem 3700 mbuild.sh 10000 11000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 11000 12000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 12000 13000 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 13000 13700 3000000 3500000
sbatch -p gen --mem 3700 mbuild.sh 13700 15000 3000000 3500000

sbatch -p gen --mem 3700 mbuild.sh 10000 11000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 11000 12000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 12000 13000 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 13000 13700 3500000 3700000
sbatch -p gen --mem 3700 mbuild.sh 13700 15000 3500000 3700000

exit $?