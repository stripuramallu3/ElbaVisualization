import os
import datetime
import re

RWfname = 'RW%s.csv' % datetime.datetime.now().strftime("_%Y-%m-%d_%H:%M:%S")
ROfname = 'RO%s.csv' % datetime.datetime.now().strftime("_%Y-%m-%d_%H:%M:%S")
header = "workload, timestamp, pit\n"
RWout=open(RWfname,"a")
RWout.write(header)
ROout=open(ROfname,"a")
ROout.write(header)

os.chdir("output")
for x in os.walk("."):
	if "RW" in x[0]:
		workload = re.findall('\d+', x[0])[0]
		os.chdir(x[0])
		pitRW = open("Pointintime.csv")
		next(pitRW)
		count = 0
		for line in pitRW:
			splitLine  = line.split(",");
			RWout.write(workload + ", " + str(count) +  ", " + splitLine[1])
			count = count + 50
		pitRW.close()
		os.chdir("../")
	elif "RO" in x[0]:
		workload = re.findall('\d+', x[0])[0]
		os.chdir(x[0])
		pitRO = open("Pointintime.csv")
		next(pitRO)
		count = 0
		for line in pitRO:
			splitLine  = line.split(",");
			ROout.write(workload + ", " + line)
			count = count + 50
		pitRO.close()
		os.chdir("../")
RWout.close()
ROout.close()

