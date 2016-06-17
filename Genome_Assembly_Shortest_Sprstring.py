#Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).
#The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
#Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
#

import sys
records=[]
f=open(sys.argv[1])
records = [line.rstrip('\n') for line in f]
f.close()
#print "records with removed new line\n",records

def findmaxoverlap(seq1,seq2):
	overlapmerge=''
	overlsize=0
	for kay in range(1,len(seq1)):
		suf1=seq1[-kay:]
		pref2=seq2[:kay]
		pref1=seq1[:kay]
		suf2=seq2[-kay:]
		if ((suf1==pref2) & (kay>overlsize)):
			overlapmerge=seq1+seq2[kay:]
			overlsize=kay
		if ((pref1==suf2) & (kay>overlsize)):
			overlapmerge=seq2+seq1[kay:]
			overlsize=kay
	return overlapmerge,overlsize


while len(records)>1:
	mostoverlap=''
	maxlength=0
	remove1=0
	remove2=0
	#print 'records pre-process\n',records
	for t in range(0,len(records)):
		for s in range(t+1,len(records)):
			if records[s]!=records[t]:
				overlapstr,overlapsize=findmaxoverlap(records[s],records[t])
				if overlapsize>maxlength:
					maxlength=overlapsize
					mostoverlap=overlapstr
					remove1=records[s]
					#print remove1
					remove2=records[t]
					#print remove2
	recset=set(records)
	recset.remove(remove1)
	recset.remove(remove2)
	recset.add(mostoverlap)
	records=list(recset)
print records[0]