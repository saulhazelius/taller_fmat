import re
import os
import sys
import glob
import shutil
import matplotlib.pyplot as plt
## creates new experimental files. csv format


atom = sys.argv[1]
di = os.getcwd()
exdi = di+'/experimental'

os.chdir(exdi)

exfs = glob.glob('*txt')


def replace_exp():
        """creates csv files"""
        exp = []
        if not 'new' in os.listdir(exdi):
                os.mkdir('new')
        for file in exfs:
                f = open(file,'r')
		
                name = file.split('.txt')[0]+'_new_'+str(atom)+'.csv'
                ff = open(name,'w')
                ff.write('label,atom,value')
                ff.write('\n')
	
                for line in f:
                        if  not re.search("#",line) and line.split()[1] == atom:
                                if not line.split()[2] == '--' and not line.split()[2] == '*': # harnessing that the first C shift exists
                                        ff.write(line.split()[0])	
                                        ff.write(',')	
                                        ff.write(line.split()[1])	
                                        ff.write(',')	
                                        ff.write(line.split()[2])
                                        ff.write('\n')
					
                                        exp.append(float(line.split()[2])) #str to float for plotting
                                if line.split()[2] == '--' or line.split()[2] == '*':
                                        nl = line.replace(line.split()[2],str(exp[-1]))
                                        ff.write(nl.split()[0])	
                                        ff.write(',')	
                                        ff.write(nl.split()[1])	
                                        ff.write(',')	
                                        ff.write(nl.split()[2])	
                                        ff.write('\n')
                                        exp.append(exp[-1])	
					
                f.close()
                ff.close()
                shutil.move(exdi+'/'+name,exdi+'/new/'+name) ## must be string not io wrapper

replace_exp()


