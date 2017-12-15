import subprocess
import time

time.sleep(int(60*60*8))
bashCommand = 'sbatch -p ai --mem 1000 mbuild2.sh'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)