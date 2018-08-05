from bs4 import BeautifulSoup
import sys

def extractPSG(infile):
    with open(infile) as f:
        soup = BeautifulSoup(f, 'xml')

    stages = []
    for c in soup.CMPStudyConfig.SleepStages:
        stages.append(c.string)

    return map(int,stages)

stages = extractPSG(sys.argv[1])

print stages

