import os
import datetime
import re

# RWfname = 'pointtime_RW.tsv' 
# ROfname = 'pointtime_RO.tsv' 
# header = "workload\ttimestamp\tpit\n"
# RWout=open(RWfname,"w")
# RWout.write(header)
# ROout=open(ROfname,"w")
# ROout.write(header)

# os.chdir("output")
# for x in os.walk("."):
# 	if "RW" in x[0]:
# 		workload = re.findall('\d+', x[0])[0]
# 		os.chdir(x[0])
# 		pitRW = open("Pointintime.csv")
# 		next(pitRW)
# 		count = 0
# 		for line in pitRW:
# 			splitLine  = line.split(",");
# 			RWout.write(workload + "\t" + str(count) +  "\t" + splitLine[1])
# 			count = count + 50
# 		pitRW.close()
# 		os.chdir("../")
# 	elif "RO" in x[0]:
# 		workload = re.findall('\d+', x[0])[0]
# 		os.chdir(x[0])
# 		pitRO = open("Pointintime.csv")
# 		next(pitRO)
# 		count = 0
# 		for line in pitRO:
# 			splitLine  = line.split(",");
# 			ROout.write(workload + "\t" + str(count) +  "\t" + splitLine[1])
# 			count = count + 50
# 		pitRO.close()
# 		os.chdir("../")
# RWout.close()
# ROout.close()
def main():
	mergePitData("RW")
	mergePitData("RO")
	mergeQLengthData("reponsetime")
	# mergeQLengthData("multiplicity")
	# mergeQLengthData("inout")

def mergePitData(config):
	fname = 'pointtime_'+config+'.tsv'
	header = "workload\ttimestamp\tpit\n"
	fout = RWout=open(RWfname,"w")
	fout.write(header)
	os.chdir("output")
	for x in os.walk("."):
		if config in x[0]:
			workload = re.findall('\d+', x[0])[0]
			os.chdir(x[0])
			pitFile = open("Pointintime.csv")
			next(pitFile)
			count = 0
			for line in pitFile:
				splitLine  = line.split(",");
				RWout.write(workload + "\t" + str(count) +  "\t" + splitLine[1])
				count = count + 50
			pitFile.close()
			os.chdir("../")
	fout.close()

def mergeQLengthData(metric):
	fout = metric + '.tsv'
	header = "workload\ttype\tdate_time\ttotal_http\n"
	fout = RWout=open(RWfname,"w")
	fout.write(header)
	os.chdir("output")
	for x in os.walk("."):