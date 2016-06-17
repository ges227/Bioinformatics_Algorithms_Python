#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

import sys
from Bio import SeqIO
f= open(sys.argv[1])
fasta_seqs= SeqIO.parse(f,'fasta')

fasta_matrix=[]
for fasta in fasta_seqs:
	fasta_matrix.append(str(fasta.seq))
seqlen= len(fasta_matrix[1])
profiledict= {"A":[0]*seqlen,"C":[0]*seqlen,"G":[0]*seqlen,"T":[0]*seqlen}
for key in profiledict:
	for i in range(0,seqlen):
		for j in range(0,len(fasta_matrix)):
			if str(fasta_matrix[j][i])==str(key):
				profiledict[key][i]+=1

for key in profiledict:
	nucprofile= map(str, profiledict[key])
	print key+":", " ".join(nucprofile)
consensus=["a"]*seqlen
for i in range(0,seqlen):
	highest=-1
	for key in profiledict: 
		if int(profiledict[key][i])>highest:
			highest=profiledict[key][i]
			consensus[i]=key
print "Consensus:", "".join(consensus)