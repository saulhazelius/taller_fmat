import re
import os
import sys
import glob
import shutil
import matplotlib.pyplot as plt
## creates histogram from experimental values
## 

atom = sys.argv[1] ## H or C shift values
bins = sys.argv[2]## specify bins for histogram 50, 100, 200, depending on shifts range 


di = os.getcwd() # current work dir
exp = di+'/experimental'

exfs = glob.glob(exp+'/*txt')


def get_exp():
	"""get the experimental shift values"""
	exp = []
	for file in exfs:
		f = open(file,'r')
		for line in f:
			if  not re.match("#",line) and line.split()[1] == atom: 
				if not line.split()[2] == '--' and not line.split()[2] == '*': 
					exp.append(float(line.split()[2])) #str to float for plotting
	return exp

def main():
	exp = get_exp()

	plt.hist(exp,bins=int(bins))
	plt.xlabel(str(atom)+' shifts (ppm)')
	plt.ylabel('Counts')
	plt.title('Shifts frequencies')
	plt.savefig('hist'+'_'+str(atom))

	if not 'plots' in os.listdir():

		os.mkdir('plots')

	shutil.move(di+'/hist_'+str(atom)+'.png',di+'/plots'+'/hist_'+str(atom)+'.png') ## complete path to overwrite file if file exists


main()

