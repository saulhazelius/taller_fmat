import re
import os
import sys
import glob
import shutil
import matplotlib.pyplot as plt
## creates a plot of calculated vs experimental values

base = sys.argv[1] ## base method 1 or 2 
atom = sys.argv[2] ## C or H
di = os.getcwd()
exp = di+'/experimental'
calc = di+'/calculated'
nb = calc+'/base'+str(base)

nbfiles = glob.glob(nb+'/*out')
exfs = glob.glob(exp+'/*txt')

def get_calc():
	"""get calculated values"""
	spec = []
	for file in sorted(nbfiles):
		f = open(file,'r')
		for line in f:
			if re.search('sotropic',line) and re.search(atom,line) and not re.search('Cl',line) and not re.search('olar',line): # avoid Cl 
				iso = round(float(line.split()[4]),1)
				spec.append(iso)
		f.close()
	return spec 


def get_exp():
        """get the experimental shift values"""
        exp = []
        for file in sorted(exfs):
                f = open(file,'r')
                for line in f:
                        if  not re.match("#",line) and line.split()[1] == atom:
                                if not line.split()[2] == '--' and not line.split()[2] == '*':
                                        exp.append(float(line.split()[2])) #str to float for plotting
                                if line.split()[2] == '--' or line.split()[2] == '*':
                                        exp.append(exp[-1])	
                f.close()
        return exp


def main():
	spec = get_calc()
	exp = get_exp()

	plt.scatter(exp,spec)
	plt.xlabel('Experimental shifts (ppm)')	
	plt.ylabel('Calculated isotropic values (ppm)')	
	plt.title(str(atom)+' base '+str(base))
	plt.savefig('plot_base_'+str(base)+'_'+str(atom))

	if not 'plots' in os.listdir():
		os.mkdir('plots')

	shutil.move(di+'/plot_base_'+str(base)+'_'+str(atom)+'.png',di+'/plots/plot_base_'+str(base)+'_'+str(atom)+'.png')			

main()

