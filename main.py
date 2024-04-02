from Bio import SeqIO
#import numpy as np
import re
import csv

PAMlist = []
AllPAMS = []
PAMre = re.compile('.{5}(?=TGGAGCAACACCTGAAGGAAGGCTTGATGAGC)')

for i1 in range(4):
    match i1:
        case 0:
            b0 = 'A'
        case 1:
            b0 = 'T'
        case 2:
            b0 = 'C'
        case 3:
            b0 = 'G'
    for i2 in range(4):
        match i2:
            case 0:
                b1 = 'A'
            case 1:
                b1 = 'T'
            case 2:
                b1 = 'C'
            case 3:
                b1 = 'G'
        for i3 in range(4):
            match i3:
                case 0:
                    b2 = 'A'
                case 1:
                    b2 = 'T'
                case 2:
                    b2 = 'C'
                case 3:
                    b2 = 'G'
            #tempString = (b0 + b1 + b2)
            #AllPAMS.append(tempString)
            for i4 in range(4):
                match i4:
                    case 0:
                        b3 = 'A'
                    case 1:
                        b3 = 'T'
                    case 2:
                        b3 = 'C'
                    case 3:
                        b3 = 'G'
                #tempString = (b0 + b1 + b2 + b3)
                #AllPAMS.append(tempString)
                
                for i5 in range(4):
                    match i5:
                        case 0:
                            b4 = 'A'
                        case 1:
                            b4 = 'T'
                        case 2:
                            b4 = 'C'
                        case 3:
                            b4 = 'G'
                    tempString = (b0 + b1 + b2 + b3 + b4)
                    AllPAMS.append(tempString)

# Dictionary to store the counts of each type of PAM
PAMDict = dict.fromkeys(AllPAMS, 0)

in_file = input("Please input Fasta file location: (no file extention)\n") + '.fasta'

for record in SeqIO.parse(in_file, "fasta"):
    tempPAM = PAMre.search(str(record.seq))
    if tempPAM:
        PAMDict[str(tempPAM.group())] += 1

outputFileName = input("please input desired output csv file name (no file extension): ") + ".csv"

with open(outputFileName, 'w') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(['PAM', 'frequency'])
    writer.writerows(PAMDict.items())
