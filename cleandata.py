import os
import datetime
import re

def main():
	mergePitData("RW")
	mergePitData("RO")
	# mergeQLengthData("responsetime", "RO")
	# mergeQLengthData("responsetime", "RW")
	# mergeQLengthData("multiplicity", "RO")
	# mergeQLengthData("multiplicity", "RW")
	mergeQLengthData("inout_", "RO")
	mergeQLengthData("inout_", "RW")


def mergePitData(config):
	#print(next(os.walk("."))[1])
	fname = 'pointtime_'+config+'.tsv'
	header = "workload\ttimestamp\tpit\n"
	fout = open(fname,"w")
	fout.write(header)
	origDir = os.getcwd()
	os.chdir("output")
	for root, dirs, files in os.walk("."):
		for dir in dirs:
			if config in dir:
				workload = re.findall('\d+', dir)[0]
				pathToOutput = os.getcwd()
				os.chdir(dir)
				pitFile = open("Pointintime.csv")
				next(pitFile)
				count = 0
				for line in pitFile:
					splitLine  = line.split(",");
					fout.write(workload + "\t" + str(count) +  "\t" + splitLine[1])
					count = count + 50
				pitFile.close()
				os.chdir(pathToOutput)
	os.chdir(origDir)
	# 		pitFile.close()
			# pathToOutput = os.getcwd()
			# os.chdir(dir)
			# for sroot, sdirs, sfiles in os.walk("."):
			# 	for name in sfiles:
			# 		if config in name:

			# 			print(name)
	# for x in os.walk("."):
	# 	print(x[0])
	# 	if config in x[0]:
	# 		workload = re.findall('\d+', x[0])[0]
	# 		os.chdir(x[0])
	# 		pitFile = open("Pointintime.csv")
	# 		next(pitFile)
	# 		count = 0
	# 		for line in pitFile:
	# 			splitLine  = line.split(",");
	# 			fout.write(workload + "\t" + str(count) +  "\t" + splitLine[1] + "\n")
	# 			count = count + 50
	# 		pitFile.close()
	
	fout.close()

def mergeQLengthData(metric, config):
	fname = metric + config + '.csv'
	header = "workload,type,date_time,total_http\n"
	fout = open(fname,"w")
	fout.write(header)
	pathToHome = os.getcwd()
	os.chdir("output")
	for root, dirs, files in os.walk("."):
		for dir in dirs:
			pathToOutput = os.getcwd()
			os.chdir(dir)
			for sroot, sdirs, sfiles in os.walk("."):
				for name in sfiles:
					if metric in name:
	   					if config in name:
		   					splitName = name.split('_')
		   					serverType = splitName[1]
		   					workload = re.findall('\d+', splitName[3])[0]
		   					datafile = open(name)
		   					next(datafile)
		   					count = 0;
		   					for line in datafile:
		   						splitLine = line.split(",")
		   						fout.write(workload + "," + serverType.lower() + "," + str(count) +"," + splitLine[1] + "\n")
		   						count = count + 50
			os.chdir(pathToOutput)
	os.chdir(pathToHome)

main()
