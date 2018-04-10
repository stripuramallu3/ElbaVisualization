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
		for line in pitRW:
			RWout.write(workload + ", " + line)
		pitRW.close()
		os.chdir("../")
	elif "RO" in x[0]:
		workload = re.findall('\d+', x[0])[0]
		os.chdir(x[0])
		pitRO = open("Pointintime.csv")
		next(pitRO)
		for line in pitRO:
			ROout.write(workload + ", " + line)
		pitRO.close()
		os.chdir("../")
RWout.close()
ROout.close()

